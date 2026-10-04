# 読み手から組み立てるスライド資料：Claude Code 用のスキルと作例

スライド資料を作るための Claude Code のスキルと、そのスキルで仕上げた作例（Claude Code の Dev Container を OWASP の10のリスクに照らした資料、全18枚）です。

## 入っているもの

```
skill/building-reader-first-slide-decks/     Claude Code に入れるスキル（このフォルダごと写す）
  SKILL.md                                   スキル本体（進め方、資料の型、言葉や図表の決まり）
  tools/build.sh                             原稿からPowerPointとPDFを作り、検査する
  tools/fix.py、test_fix.py                  変換後の補正、フォントとリンクの埋め込み、検査と、そのテスト
  tools/theme.css                            見た目（デジタル庁デザインシステムに沿ったテーマ）
  tools/package.json、package-lock.json      Marp、アイコン、フォントの版
  example/deck.md、icons/、deck.pdf          作例の原稿、アイコン、仕上がり
deck/out/deck.pptx、deck.pdf                 作例の完成ファイル（PowerPointはフォント埋め込み済み）
deck/docs/superpowers/                       作例の設計書と実行計画（決めたことと理由の記録）
```

資料を見るだけなら `deck/out/` の2つで足ります。

## Claude Code への入れ方

スキルのフォルダを、次のどちらかに写します。

```bash
# 自分のすべてのプロジェクトで使う
mkdir -p ~/.claude/skills
cp -r skill/building-reader-first-slide-decks ~/.claude/skills/

# 1つのリポジトリで、そこで作業する全員が使う（リポジトリにコミットする）
mkdir -p .claude/skills
cp -r skill/building-reader-first-slide-decks .claude/skills/
```

- Claude Code を起動した後に `skills` フォルダを初めて作った場合は、`/reload-skills` を実行します。すでにあるフォルダへの追加や編集は、そのまま反映されます
- 使うときは「このメモをスライドにして」のように頼むと、Claude が自分で呼びます。`/building-reader-first-slide-decks` と打って直接呼ぶこともできます

## 必要なもの

スキルが資料を組み立てるときに使います。

- Node.js（Marp CLI、アイコン、フォントを `npm ci` で入れる）
- Python 3 と `fonttools`（テストには `python-pptx` も要る）
- LibreOffice（`soffice`）
- Poppler（`pdffonts`、`pdftoppm`）
- Chrome か Chromium。コンテナの中などで起動しないときは、`CHROME_PATH` と `CHROME_NO_SANDBOX=1` を指定する

## 作例を作り直して動作を確かめる

```bash
SKILL=~/.claude/skills/building-reader-first-slide-decks
mkdir my-deck && cd my-deck
cp $SKILL/tools/{theme.css,package.json,package-lock.json} . && npm ci
cp -r $SKILL/example/icons . && cp $SKILL/example/deck.md .
$SKILL/tools/build.sh          # out/deck.pptx、out/deck.pdf、out/page-NN.png ができる
```

`build.sh` は、検査に1つでも引っかかると止まります。検査の中身は、12pt未満の文字、句点、文字化け、指定外のフォント、フォントの埋め込み、メインメッセージの長さ、引用と参考文献の対応、リンクの埋め込みです。

## 作例について知っておいてほしいこと

- 表紙の氏名は「（氏名）」のままです。使うときに書き換えてください
- 言葉は ISMS（JIS Q 27000 系）の用語にそろえています。根拠は JIS Q 27000:2019 の転載サイト、JIPDEC のガイド、日本規格協会の目次で、JIS の本体は確かめていません
- 有効性（低減できる／低減できない）と「残留リスクが大きい構成」は、公開されている設定ファイルと OWASP の原文を読んで導いたものです。実機では試していません
- 対象は anthropics/claude-code の `.devcontainer`（commit 1c229fc、2026年10月2日時点）です。その後の変更は反映していません
- PowerPoint での表示は、作成者のパソコンで文字化けしないことを一度確かめています。その後に足した引用の上付き文字とリンクは、PowerPoint では確かめていません（PDF に変換して確認）
- 参考文献2（GitHub）のリンク先は、作成時に自動では開けず、未確認です
- このスキルは、Claude Code に実際に入れて呼ぶところまでは試していません。確かめたのは、スキルの文面どおりに原稿が書かれることと、付属の道具で作例が作り直せることです

## 利用条件

- 4枚目の図は、OWASP「Agentic Top 10 At A Glance」（CC BY-SA 4.0）をもとに作ったものです。この図を使った資料を配るときは、出典を示し、同じ条件（CC BY-SA 4.0）で配ってください
- アイコンは Material Symbols（Apache-2.0）、フォントは Noto Sans JP（SIL Open Font License 1.1）です
