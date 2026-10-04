# Claude CodeのDev ContainerをISMSで運用する流れ

Marpで書いたスライド資料の一式です。

## 中身

| ファイル | 内容 |
|---|---|
| claude-code-devcontainer-isms.pptx | 編集できるPowerPoint（Noto Sans JPを埋め込み済み） |
| claude-code-devcontainer-isms.pdf | 確認用のPDF |
| deck.md | Marpの原稿（全22枚） |
| theme.css | Marpのテーマ（デジタル庁デザインシステムの色と文字の決まりに沿う） |
| icons/ | 原稿が使うアイコン（Material Symbols Outlined、Apache-2.0） |
| fonts/ | Noto Sans JP の400と700（SIL Open Font License 1.1）。TTFと、PowerPointへの埋め込み用のfntdata |
| design.md | 設計書。読み手、章、決まりの一覧、判断の記録 |
| build.sh、tools/ | 作り直しと検査のスクリプト |

## プレビューだけしたいとき

VS Codeの拡張「Marp for VS Code」を入れ、設定の Markdown > Marp: Themes に `theme.css` を足し、HTMLを有効にして `deck.md` を開きます。
フォントが入っていない場合は、`fonts/` のTTFを先にインストールしてください。

## 作り直し方

必要なもの: Node.js、Google ChromeかChromium、LibreOffice、Python 3、poppler（pdffonts）、Noto Sans JP（`fonts/` のTTFをインストール）。

```bash
bash build.sh
```

`deck.md` を変換し、フォント名、言語、合字、引用の番号、リンク、フォントの埋め込みを補正して、PowerPointとPDFを上書きします。最後に自動検査（12pt未満、句点、32字を超えるメインメッセージ、フォント、リンク、引用と参考文献の対応）が走り、問題があれば件数と中身を表示します。

Chromeが見つからないときは、環境変数 `CHROME_PATH` に実行ファイルの場所を入れてください。

## 確かめていないこと

- PowerPointで開いたときの表示（作成した環境ではLibreOfficeでしか確かめていません）
- 付録の設定を入れた状態で実際に動くか
- 規格の現行版（2025年版）の本文との突き合わせ

詳しくは `design.md` を見てください。
