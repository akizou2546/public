#!/usr/bin/env bash
# 原稿 → 編集できるPowerPoint → 補正・フォントとリンクの埋め込み・検査 → PDF → 確認用の画像
# 使い方: 資料のフォルダ（deck.md、theme.css、icons/、node_modules/ がある場所）で、このファイルを実行する
# --no-stdin: 付けないと、Marpが標準入力を原稿として待ち続けて止まることがある
# コンテナの中などでChromeが起動しないときは、CHROME_PATH と CHROME_NO_SANDBOX=1 を指定する
set -euo pipefail
TOOLS="$(cd "$(dirname "$0")" && pwd)"
FONTS=node_modules/@expo-google-fonts/noto-sans-jp

# Noto Sans JP がなければ入れる（ないと別のフォントで代用され、PDFの見た目が変わる）
if ! fc-list | grep -q "Noto Sans JP"; then
  mkdir -p ~/.local/share/fonts/notosansjp
  cp $FONTS/{400Regular,700Bold}/*.ttf ~/.local/share/fonts/notosansjp/
  fc-cache -f
fi

rm -rf out && mkdir out
timeout 120 node_modules/.bin/marp deck.md --no-stdin --theme-set theme.css --html --allow-local-files \
  --pptx --pptx-editable -o out/raw.pptx
python3 "$TOOLS/fix.py" out/raw.pptx out/deck.pptx deck.md \
  $FONTS/400Regular/NotoSansJP_400Regular.ttf $FONTS/700Bold/NotoSansJP_700Bold.ttf
timeout 120 soffice --headless --convert-to pdf --outdir out out/deck.pptx >/dev/null
python3 "$TOOLS/fix.py" --pdf out/deck.pdf
pdftoppm -r 80 -png out/deck.pdf out/page
rm out/raw.pptx
