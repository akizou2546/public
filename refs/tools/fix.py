# 変換後のPowerPointを補正する: フォント名、言語、部首用の文字、フォントの埋め込み、リンクの色
import sys, re, os, shutil, zipfile, unicodedata, glob
raw, out = sys.argv[1], sys.argv[2]
d = 'build_x'; shutil.rmtree(d, ignore_errors=True)
zipfile.ZipFile(raw).extractall(d)
def radicals(m):
    return m.group(1) + ''.join(unicodedata.normalize('NFKC', c) if ('⺀' <= c <= '⿟' or 0xfb00 <= ord(c) <= 0xfb06) else c for c in m.group(2)) + m.group(3)
for f in glob.glob(d + '/ppt/**/*.xml', recursive=True):
    s = open(f, encoding='utf8').read(); o = s
    s = re.sub(r'typeface="(NotoSansJP|Times New Roman)"', 'typeface="Noto Sans JP"', s)
    s = re.sub(r' lang="[^"]*"', ' lang="ja-JP"', s)
    s = re.sub(r'(<a:t>)([^<]*)(</a:t>)', radicals, s)
    if 'theme' in f:
        s = re.sub(r'<a:hlink>.*?</a:hlink>', '<a:hlink><a:srgbClr val="0017c1"/></a:hlink>', s)
    if s != o: open(f, 'w', encoding='utf8').write(s)

# 引用の番号: 別の箱になった番号を消し、左隣の根拠のメッセージの末尾に上付きの区切りとしてつなぐ
# リンク: 原稿の <a href> の文字と一致する箱に、下線とリンクを戻す
md = open(sys.argv[3], encoding='utf8').read() if len(sys.argv) > 3 else ''
links = dict((t, u) for u, t in re.findall(r'<a href="([^"]+)">([^<]+)</a>', md))
restored = 0; sups = 0
for f in sorted(glob.glob(d + '/ppt/slides/slide*.xml')):
    s = open(f, encoding='utf8').read(); o = s
    sps = re.findall(r'<p:sp>.*?</p:sp>', s, re.S)
    def info(sp):
        m = re.search(r'<a:off x="(\d+)" y="(\d+)"/><a:ext cx="(\d+)" cy="(\d+)"', sp)
        return (''.join(re.findall(r'<a:t>([^<]*)</a:t>', sp)), *(int(v) for v in m.groups())) if m else ('', 0, 0, 0, 0)
    for sp in sps:
        t, x, y, cx, cy = info(sp)
        if re.fullmatch(r'\d+', t.strip()) and y < 6000000 and ' sz="1200"' in sp:
            host = [h for h in sps if h != sp and ' sz="1800"' in h and abs(info(h)[2] - y) < 60000 and info(h)[1] < x <= info(h)[1] + info(h)[3] + 400000]
            if not host: continue
            h = host[0]
            runs = re.findall(r'<a:r>.*?</a:r>', h, re.S)
            rpr = re.search(r'<a:rPr[^>]*>.*?</a:rPr>', runs[-1], re.S).group(0)
            rpr = re.sub(r' sz="\d+"', ' sz="2100" baseline="30000"', rpr, 1).replace(' b="1"', ' b="0"')
            new = h.replace(runs[-1], runs[-1] + f'<a:r>{rpr}<a:t>{t.strip()}</a:t></a:r>')
            new = re.sub(r'(<a:ext cx=")(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 300000), new, 1)
            s = s.replace(sp, '').replace(h, new); sups += 1
    rels_p = f.replace('/slides/', '/slides/_rels/') + '.rels'
    rels = open(rels_p, encoding='utf8').read(); k = 0
    for sp in re.findall(r'<p:sp>.*?</p:sp>', s, re.S):
        t = info(sp)[0].strip()
        if t in links:
            k += 1; rid = f'rIdL{k}'
            new = re.sub(r'<a:rPr([^>]*)>(.*?)</a:rPr>', lambda m: f'<a:rPr{m.group(1)} u="sng">{m.group(2)}<a:hlinkClick r:id="{rid}"/></a:rPr>', sp, flags=re.S)
            s = s.replace(sp, new)
            rels = rels.replace('</Relationships>', f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="{links[t]}" TargetMode="External"/></Relationships>')
            restored += 1
    if s != o:
        open(f, 'w', encoding='utf8').write(s); open(rels_p, 'w', encoding='utf8').write(rels)
print('引用の番号:', sups, 'リンク:', restored, '/', len(links))

# フォントの埋め込み（前回の資料と同じ Noto Sans JP の400と700）
os.makedirs(d + '/ppt/fonts', exist_ok=True)
for i in (1, 2): shutil.copy(f'fonts/font{i}.fntdata', d + f'/ppt/fonts/font{i}.fntdata')
p = d + '/[Content_Types].xml'; s = open(p, encoding='utf8').read()
if 'fntdata' not in s: s = s.replace('<Default ', '<Default Extension="fntdata" ContentType="application/x-fontdata"/><Default ', 1)
open(p, 'w', encoding='utf8').write(s)
p = d + '/ppt/_rels/presentation.xml.rels'; s = open(p, encoding='utf8').read()
s = s.replace('</Relationships>', ''.join(f'<Relationship Id="rIdFont{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/font" Target="fonts/font{i}.fntdata"/>' for i in (1, 2)) + '</Relationships>')
open(p, 'w', encoding='utf8').write(s)
p = d + '/ppt/presentation.xml'; s = open(p, encoding='utf8').read()
s = re.sub(r' (embedTrueTypeFonts|saveSubsetFonts)="[^"]*"', '', s)
s = s.replace('<p:presentation ', '<p:presentation embedTrueTypeFonts="1" saveSubsetFonts="1" ', 1)
s = re.sub(r'(<p:notesSz [^>]*/>)', r'\1<p:embeddedFontLst><p:embeddedFont><p:font typeface="Noto Sans JP" panose="020B0200000000000000" pitchFamily="34" charset="-128"/><p:regular r:id="rIdFont1"/><p:bold r:id="rIdFont2"/></p:embeddedFont></p:embeddedFontLst>', s, 1)
open(p, 'w', encoding='utf8').write(s)
if os.path.exists(out): os.remove(out)
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(d + '/[Content_Types].xml', '[Content_Types].xml')
    for root, _, files in os.walk(d):
        for n in files:
            full = os.path.join(root, n); arc = os.path.relpath(full, d)
            if arc != '[Content_Types].xml': z.write(full, arc)
print('fixed ->', out)
