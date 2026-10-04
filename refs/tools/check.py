# 自動検査: 12pt未満、句点、32字超、部首用の文字、指定外のフォント名、フォントの埋め込み、PDFのフォント
import sys, re, zipfile, subprocess
n = sys.argv[1]; bad = []
md = open(n + '.md', encoding='utf8').read()
def width(t): return sum(0.5 if (c.isascii() and (c.isalnum() or c == ' ')) else 1 for c in t)
for m in re.finditer(r'^## (.+)$', md, re.M):
    t = re.sub(r'<[^>]+>', '', m.group(1))
    if width(t) > 32: bad.append(f'32字超({width(t)}): {t}')
for m in re.finditer(r'^#{1,3} (.+)$|<h3>(.*?)</h3>', md, re.M):
    t = re.sub(r'<[^>]+>', '', m.group(1) or m.group(2))
    if '。' in t: bad.append('句点: ' + t)
z = zipfile.ZipFile(n + '.pptx')
for name in z.namelist():
    if not re.match(r'ppt/slides/slide\d+\.xml', name): continue
    s = z.read(name).decode('utf8')
    for v in re.findall(r' sz="(\d+)"', s):
        if int(v) < 1200: bad.append(f'{name}: 12pt未満 sz={v}')
    for t in re.findall(r'<a:t>([^<]*)</a:t>', s):
        if any(0xfb00 <= ord(ch) <= 0xfb06 for ch in t): bad.append(f'{name}: 合字 {t}')
        if any('⺀' <= c <= '⿟' for c in t): bad.append(f'{name}: 部首用の文字 {t}')
        if '。' in t: bad.append(f'{name}: 句点 {t}')
    for v in set(re.findall(r'typeface="([^"]*)"', s)) - {'Noto Sans JP'}: bad.append(f'{name}: 指定外のフォント {v}')
    for v in set(re.findall(r' lang="([^"]*)"', s)) - {'ja-JP'}: bad.append(f'{name}: 言語 {v}')
# リンクと引用
want = re.findall(r'<a href="([^"]+)">', md); got = []
for name in z.namelist():
    if re.match(r'ppt/slides/_rels/slide\d+\.xml\.rels', name): got += re.findall(r'hyperlink" Target="([^"]+)"', z.read(name).decode('utf8'))
for u in want:
    if u not in got: bad.append('リンクが戻っていない: ' + u)
cites = []
for v in re.findall(r'<sup>(\d+)</sup>', md):
    if v in cites: bad.append('引用が2回: ' + v)
    cites.append(v)
refs = re.findall(r'<tr><td>(\d+)\.</td>', md)
if cites != [str(i + 1) for i in range(len(cites))]: bad.append(f'引用が初めて出た順でない: {cites}')
if cites != refs: bad.append(f'引用と参考文献が対応しない: 引用{cites} 文献{refs}')
alltext = ''.join(''.join(re.findall(r'<a:t>([^<]*)</a:t>', z.read(nm).decode('utf8'))) for nm in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml', nm))
if len(re.findall(r'baseline="30000"', ''.join(z.read(nm).decode('utf8') for nm in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml', nm)))) != len(cites): bad.append('上付きの引用番号の数が原稿と合わない')
p = z.read('ppt/presentation.xml').decode('utf8')
if 'embedTrueTypeFonts="1"' not in p or '<p:embeddedFontLst>' not in p or 'ppt/fonts/font1.fntdata' not in z.namelist(): bad.append('フォントが埋め込まれていない')
out = subprocess.run(['pdffonts', n + '.pdf'], capture_output=True, text=True).stdout
print(out)
for line in out.splitlines()[2:]:
    if 'NotoSansJP' not in line.replace(' ', ''): bad.append('PDFに別のフォント: ' + line.split()[0])
    elif ' yes ' not in line: bad.append('PDFでフォントが埋め込まれていない: ' + line.split()[0])
print(f'{len(bad)}件'); [print(' -', b) for b in bad]
sys.exit(1 if bad else 0)
