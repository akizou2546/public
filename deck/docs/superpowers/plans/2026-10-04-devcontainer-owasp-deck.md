# devcontainer × OWASP Agentic Top 10 スライド Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Marpの原稿1つから、編集可能な `deck.pptx` とレビュー用の `deck.pdf` を作る。先に2〜6枚目のサンプルを作って確認を受け、その後に全15枚を仕上げる

**Architecture:** `deck.md` と `theme.css` をMarp CLIの編集可能方式でPowerPointに変換し、`fix.py` が文字とフォントを補正して標準グラフを差し込み、検査する。PDFは完成したPowerPointからLibreOfficeで作る。全工程は `build.sh` 1本で動く

**Tech Stack:** Marp CLI 4.5.1、LibreOffice 24.2、Chromium、Python 3（python-pptx 1.0.2、標準の unittest）、Material Symbols（`@material-symbols/svg-400` 0.47.6）

**Spec:** `docs/superpowers/specs/2026-10-04-devcontainer-owasp-deck-design.md`

## Global Constraints

- 文字は12pt以上（CSSでは16px以上）。標準グラフの文字も含む
- 句点（。）は一切使わない
- メインメッセージと根拠のメッセージは常体の文。体言止めにしない
- メインメッセージは32字以内で1行（表紙と出典を除く）
- 前のスライドのメインメッセージに出た単語を次のメインメッセージが受ける。目印は付けない
- 説明は図解・表・グラフ。図中の文字はラベルに限り、1行に収める
- フォント名は Noto Sans JP、太さは400と700のみ
- 文字の大きさ: メイン36px、根拠24px、ラベル20px、現在位置と補足16px
- 色: 文字 #1a1a1a、主色 #0017c1、枠の地 #e8f1fe、効く #197a4b、一部効く #c74700、範囲外 #4d4d4d、背景 #ffffff
- 判定は色だけで示さず、アイコンと判定語を添える
- アイコンは Material Symbols Outlined 400
- 内容の判定と事実は仕様書と承認済み文書のとおり。対策や人の承認は書かない
- 新しい依存は足さない（pytest も使わない）

## Review Focus

- Noto Sans JP がないパソコンで開く: 文字幅が変わっても枠からはみ出して読めなくなることがない（各ラベルの枠に左右16px以上の余白を取る）
- PowerPointで文字を書き換える: 補正後の文字が通常の漢字で、検索と置換が効く（Task 1 の `test_radicals_are_normalized`）
- 日本語の校正言語: 文字の言語が中国語のままだと字形や校正が変わる（Task 1 の `test_lang_is_japanese`）
- 標準グラフの数値を変える: 埋め込みの表が開き、棒が追従する（Task 2 の `test_chart_has_embedded_workbook`）
- 2回続けてビルドする: 前回の出力が残っていても同じ結果になる（Task 3 の Step 5）

## File Structure

| ファイル | 責務 |
|---|---|
| `deck.md` | スライドの内容 |
| `theme.css` | 見た目。Marpのテーマ名は `dads` |
| `icons/*.svg` | 使うアイコン。色を付けた複製（`名前-blue.svg` など） |
| `charts.json` | 標準グラフの数値と位置 |
| `fix.py` | 補正、グラフ差し込み、検査。コマンドとしても動く |
| `test_fix.py` | `fix.py` のテスト |
| `build.sh` | 変換から検査、PDF作成まで |
| `package.json` | Marp CLI とアイコンの版の固定 |

---

### Task 1: 補正と検査（`fix.py`）

**Files:**
- Create: `fix.py`
- Test: `test_fix.py`

**Interfaces:**
- Produces:
  - `normalize_radicals(text: str) -> str` U+2E80〜U+2FDF の文字だけを NFKC で通常の漢字に直す。全角コロンなど他の文字は変えない
  - `fix_pptx(src: str, dst: str, font: str = "Noto Sans JP") -> None` スライドの文字を `normalize_radicals` に通し、`typeface` をすべて `font` に、`lang` をすべて `ja-JP` にする
  - `check_pptx(path: str) -> list[str]` 違反の説明を返す。空なら合格。対象は `ppt/slides/*.xml` と `ppt/charts/*.xml`
  - `check_source(md: str) -> list[str]` 原稿の違反を返す

