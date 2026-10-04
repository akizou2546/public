#!/bin/bash
# deck.md から PowerPoint と PDF を作り直す。README.md の「作り直し方」を参照
set -e
n=${1:-deck}
out=claude-code-devcontainer-isms
export CHROME_NO_SANDBOX=1
timeout 300 ${MARP:-npx @marp-team/marp-cli} $n.md --no-stdin --theme-set theme.css --html --allow-local-files --pptx --pptx-editable -o raw-$n.pptx
python3 tools/fix.py raw-$n.pptx $out.pptx $n.md
soffice --headless --convert-to pdf $out.pptx >/dev/null 2>&1
cp $out.pptx $n.pptx; cp $out.pdf $n.pdf
python3 tools/check.py $n
rm -f raw-$n.pptx $n.pptx $n.pdf; rm -rf build_x
