"""Marpの編集可能PowerPointを補正し、検査する"""
import re
import shutil
import sys
import unicodedata
import zipfile

FONT = "Noto Sans JP"
RADICAL = re.compile("[⺀-⿟]")
TEXT = re.compile(r"(<a:t>)([^<]*)(</a:t>)")
PART = re.compile(r"ppt/slides/[^/]+\.xml$")


def normalize_radicals(text):
    return RADICAL.sub(lambda m: unicodedata.normalize("NFKC", m.group()), text)


def _rewrite(src, dst, edit):
    """zip内の対象XMLに edit(name, xml) を適用して書き出す"""
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst + ".tmp", "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if PART.match(item.filename):
                data = edit(item.filename, data.decode("utf8")).encode("utf8")
            zout.writestr(item, data)
    shutil.move(dst + ".tmp", dst)


SHAPE = re.compile(r"<p:sp>.*?</p:sp>", re.S)
SUP = re.compile(r"<sup>(.*?)</sup>")


def merge_cites(xml, cites):
    """引用の番号を、直前の根拠のメッセージの末尾に上付きの文字としてつなぐ。
    変換後は番号が別の箱になり、PowerPoint側で文の幅が変わると文に重なるため"""
    def box(m):
        x, y = map(int, re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"', m.group()).groups())
        return x, y, "".join(t.group(2) for t in TEXT.finditer(m.group())).strip()

    dash = lambda t: re.sub("[‐-―−]", "-", t)  # 変換で横線が別の文字に変わるので、そろえて比べる
    cites = {dash(c): c for c in cites}
    shapes = [m for m in SHAPE.finditer(xml) if "<a:off " in m.group() and "<a:t>" in m.group()]
    edits = []  # (始まり, 終わり, 置き換える文字列)
    for sup in shapes:
        sx, sy, text = box(sup)
        if dash(text) not in cites or 'sz="1200"' not in sup.group():
            continue
        text = cites[dash(text)]
        hosts = [h for h in shapes if 'b="1"' in h.group() and 'val="0017c1"' in h.group()
                 and abs(box(h)[1] - sy) < 100000 and box(h)[0] < sx]
        if not hosts:
            continue
        host = max(hosts, key=lambda h: box(h)[0])
        last = list(RUN.finditer(host.group()))[-1]
        # 約58〜65%に縮むので、12pt を保つために 21pt を指定する
        props = re.sub(r'\bb="1"', 'b="0"', re.sub(r'sz="\d+"', 'sz="2100" baseline="30000"', last.group(1)))
        run = f'<a:r>{props}>{last.group(2) or ""}</a:rPr><a:t> {text}</a:t></a:r>'
        at = host.start() + last.end()
        edits += [(sup.start(), sup.end(), ""), (at, at, run)]
    for a, b, new in sorted(edits, reverse=True):
        xml = xml[:a] + new + xml[b:]
    return xml


def check_cites(md):
    """引用の番号と参考文献の番号が対応しているか。番号は初めて出た順に振る（Scienceの決まり）"""
    body, _, refs = md.rpartition("# 参考文献")
    cited = []
    for sup in SUP.findall(body):
        for part in sup.split(","):
            a, _, b = re.sub(r"\s", "", part).replace("–", "-").partition("-")
            cited += range(int(a), int(b or a) + 1)
    listed = [int(n) for n in re.findall(r"<tr><td>(\d+)\.</td>", refs)]
    out = []
    first = list(dict.fromkeys(cited))
    if first != sorted(first):
        out.append(f"引用の番号が初めて出た順になっていない {first}")
    if listed != list(range(1, len(listed) + 1)):
        out.append(f"参考文献の番号が1からの連番でない {listed}")
    out += [f"引用 {n} が参考文献にない" for n in sorted(set(cited) - set(listed))]
    out += [f"参考文献 {n} がどこからも引用されていない" for n in sorted(set(listed) - set(cited))]
    return out


def fix_pptx(src, dst, font=FONT, cites=()):
    def edit(name, xml):
        xml = merge_cites(xml, cites)
        xml = TEXT.sub(lambda m: m.group(1) + normalize_radicals(m.group(2)) + m.group(3), xml)
        xml = re.sub(r'typeface="[^"+][^"]*"', f'typeface="{font}"', xml)
        return re.sub(r'\blang="[^"]*"', 'lang="ja-JP"', xml)

    _rewrite(src, dst, edit)


def check_pptx(path):
    out = []
    with zipfile.ZipFile(path) as z:
        fonts = [n for n in z.namelist() if n.endswith(".fntdata")]
        if len(fonts) < 2 or 'embedTrueTypeFonts="1"' not in z.read("ppt/presentation.xml").decode("utf8"):
            out.append("ppt/presentation.xml: フォントが埋め込まれていない")
        for name in filter(PART.match, z.namelist()):
            xml = z.read(name).decode("utf8")
            text = "".join(m.group(2) for m in TEXT.finditer(xml))
            small = [int(s) / 100 for s in re.findall(r'\bsz="(\d+)"', xml) if int(s) < 1200]
            fonts = set(re.findall(r'typeface="([^"+][^"]*)"', xml)) - {FONT}
            if small:
                out.append(f"{name}: 12pt未満の文字がある {sorted(set(small))}")
            if "。" in text:
                out.append(f"{name}: 句点がある")
            if RADICAL.search(text):
                out.append(f"{name}: 部首用の文字が残っている")
            if fonts:
                out.append(f"{name}: フォントが {FONT} 以外 {sorted(fonts)}")
    return out


def check_source(md):
    out = []
    for i, slide in enumerate(re.split(r"^---$", md, flags=re.M), 1):
        if "。" in slide:
            out.append(f"原稿 {i}区画目: 句点がある")
        if re.search(r"_class:\s*(cover|source)", slide):
            continue
        for h in re.findall(r"^## (.+)$", slide, flags=re.M):
            width = sum(0.5 if c.isascii() else 1 for c in h)  # 半角の英数字は半分の幅として数える
            if width > 32:
                out.append(f"原稿 {i}区画目: メインメッセージが32字を超える（{width:g}字）")
    return out


LINK = re.compile(r'<a href="([^"]+)">(.*?)</a>')
RUN = re.compile(r"<a:r>(<a:rPr\b[^>]*?)(?:/>|>(.*?)</a:rPr>)<a:t>([^<]*)</a:t></a:r>", re.S)
HLINK = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"


def _squash(text):
    return re.sub(r"\s+", "", re.sub(r"<[^>]+>", "", text))


def add_links(path, md):
    """原稿の <a href> を、PowerPointのリンクに戻す（変換でリンクは消え、文字は複数の区切りに分かれる）。
    戻せなかったリンクの一覧を返す"""
    links = [(url, _squash(text)) for url, text in LINK.findall(md)]
    done = set()
    with zipfile.ZipFile(path) as zin:
        items = zin.infolist()
        files = {i.filename: zin.read(i.filename) for i in items}
    for name in filter(PART.match, list(files)):
        xml = files[name].decode("utf8")
        runs = list(RUN.finditer(xml))
        marks = {}  # 区切りの番号 → リンクの番号
        for n, (url, want) in enumerate(links):
            for i in range(len(runs)):
                got, j = "", i
                while j < len(runs) and want.startswith(got) and got != want:
                    got += _squash(runs[j].group(3))
                    j += 1
                if got == want:
                    marks.update({k: n for k in range(i, j)})
                    done.add(n)
                    break
        if not marks:
            continue
        for k in sorted(marks, reverse=True):
            m = runs[k]
            run = (f'<a:r>{m.group(1)} u="sng">{m.group(2) or ""}<a:hlinkClick r:id="rIdLink{marks[k]}"/>'
                   f'</a:rPr><a:t>{m.group(3)}</a:t></a:r>')
            xml = xml[:m.start()] + run + xml[m.end():]
        files[name] = xml.encode("utf8")
        rel_name = name.replace("slides/", "slides/_rels/") + ".rels"
        rel = files[rel_name].decode("utf8")
        for n in sorted(set(marks.values())):
            url = links[n][0].replace("&", "&amp;")
            rel = rel.replace("</Relationships>", f'<Relationship Id="rIdLink{n}" Type="{HLINK}" Target="{url}" TargetMode="External"/></Relationships>')
        files[rel_name] = rel.encode("utf8")
    # PowerPointはリンクの色をテーマから取るので、テーマ側も主色にそろえる
    for name in [n for n in files if re.match(r"ppt/theme/theme\d+\.xml$", n)]:
        files[name] = re.sub(r"(<a:(hlink|folHlink)><a:srgbClr val=\")[0-9a-fA-F]{6}", r"\g<1>0017c1",
                             files[name].decode("utf8")).encode("utf8")
    # PowerPointはリンクの色をテーマから取るので、テーマ側も主色にそろえる
    for name in [n for n in files if re.match(r"ppt/theme/theme\d+\.xml$", n)]:
        files[name] = re.sub(r"(<a:(?:hlink|folHlink)><a:srgbClr val=\")[0-9a-fA-F]{6}", r"\g<1>0017c1",
                             files[name].decode("utf8")).encode("utf8")
    with zipfile.ZipFile(path + ".tmp", "w", zipfile.ZIP_DEFLATED) as zout:
        for item in items:
            zout.writestr(item, files[item.filename])
    shutil.move(path + ".tmp", path)
    return [f"リンクを戻せなかった: {links[n][0]}" for n in range(len(links)) if n not in done]


def eot(ttf_path):
    """フォントを、PowerPointの埋め込み形式（EOT 2.2、圧縮なし）に包む"""
    import struct

    from fontTools.ttLib import TTFont

    data = open(ttf_path, "rb").read()
    font = TTFont(ttf_path)
    os2 = font["OS/2"]
    head = struct.pack("<II", 0x00020002, 0) + bytes(_panose(os2)) + struct.pack(
        "<BBIHH", 1, os2.fsSelection & 1, os2.usWeightClass, os2.fsType, 0x504C)
    head += struct.pack("<6I", os2.ulUnicodeRange1, os2.ulUnicodeRange2, os2.ulUnicodeRange3, os2.ulUnicodeRange4,
                        getattr(os2, "ulCodePageRange1", 0), getattr(os2, "ulCodePageRange2", 0))
    head += struct.pack("<5I", font["head"].checkSumAdjustment, 0, 0, 0, 0)
    for name_id in (1, 2, 5, 4):  # ファミリー名、スタイル名、版、完全名
        text = (font["name"].getDebugName(name_id) or "").encode("utf-16-le")
        head += struct.pack("<HH", 0, len(text)) + text
    head += struct.pack("<HH", 0, 0) + struct.pack("<IIHHII", 0, 0, 0, 0, 0, 0)  # RootString以降は空
    return struct.pack("<II", 8 + len(head) + len(data), len(data)) + head + data


def _panose(os2):
    p = os2.panose
    return [p.bFamilyType, p.bSerifStyle, p.bWeight, p.bProportion, p.bContrast,
            p.bStrokeVariation, p.bArmStyle, p.bLetterForm, p.bMidline, p.bXHeight]


def embed_fonts(path, regular, bold, family=FONT):
    """標準と太字のフォントを埋め込み、PowerPointに埋め込みフォントを使うよう指定する"""
    from fontTools.ttLib import TTFont

    panose = "".join("%02X" % v for v in _panose(TTFont(regular)["OS/2"]))
    rels = "".join(f'<Relationship Id="rIdFont{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                   f'relationships/font" Target="fonts/font{i}.fntdata"/>' for i in (1, 2))
    listing = (f'<p:embeddedFontLst><p:embeddedFont><p:font typeface="{family}" panose="{panose}" pitchFamily="34" '
               'charset="-128"/><p:regular r:id="rIdFont1"/><p:bold r:id="rIdFont2"/></p:embeddedFont></p:embeddedFontLst>')
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(path + ".tmp", "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            xml = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                xml = xml.decode("utf8").replace(
                    "<Default ", '<Default Extension="fntdata" ContentType="application/x-fontdata"/><Default ', 1).encode("utf8")
            elif item.filename == "ppt/_rels/presentation.xml.rels":
                xml = xml.decode("utf8").replace("</Relationships>", rels + "</Relationships>").encode("utf8")
            elif item.filename == "ppt/presentation.xml":
                text = xml.decode("utf8")
                at = (re.search(r"<p:notesSz[^>]*/>", text) or re.search(r"<p:sldSz[^>]*/>", text)).end()
                text = text[:at] + listing + text[at:]
                # この指定がないと、PowerPointは埋め込んだフォントを使わない。同じ属性が2つあるとファイルが開けなくなる
                for attr in ("saveSubsetFonts", "embedTrueTypeFonts"):
                    text = re.sub(rf'(<p:presentation\b[^>]*?)\s{attr}="[^"]*"', r"\1", text, count=1)
                    text = text.replace("<p:presentation ", f'<p:presentation {attr}="1" ', 1)
                xml = text.encode("utf8")
            zout.writestr(item, xml)
        zout.writestr("ppt/fonts/font1.fntdata", eot(regular))
        zout.writestr("ppt/fonts/font2.fntdata", eot(bold))
    shutil.move(path + ".tmp", path)


def pdf_font_problems(pdffonts_output):
    """pdffonts の出力を受け取り、Noto Sans JP 以外の埋め込みフォントを報告する"""
    names = [line.split()[0] for line in pdffonts_output.splitlines()[2:] if line.strip()]
    if not names:
        return ["PDF: 埋め込みフォントがない"]
    return [f"PDF: {FONT} 以外のフォントで描かれている {n}" for n in sorted(set(names)) if "NotoSansJP" not in n]


if __name__ == "__main__":
    if sys.argv[1] == "--pdf":  # python3 fix.py --pdf out/deck.pdf
        import subprocess

        problems = pdf_font_problems(subprocess.run(["pdffonts", sys.argv[2]], capture_output=True, text=True).stdout)
        print("\n".join(problems) or "PDFのフォントOK")
        sys.exit(1 if problems else 0)
    raw, dst, md, regular, bold = sys.argv[1:6]
    fix_pptx(raw, dst, cites=set(SUP.findall(open(md, encoding="utf8").read())))
    embed_fonts(dst, regular, bold)
    source = open(md, encoding="utf8").read()
    problems = check_source(source) + check_cites(source) + add_links(dst, source) + check_pptx(dst)
    with zipfile.ZipFile(dst) as z:
        joined = sum(z.read(n).count(b'baseline="30000"') for n in z.namelist() if PART.match(n))
    if joined != len(SUP.findall(source)):
        problems.append(f"引用の番号をつなげなかった箇所がある（原稿 {len(SUP.findall(source))}、ファイル {joined}）")
    print("\n".join(problems) or "検査OK")
    sys.exit(1 if problems else 0)