- [ ] **Step 1: 失敗するテストを書く**

`test_fix.py` に unittest で次を書く。テスト用のPowerPointは python-pptx でその場で作る（文字「⽅式A」、フォント `NotoSansCJKjp`、大きさ10pt、`lang="zh-CN"`、別の枠に「終わり。」）

```python
def test_radicals_are_normalized(self):
    self.assertEqual(normalize_radicals("⽅式：⾮root"), "方式：非root")

def test_check_reports_each_violation(self):
    v = "\n".join(check_pptx(self.raw))
    for word in ["12pt", "句点", "部首", "フォント"]:
        self.assertIn(word, v)

def test_fix_clears_radicals_and_font(self):
    fix_pptx(self.raw, self.out)
    v = "\n".join(check_pptx(self.out))
    self.assertNotIn("部首", v)
    self.assertNotIn("フォント", v)
    self.assertIn("12pt", v)      # 大きさと句点は原稿側で直すものなので残る
    self.assertIn("句点", v)

def test_lang_is_japanese(self):
    fix_pptx(self.raw, self.out)
    xml = read_slide_xml(self.out, 1)
    self.assertNotIn('lang="zh-CN"', xml)
    self.assertIn('lang="ja-JP"', xml)

def test_source_rules(self):
    md = "# " + "あ" * 33 + "\n\n---\n\n<!-- _class: cover -->\n# " + "い" * 40 + "\n\n文。\n"
    v = "\n".join(check_source(md))
    self.assertIn("32字", v)
    self.assertEqual(v.count("32字"), 1)   # cover は対象外
    self.assertIn("句点", v)
```

- [ ] **Step 2: 失敗を確かめる**

Run: `python3 -m unittest test_fix -v`
Expected: `ModuleNotFoundError: No module named 'fix'`

- [ ] **Step 3: `fix.py` に4つの関数を実装する**

PowerPointはzipなので、`zipfile` で読み、XMLを文字列のまま正規表現で書き換えて書き戻す。`check_pptx` の基準: `sz` が1200未満、`<a:t>` に「。」、`<a:t>` に U+2E80〜U+2FDF、`typeface` が `Noto Sans JP` 以外。`check_source` の基準: 「。」がある、`# ` で始まる行が32字を超える（その行のスライドに `_class: cover` か `_class: source` があれば対象外）

- [ ] **Step 4: 合格を確かめる**

Run: `python3 -m unittest test_fix -v`
Expected: `OK`（5件）

- [ ] **Step 5: Commit**

```bash
git add fix.py test_fix.py
git commit -m "feat: add pptx fix and checks"
```

### Task 2: 標準グラフの差し込み

**Files:**
- Modify: `fix.py`
- Modify: `test_fix.py`
- Create: `charts.json`

**Interfaces:**
- Consumes: `check_pptx`（Task 1）
- Produces:
  - `insert_charts(path: str, charts: list[dict]) -> None` 各要素は `{"slide": int, "x": int, "y": int, "w": int, "h": int, "categories": [str], "values": [number], "colors": [str]}`。`slide` は1始まり、位置と大きさは1280×720のpx、`colors` は項目ごとの16進色
  - コマンド: `python3 fix.py <変換直後.pptx> <出力.pptx> <charts.json> <deck.md>` 補正、差し込み、検査の順に行い、違反があれば内容を出して終了コード1

- [ ] **Step 1: 失敗するテストを書く**

```python
def test_chart_has_embedded_workbook(self):
    fix_pptx(self.raw, self.out)
    insert_charts(self.out, [{"slide": 1, "x": 700, "y": 300, "w": 500, "h": 300,
        "categories": ["効く", "一部効く", "範囲外"], "values": [1, 5, 4],
        "colors": ["#197a4b", "#c74700", "#4d4d4d"]}])
    names = zipfile.ZipFile(self.out).namelist()
    self.assertTrue(any(n.startswith("ppt/charts/chart") for n in names))
    self.assertTrue(any(n.startswith("ppt/embeddings/") for n in names))

def test_chart_text_passes_checks(self):
    # 上と同じ差し込みの後
    v = "\n".join(check_pptx(self.out))
    self.assertNotIn("chart", v)   # グラフ由来の12pt未満やフォント違反がない
```

- [ ] **Step 2: 失敗を確かめる**

Run: `python3 -m unittest test_fix -v`
Expected: `ImportError`（`insert_charts` がない）

- [ ] **Step 3: `insert_charts` とコマンド入口を実装する**

python-pptx の `add_chart(XL_CHART_TYPE.BAR_CLUSTERED, ...)` を使う。凡例なし、数値ラベルあり、文字は15pt、フォントは Noto Sans JP、項目ごとに `colors` の色、上から `categories` の順に並ぶよう縦軸を反転する。pxからEMUへは `px * 9525`

- [ ] **Step 4: `charts.json` を書く**

サンプル段階では3枚目の1件だけ。位置はTask 3で枠に合わせて確定する

```json
[{"slide": 2, "x": 64, "y": 300, "w": 480, "h": 300,
  "categories": ["効く", "一部効く", "範囲外"], "values": [1, 5, 4],
  "colors": ["#197a4b", "#c74700", "#4d4d4d"]}]
```

（サンプルのファイルでは3枚目が2ページ目になるので `slide` は2）

- [ ] **Step 5: 合格を確かめる**

Run: `python3 -m unittest test_fix -v`
Expected: `OK`（7件）

- [ ] **Step 6: Commit**

```bash
git add fix.py test_fix.py charts.json
git commit -m "feat: insert native charts"
```

### Task 3: テーマ、ビルド、サンプル5枚

**Files:**
- Create: `package.json`, `theme.css`, `build.sh`, `deck.md`, `icons/*.svg`
- Modify: `charts.json`

**Interfaces:**
- Consumes: `fix.py` のコマンド（Task 2）
- Produces:
  - `./build.sh` が `out/deck.pptx` と `out/deck.pdf` と `out/page-NN.png` を作る。違反があれば終了コード1
  - CSSのクラス: `section.cover`、`section.source`、`.ev`（根拠を並べる枠）、`.card`（根拠1つ）、`.slot`（グラフ用の空枠）、`.flow`（図解の横並び）、`.node`（アイコンと名前）、`.arrow`、`.ok` `.part` `.out`（判定の色）
  - 章の名前とページ番号は Marp の `footer` と `paginate` で出す

- [ ] **Step 1: 依存を固定して入れる**

`package.json` に `@marp-team/marp-cli` 4.5.1 と `@material-symbols/svg-400` 0.47.6 を書き、`npm install`
Expected: `node_modules/.bin/marp` がある

- [ ] **Step 2: アイコンを用意する**

`icons/` に使うものだけを複製し、`<svg` に `fill` を足して色を付ける。名前は `<アイコン名>-<blue|ink|ok|part|out>.svg`。判定は `check_circle`（効く）、`radio_button_partial`（一部効く）、`do_not_disturb_on`（範囲外）、矢印は `arrow_forward` と `arrow_downward`

- [ ] **Step 3: `theme.css` を書く**

`/* @theme dads */`。値は Global Constraints のとおり。`section` は 1280×720、余白は上下48px・左右64px、上寄せ。`h1` はメインメッセージで下に主色の線。`h2` は根拠のメッセージ。表は罫線を細いグレー（#e6e6e6）にする

- [ ] **Step 4: `build.sh` を書く**

順に: `out/` を空にする → `marp --pptx --pptx-editable` で `out/raw.pptx` → `python3 fix.py out/raw.pptx out/deck.pptx charts.json deck.md` → `soffice --headless --convert-to pdf` で `out/deck.pdf` → `pdftoppm -r 80 -png` で `out/page-NN.png`。`set -euo pipefail`、`CHROME_PATH` と `CHROME_NO_SANDBOX=1` を設定

- [ ] **Step 5: `deck.md` にサンプル5枚（2〜6枚目）を書く**

メインメッセージと根拠のメッセージは仕様書6節の表のとおり。各スライドの図は次のとおり

| # | 図 |
|---|---|
| 2 | 横の流れ4段: 結論 → 防御 → 判定 → 穴。各段にアイコンと、その章の要点を数字で（「10項目」「4つ」「1・5・4」「9件」） |
| 3 | 左に `.slot`（標準グラフ）、右に10項目の表（項目番号、名前、判定アイコンと判定語） |
| 4 | ホスト、コンテナ、外部の3領域を横に並べ、境界に4つの防御の名前を置く |
| 5 | 左: コンテナから2本の矢印。1本は「許可先 8種類」へ、1本は遮断の印で止まる。右: 起動 → 確認 → 開始または中止 |
| 6 | 左: 一般ユーザーはコンテナ内だけ、管理者の領域には遮断の印。右: 管理者権限から出る矢印は「ファイアウォール初期化」だけに届く |

- [ ] **Step 6: ビルドして検査を通す**

Run: `./build.sh && ./build.sh`
Expected: 2回とも終了コード0、`out/deck.pptx` と `out/deck.pdf` があり、`pdfinfo out/deck.pdf` が `Pages: 5`

違反が出たら原稿かテーマを直す。16pxが1200未満で出る場合は、最小の大きさを1段上げる

- [ ] **Step 7: 目で確認する**

`out/page-01.png`〜`page-05.png` を開き、次を確かめる: 文字の重なりやはみ出しがない、標準グラフが `.slot` の枠に収まっている（ずれていれば `charts.json` を直して再ビルド）、メインメッセージが1行、前後のスライドで単語がつながっている

- [ ] **Step 8: Commit**

```bash
git add package.json package-lock.json theme.css build.sh deck.md icons charts.json .gitignore
git commit -m "feat: add theme, build and five sample slides"
```

`.gitignore` には `node_modules/` と `out/` を書く

- [ ] **Step 9: 利用者の確認を受ける（ここで止まる）**

`out/deck.pptx` と `out/deck.pdf` を渡し、型、見た目、文言、つながりの確認を受ける。指摘は直して再ビルドし、承認が出るまでTask 4に進まない

### Task 4: 残りの10枚

**Files:**
- Modify: `deck.md`, `charts.json`, `icons/`

**Interfaces:**
- Consumes: Task 3 のクラスと `build.sh`、利用者の指摘で変わった決まり

- [ ] **Step 1: 7〜14枚目の根拠のメッセージを書き、利用者に見せる**

サンプルで確定した決まりに従って文言を書き、表で提示して確認を受ける

- [ ] **Step 2: 1枚目と7〜15枚目を `deck.md` に足す**

図は仕様書6節の「根拠の見せ方」のとおり。1枚目は `_class: cover`、15枚目は `_class: source`

- [ ] **Step 3: `charts.json` を全15枚用に直す**

3枚目のグラフの `slide` を3にし、13枚目のグラフ（持ち出し経路 4、設定 3、ホスト側への波及 1、監視 1、色はすべて主色）を足す

- [ ] **Step 4: ビルドして検査を通す**

Run: `./build.sh`
Expected: 終了コード0、`pdfinfo out/deck.pdf` が `Pages: 15`

- [ ] **Step 5: 全ページを目で確認し、仕様書と1行ずつ照合する**

Task 3 Step 7 の観点に加え、10項目の判定と9件の穴が仕様書と一致していること、対策や人の承認を書いていないことを確かめる

- [ ] **Step 6: Commit して成果物を渡す**

```bash
git add deck.md charts.json icons
git commit -m "feat: complete all fifteen slides"
```

---

## 改訂（サンプル確認後、2026-10-04）

仕様書9節の改訂に合わせて、Task 3 をやり直した。変更点は次のとおり

- `fix.py`: `check_source` の対象を `## ` に変更。`pdf_font_problems(pdffonts_output: str) -> list[str]` と `python3 fix.py --pdf <file>` を追加（テスト: `test_pdf_fonts_must_be_noto_sans_jp`、`test_source_rules`）
- `build.sh`: Noto Sans JP がなければ `@expo-google-fonts/noto-sans-jp` 0.4.3 から入れる。PDF作成後にフォント検査を行う
- `theme.css`: `h1` タイトル、`h2` メインメッセージ、`h3` 根拠。部品に `.pill` `.box` `.grid2` `.note` `.roomy`、3枚目用に `.glance` `.zone` `.n` `.badge` を追加
- `charts.json`: サンプルではグラフなし（`[]`）
- Task 4 Step 3 は、13枚目の標準グラフの要否を利用者に確認してから行う
