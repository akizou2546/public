---
marp: true
theme: dads
size: 16:9
paginate: true
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Claude CodeのDev Containerで<br>低減できるリスク

<div class="who">（氏名）</div>
<div class="who">2026年10月4日</div>

---

<!-- header: 結論 ／ 管理策 ／ 有効性 ／ ぜい弱性 ／ リスク対応 -->

# この資料の目的

## Dev Containerが10のリスクをどこまで低減するかを確かめる

<div class="ev">
<div class="card">
<h3>10のリスクはOWASPがまとめたものである<sup>1</sup></h3>
<div class="fig"><div class="flow" style="gap:0">
<div class="node desc"><img src="icons/fact_check-blue.svg"><b>OWASP</b><span>ソフトウェアの安全に<br>取り組む非営利団体</span><span>AIエージェントの<br>10大リスク（2026年版）</span></div>
<div class="link stub"></div>
<div class="branches">
<div class="br"><div class="link"></div><div class="pill">ASI01 目標の乗っ取り</div></div>
<div class="br"><div class="link"></div><div class="pill">ASI02 ツールの悪用</div></div>
<div class="br"><div class="link"></div><div class="pill">ASI03 身元と権限の悪用</div></div>
<div class="br"><div class="link"></div><div class="pill">ほか7つ（ASI04〜ASI10）</div></div>
</div>
</div></div>
</div>
<div class="card">
<h3>Dev Containerは4つの管理策を備える<sup>2</sup></h3>
<div class="fig"><div class="flow" style="gap:0">
<div class="node desc"><img src="icons/deployed_code-blue.svg"><b>Claude Codeの<br>Dev Container</b><span>Anthropicが公開する<br>開発用コンテナの設定例</span><span>3つの設定ファイルを読む</span><span>実機では検証していない</span></div>
<div class="link stub"></div>
<div class="branches">
<div class="br"><div class="link"></div><div class="pill"><img src="icons/shield-blue.svg">通信の許可リスト</div></div>
<div class="br"><div class="link"></div><div class="pill"><img src="icons/shield-blue.svg">非root実行</div></div>
<div class="br"><div class="link"></div><div class="pill"><img src="icons/shield-blue.svg">ファイルの隔離</div></div>
<div class="br"><div class="link"></div><div class="pill"><img src="icons/shield-blue.svg">起動時の検証</div></div>
</div>
</div></div>
</div>
</div>

---

# まとめ

## 10のリスクは、4つの管理策に追加のリスク対応を重ねれば低減できる

<div class="ev"><div class="card">
<div class="fig"><div class="col mid" style="gap:0;align-items:flex-start">
<div class="pt"><div class="pill tag"><img src="icons/fact_check-blue.svg"><b>結論</b></div><div class="link plain"></div><div class="ptx"><h3>4つの管理策は6つのリスクを低減するが、起こりやすさは変えない</h3><div class="subs"><span class="sub">リスクと管理策の対応</span></div></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/shield-blue.svg"><b>管理策</b></div><div class="link plain"></div><div class="ptx"><h3>4つの管理策は、ホストとの境界と外部との境界に2つずつ置かれる</h3><div class="subs"><span class="sub">通信の許可リスト</span><span class="sub">非root実行</span><span class="sub">ファイルの隔離</span></div></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/rule-blue.svg"><b>有効性</b></div><div class="link plain"></div><div class="ptx"><h3>境界だけでリスクを低減できるのは6つで、4つは低減できない</h3><div class="subs"><span class="sub">低減できる6つのリスク</span><span class="sub">低減できない4つのリスク</span><span class="sub">公式の警告</span></div></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/lock_open-blue.svg"><b>ぜい弱性</b></div><div class="link plain"></div><div class="ptx"><h3>持ち出しの経路など10のぜい弱性が、管理策そのものにも残る</h3><div class="subs"><span class="sub">持ち出しの経路</span></div></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/handshake-blue.svg"><b>リスク対応</b></div><div class="link plain"></div><div class="ptx"><h3>持ち出しの経路が残っても、構成を変えれば残留リスクは低減できる</h3></div></div>
</div></div>
</div></div>

---

<!-- header: '**結論** ／ 管理策 ／ 有効性 ／ ぜい弱性 ／ リスク対応' -->

# 10のリスクと管理策の有効性

## 4つの管理策は6つのリスクを低減するが、起こりやすさは変えない

<div class="ev"><div class="card" style="padding-left:10px;padding-right:10px">
<h3>低減できないリスクは入力と処理の側に集まる</h3>
<div class="fig" style="gap:8px">
<div class="glance">
<div class="zone" style="left:0;width:160px">入力</div>
<div class="zone" style="left:250px;width:320px">処理</div>
<div class="zone" style="left:610px;width:170px">出力</div>

<div class="n" style="left:12px;top:44px;width:136px"><img src="icons/record_voice_over-blue.svg">利用者の指示</div>
<div class="n" style="left:12px;top:166px;width:136px"><img src="icons/api-blue.svg">API</div>
<div class="n" style="left:12px;top:280px;width:136px"><img src="icons/smart_toy-blue.svg">外部エージェント</div>

<div class="link" style="left:160px;top:75px;width:90px"></div>
<div class="badge b-out" style="left:164px;top:98px"><img src="icons/do_not_disturb_on-white.svg">ASI01</div>
<div class="badge b-ok" style="left:164px;top:127px"><img src="icons/check_circle-white.svg">ASI03</div>
<div class="badge b-out" style="left:164px;top:156px"><img src="icons/do_not_disturb_on-white.svg">ASI09</div>
<div class="link" style="left:160px;top:197px;width:90px"></div>

<div class="n" style="left:262px;top:44px;width:128px"><img src="icons/policy-blue.svg">方針と統制</div>
<div class="n" style="left:430px;top:44px;width:128px"><img src="icons/support_agent-blue.svg">人の確認</div>
<div class="link both" style="left:390px;top:75px;width:40px"></div>
<div class="link v both" style="left:325px;top:108px;height:42px"></div>
<div class="link v both" style="left:493px;top:108px;height:42px"></div>

<div class="inner" style="left:270px;top:150px;width:280px;height:100px"></div>
<div class="n" style="left:282px;top:160px;width:106px"><img src="icons/smart_toy-blue.svg">エージェント</div>
<div class="link both" style="left:388px;top:191px;width:44px"></div>
<div class="n rogue" style="left:432px;top:160px;width:106px"><img src="icons/smart_toy-blue.svg">エージェント</div>
<div class="badge b-ok" style="left:478px;top:138px"><img src="icons/check_circle-white.svg">ASI10</div>
<div class="badge b-out" style="left:367px;top:218px"><img src="icons/do_not_disturb_on-white.svg">ASI07</div>

<div class="link v both" style="left:493px;top:250px;height:30px"></div>
<div class="n" style="left:262px;top:280px;width:128px"><img src="icons/menu_book-blue.svg">接続データ</div>
<div class="link both" style="left:390px;top:311px;width:40px"></div>
<div class="n" style="left:430px;top:280px;width:128px"><img src="icons/database-blue.svg">メモリ</div>
<div class="badge b-out" style="left:322px;top:266px"><img src="icons/do_not_disturb_on-white.svg">ASI06</div>

<div class="link" style="left:570px;top:197px;width:40px"></div>
<div class="link" style="left:570px;top:311px;width:40px"></div>
<div class="n" style="left:622px;top:44px;width:146px"><img src="icons/dns-blue.svg">API・リソース</div>
<div class="link v up" style="left:694px;top:108px;height:58px"></div>
<div class="n" style="left:622px;top:166px;width:146px"><img src="icons/construction-blue.svg">ツール</div>
<div class="badge b-ok" style="left:690px;top:218px"><img src="icons/check_circle-white.svg">ASI02</div>
<div class="n" style="left:622px;top:280px;width:146px"><img src="icons/smart_toy-blue.svg">外部エージェント</div>

<div class="rule"></div>
<div class="badge b-ok" style="left:249px;top:356px"><img src="icons/check_circle-white.svg">ASI04</div>
<div class="badge b-ok" style="left:349px;top:356px"><img src="icons/check_circle-white.svg">ASI05</div>
<div class="badge b-ok" style="left:449px;top:356px"><img src="icons/check_circle-white.svg">ASI08</div>
</div>
<table class="mini">
<tr><td>ASI01</td><td>目標の乗っ取り</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI02</td><td>ツールの悪用</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI03</td><td>身元と権限の悪用</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI04</td><td>供給網のぜい弱性</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI05</td><td>想定外のコード実行</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI06</td><td>記憶と文脈の汚染</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI07</td><td>安全でない<br>エージェント間通信</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI08</td><td>連鎖的な障害</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI09</td><td>人の信頼の悪用</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI10</td><td>暴走エージェント</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
</table>
</div>
</div></div>

---

# リスクと管理策の対応

## 6つのリスクには4つの管理策のどれかが効き、4つには効かない

<div class="ev"><div class="card" style="padding-left:10px;padding-right:10px">
<h3>管理策が効く6つも、残留リスクが大きい構成では低減しきれない</h3>
<div class="fig">
<table class="matrix" style="width:1132px">
<tr><th style="width:296px">リスク</th><th style="width:192px">どんなリスクか</th><th class="c" style="width:88px">通信の<br>許可リスト</th><th class="c" style="width:64px">非root<br>実行</th><th class="c" style="width:88px">ファイルの<br>隔離</th><th class="c" style="width:76px">起動時の<br>検証</th><th style="width:200px">残留リスクが大きい構成</th><th style="width:128px">有効性</th></tr>
<tr><td>ASI01 目標の乗っ取り</td><td>指示で目的が書き換わる</td><td class="c"></td><td class="c"></td><td class="c"></td><td class="c"></td><td>他人の文書を読む</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI02 ツールの悪用</td><td>ツールが危険に使われる</td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td>秘密や大事なデータを置く</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI03 身元と権限の悪用</td><td>権限が範囲外で使われる</td><td class="c"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"></td><td>認証を引き継ぐ</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI04 供給網のぜい弱性</td><td>取り込む部品が改ざん済み</td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"></td><td class="c"></td><td class="c"><img src="icons/check-blue.svg"></td><td>外部の部品を取り込む</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI05 想定外のコード実行</td><td>意図しない命令が動く</td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td>成果物をホストで動かす</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI06 記憶と文脈の汚染</td><td>記憶に悪い情報が残る</td><td class="c"></td><td class="c"></td><td class="c"></td><td class="c"></td><td>履歴を引き継ぐ</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI07 安全でないエージェント間通信</td><td>通信の相手が偽装される</td><td class="c"></td><td class="c"></td><td class="c"></td><td class="c"></td><td>複数を連携させる</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI08 連鎖的な障害</td><td>1つの誤りが他へ広がる</td><td class="c"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"></td><td>自動で後工程に流す</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
<tr><td>ASI09 人の信頼の悪用</td><td>人が出力を信じすぎる</td><td class="c"></td><td class="c"></td><td class="c"></td><td class="c"></td><td>確かめずに承認する</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td></tr>
<tr><td>ASI10 暴走エージェント</td><td>役割から外れて動く</td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td class="c"><img src="icons/check-blue.svg"></td><td>無人で動かす</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td></tr>
</table>
</div>
</div></div>

---

<!-- header: '結論 ／ **管理策** ／ 有効性 ／ ぜい弱性 ／ リスク対応' -->

# 4つの管理策の配置

## 4つの管理策は、ホストとの境界と外部との境界に2つずつ置かれる

<div class="ev"><div class="card">
<h3>管理策は3つの領域の境界で働く</h3>
<div class="fig"><div class="flow" style="gap:0">
<div class="node big" style="min-width:0;padding:16px 12px"><img src="icons/computer-blue.svg"><b>ホスト</b></div>
<div class="link back" style="width:24px"></div>
<div class="branches both">
<div class="br" style="padding:44px 0"><div class="link plain" style="width:24px"></div><div class="pill two"><img src="icons/shield-blue.svg"><div><b>ファイルの隔離</b><span>作業フォルダだけ見える</span></div></div><div class="link back" style="width:24px"></div></div>
<div class="br" style="padding:44px 0"><div class="link plain" style="width:24px"></div><div class="pill two"><img src="icons/shield-blue.svg"><div><b>非root実行</b><span>一般ユーザーで動く</span></div></div><div class="link back" style="width:24px"></div></div>
</div>
<div class="link stub"></div>
<div class="node big" style="min-width:0;padding:16px 12px"><img src="icons/deployed_code-blue.svg"><b>コンテナ</b></div>
<div class="link stub"></div>
<div class="branches both">
<div class="br" style="padding:44px 0"><div class="link" style="width:24px"></div><div class="pill two"><img src="icons/shield-blue.svg"><div><b>通信の許可リスト</b><span>8種類の宛先だけ通す</span></div></div><div class="link plain" style="width:24px"></div></div>
<div class="br" style="padding:44px 0"><div class="link" style="width:24px"></div><div class="pill two"><img src="icons/shield-blue.svg"><div><b>起動時の検証</b><span>遮断を確かめて開始</span></div></div><div class="link plain" style="width:24px"></div></div>
</div>
<div class="link" style="width:24px"></div>
<div class="node big" style="min-width:0;padding:16px 12px"><img src="icons/public-blue.svg"><b>外部</b></div>
</div></div>
</div></div>

---

# 通信の許可リスト

## 外部との境界では、通信を許可リストにある宛先だけに絞る

<div class="ev">
<div class="card">
<h3>外向きの通信は既定ですべて遮断される</h3>
<div class="fig"><div class="flow" style="gap:0">
<div class="node"><img src="icons/deployed_code-blue.svg"><b>コンテナ</b></div>
<div class="link stub"></div>
<div class="branches">
<div class="br" style="padding:16px 0"><div class="link"></div>
<div class="box">
<div class="head"><img src="icons/check_circle-ok.svg">許可先 8種類</div>
<div class="grid2">
<div>GitHub</div><div>npm</div>
<div>Anthropic API</div><div>Sentry</div>
<div>Statsig</div><div>VS Code 拡張</div>
<div>VS Code 配布</div><div>VS Code 更新</div>
</div>
</div>
</div>
<div class="br" style="padding:16px 0"><div class="link cut"><img src="icons/block-ink.svg"></div><div class="pill mute"><img src="icons/public-blue.svg">その他の宛先</div></div>
</div>
</div></div>
</div>
<div class="card">
<h3>遮断は起動時に確かめられる</h3>
<div class="fig"><div class="col mid" style="gap:0">
<div class="pill"><img src="icons/power_settings_new-blue.svg"><b>起動</b></div>
<div class="link v"></div>
<div class="box" style="border-color:#0017c1">
<div class="head"><img src="icons/search-blue.svg">確認</div>
<div>example.com に届かない</div>
<div>api.github.com に届く</div>
</div>
<div class="flow top" style="gap:56px">
<div class="col mid" style="gap:0">
<div class="link v lab"><span class="l">両方を満たす</span></div>
<div class="pill good"><img src="icons/play_arrow-ok.svg"><b>開始</b></div>
</div>
<div class="col mid" style="gap:0">
<div class="link v lab"><span>どちらか外れる</span></div>
<div class="pill mute"><img src="icons/block-ink.svg"><b>中止</b></div>
</div>
</div>
</div></div>
</div>
</div>

---

# 非root実行

## 許可リストは、一般ユーザーで動かすので書き換えられない

<div class="ev">
<div class="card">
<h3>実行は一般ユーザーに限られる</h3>
<div class="fig roomy"><div class="flow" style="gap:0">
<div class="node"><img src="icons/person-blue.svg"><b>一般ユーザー</b><span>node</span></div>
<div class="link stub"></div>
<div class="branches">
<div class="br"><div class="link" style="width:72px"></div><div class="pill good"><img src="icons/terminal-blue.svg">コマンド実行</div></div>
<div class="br"><div class="link" style="width:72px"></div><div class="pill good"><img src="icons/deployed_code-blue.svg">作業フォルダの編集</div></div>
<div class="br"><div class="link cut"><img src="icons/block-ink.svg"></div><div class="pill mute"><img src="icons/shield-blue.svg">許可リストの変更</div></div>
<div class="br"><div class="link cut"><img src="icons/block-ink.svg"></div><div class="pill mute"><img src="icons/settings-blue.svg">システム領域の変更</div></div>
</div>
</div></div>
</div>
<div class="card">
<h3>管理者権限は初期化にしか使えない</h3>
<div class="fig roomy"><div class="flow" style="gap:0">
<div class="node"><img src="icons/admin_panel_settings-blue.svg"><b>管理者権限</b><span>sudo</span></div>
<div class="link stub"></div>
<div class="branches">
<div class="br"><div class="link" style="width:72px"></div>
<div class="box">
<div class="head"><img src="icons/check_circle-ok.svg">init-firewall.sh</div>
<div>許可リストの設定</div>
<div>遮断の確認</div>
</div>
</div>
<div class="br"><div class="link cut"><img src="icons/block-ink.svg"></div><div class="pill mute"><img src="icons/terminal-blue.svg">それ以外のコマンド</div></div>
</div>
</div></div>
</div>
</div>

---

# ファイルの隔離

## 一般ユーザーには、ホストとの境界で作業フォルダだけを見せる

<div class="ev">
<div class="card">
<h3>ホストから渡すのは作業フォルダだけである</h3>
<div class="fig roomy"><div class="flow" style="gap:0">
<div class="node"><img src="icons/deployed_code-blue.svg"><b>コンテナ</b></div>
<div class="link stub"></div>
<div class="branches">
<div class="br"><div class="link" style="width:72px"></div><div class="pill good"><img src="icons/folder-blue.svg">作業フォルダ</div></div>
<div class="br"><div class="link cut"><img src="icons/block-ink.svg"></div><div class="pill mute"><img src="icons/key-blue.svg">SSHの鍵のファイル</div></div>
<div class="br"><div class="link cut"><img src="icons/block-ink.svg"></div><div class="pill mute"><img src="icons/cloud-blue.svg">クラウドの認証情報</div></div>
<div class="br"><div class="link cut"><img src="icons/block-ink.svg"></div><div class="pill mute"><img src="icons/description-blue.svg">その他のファイル</div></div>
</div>
</div></div>
</div>
<div class="card">
<h3>鍵は見えないがホストの認証は使える<sup>3</sup></h3>
<div class="fig"><div class="col mid" style="gap:0">
<div class="pill"><img src="icons/key-blue.svg">ホストのGit認証とSSHエージェント</div>
<div class="link v lab"><span>VS Code が引き継ぐ</span></div>
<div class="node"><img src="icons/deployed_code-blue.svg"><b>コンテナ</b></div>
<div class="link v"></div>
<div class="pill"><img src="icons/terminal-blue.svg">ホストの認証でGitを操作できる</div>
</div></div>
</div>
</div>

---

<!-- header: '結論 ／ 管理策 ／ **有効性** ／ ぜい弱性 ／ リスク対応' -->

# 有効性の内訳

## 境界だけでリスクを低減できるのは6つで、4つは低減できない

<div class="ev"><div class="card">
<h3>どのリスクにも残留リスクが大きい構成が1つずつある</h3>
<div class="fig"><div class="flow top verdicts" style="gap:24px">
<div class="col fill" style="gap:8px">
<div class="pill" style="justify-content:center"><img src="icons/check_circle-ok.svg"><b>低減できる</b>6つ</div>
<div class="flow top" style="gap:12px">
<div class="col fill" style="gap:8px">
<div class="pill two" style="padding:2px 16px 2px 10px"><img src="icons/check_circle-ok.svg"><div><b>ASI02 ツールの悪用</b><span>秘密や大事なデータを置く</span></div></div>
<div class="pill two" style="padding:2px 16px 2px 10px"><img src="icons/check_circle-ok.svg"><div><b>ASI03 身元と権限の悪用</b><span>認証を引き継ぐ</span></div></div>
<div class="pill two" style="padding:2px 16px 2px 10px"><img src="icons/check_circle-ok.svg"><div><b>ASI04 供給網のぜい弱性</b><span>外部の部品を取り込む</span></div></div>
</div>
<div class="col fill" style="gap:8px">
<div class="pill two" style="padding:2px 16px 2px 10px"><img src="icons/check_circle-ok.svg"><div><b>ASI05 想定外のコード実行</b><span>成果物をホストで動かす</span></div></div>
<div class="pill two" style="padding:2px 16px 2px 10px"><img src="icons/check_circle-ok.svg"><div><b>ASI08 連鎖的な障害</b><span>自動で後工程に流す</span></div></div>
<div class="pill two" style="padding:2px 16px 2px 10px"><img src="icons/check_circle-ok.svg"><div><b>ASI10 暴走エージェント</b><span>無人で動かす</span></div></div>
</div>
</div>
</div>
<div class="col fill" style="gap:8px">
<div class="pill" style="justify-content:center"><img src="icons/do_not_disturb_on-out.svg"><b>低減できない</b>4つ</div>
<div class="pill two mute" style="padding:2px 16px 2px 10px"><img src="icons/do_not_disturb_on-out.svg"><div><b>ASI01 目標の乗っ取り</b><span>他人の文書を読む</span></div></div>
<div class="pill two mute" style="padding:2px 16px 2px 10px"><img src="icons/do_not_disturb_on-out.svg"><div><b>ASI06 記憶と文脈の汚染</b><span>履歴を引き継ぐ</span></div></div>
<div class="pill two mute" style="padding:2px 16px 2px 10px"><img src="icons/do_not_disturb_on-out.svg"><div><b>ASI07 安全でないエージェント間通信</b><span>複数を連携させる</span></div></div>
<div class="pill two mute" style="padding:2px 16px 2px 10px"><img src="icons/do_not_disturb_on-out.svg"><div><b>ASI09 人の信頼の悪用</b><span>確かめずに承認する</span></div></div>
</div>
</div></div>
</div></div>

---


# 低減できる6つのリスク

## 低減できる6つも、コンテナの中にあるものは守れない

<div class="ev"><div class="card">
<h3>6つのうち2つは、VS Codeでそのまま使うと当てはまる</h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1068px">
<tr><th style="width:380px">リスク</th><th style="width:276px">管理策の働き</th><th style="width:262px">残留リスクが大きい構成</th><th style="width:150px">そのまま使うと</th></tr>
<tr><td><img src="icons/check_circle-ok.svg">ASI02 ツールの悪用</td><td>ホストと許可外には届かない</td><td>秘密や大事なデータを置く</td><td>当てはまらない</td></tr>
<tr><td><img src="icons/check_circle-ok.svg">ASI03 身元と権限の悪用</td><td>鍵のファイルは見えない</td><td>認証を引き継ぐ</td><td>当てはまる</td></tr>
<tr><td><img src="icons/check_circle-ok.svg">ASI04 供給網のぜい弱性</td><td>通信先は許可先だけ</td><td>外部の部品を取り込む</td><td>当てはまる</td></tr>
<tr><td><img src="icons/check_circle-ok.svg">ASI05 想定外のコード実行</td><td>実行はコンテナ内に留まる</td><td>成果物をホストで動かす</td><td>当てはまらない</td></tr>
<tr><td><img src="icons/check_circle-ok.svg">ASI08 連鎖的な障害</td><td>コンテナ内に留まる</td><td>自動で後工程に流す</td><td>当てはまらない</td></tr>
<tr><td><img src="icons/check_circle-ok.svg">ASI10 暴走エージェント</td><td>行動範囲を封じ込める</td><td>無人で動かす</td><td>当てはまらない</td></tr>
</table>
</div>
</div></div>

---

# 低減できない4つのリスク

## コンテナで囲っても、判断と過信に関わる4つは低減できない

<div class="ev"><div class="card">
<h3>4つとも隔離では止められず、1つだけが当てはまらない</h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1068px">
<tr><th style="width:380px">リスク</th><th style="width:276px">管理策の働き</th><th style="width:262px">残留リスクが大きい構成</th><th style="width:150px">そのまま使うと</th></tr>
<tr><td><img src="icons/do_not_disturb_on-out.svg">ASI01 目標の乗っ取り</td><td>読む内容を検査しない</td><td>他人の文書を読む</td><td>当てはまる</td></tr>
<tr><td><img src="icons/do_not_disturb_on-out.svg">ASI06 記憶と文脈の汚染</td><td>保存内容を検査しない</td><td>履歴を引き継ぐ</td><td>当てはまる</td></tr>
<tr><td><img src="icons/do_not_disturb_on-out.svg">ASI07 安全でないエージェント間通信</td><td>通信を守る仕組みがない</td><td>複数を連携させる</td><td>当てはまらない</td></tr>
<tr><td><img src="icons/do_not_disturb_on-out.svg">ASI09 人の信頼の悪用</td><td>人の判断に関与しない</td><td>確かめずに承認する</td><td>当てはまる</td></tr>
</table>
</div>
</div></div>

---

# 公式の警告

## 過信せず認証情報の持ち出しに備えるよう、公式も警告している

<div class="ev">
<div class="card">
<h3>許可確認を省くと持ち出しは防げない<sup>4</sup></h3>
<div class="fig"><div class="col mid" style="gap:0">
<div class="pill mute"><img src="icons/warning-blue.svg">悪意あるプロジェクト</div>
<div class="link v lab"><span>許可確認なしで実行</span></div>
<div class="node"><img src="icons/deployed_code-blue.svg"><b>コンテナ</b><span>Claude Code の認証情報がある</span></div>
<div class="link v lab"><span>持ち出し</span></div>
<div class="pill mute"><img src="icons/public-blue.svg">外部</div>
</div></div>
</div>
<div class="card">
<h3>公式は使い方に3つの条件を付けている</h3>
<div class="fig"><div class="col fill" style="gap:20px">
<div class="pill" style="padding:16px 24px 16px 16px"><img src="icons/verified_user-blue.svg">信頼できるリポジトリで使う</div>
<div class="pill" style="padding:16px 24px 16px 16px"><img src="icons/visibility-blue.svg">Claude の動作を監視する</div>
<div class="pill" style="padding:16px 24px 16px 16px"><img src="icons/key-blue.svg">ホストの秘密を持ち込まない</div>
</div></div>
</div>
</div>

---

<!-- header: '結論 ／ 管理策 ／ 有効性 ／ **ぜい弱性** ／ リスク対応' -->

# 管理策に残る10のぜい弱性

## 持ち出しの経路など10のぜい弱性が、管理策そのものにも残る

<div class="ev"><div class="card">
<h3>ぜい弱性は持ち出し、設定、波及、監視の4種類に分かれる</h3>
<div class="fig"><div class="flow top" style="gap:16px">
<div class="col fill">
<div class="node"><img src="icons/public-blue.svg"><b>持ち出しの経路</b><span>4つ</span></div>
<div class="pill">DNSの宛先が無制限</div>
<div class="pill">SSHの宛先が無制限</div>
<div class="pill">許可先への送信</div>
<div class="pill">ホスト側ネットワーク</div>
</div>
<div class="col fill">
<div class="node"><img src="icons/settings-blue.svg"><b>設定</b><span>3つ</span></div>
<div class="pill">許可IPが起動時に固定</div>
<div class="pill">IPv6の規則がない</div>
<div class="pill">版が固定されていない</div>
</div>
<div class="col fill">
<div class="node"><img src="icons/computer-blue.svg"><b>ホスト側への波及</b><span>2つ</span></div>
<div class="pill">作業フォルダ経由の実行</div>
<div class="pill">ホストの認証の引き継ぎ</div>
</div>
<div class="col fill">
<div class="node"><img src="icons/visibility_off-blue.svg"><b>監視</b><span>1つ</span></div>
<div class="pill">監視と記録がない</div>
</div>
</div></div>
</div></div>

---

# 持ち出しの経路

## ぜい弱性のうち持ち出しは、許可リストの例外と許可先そのものを通る

<div class="ev">
<div class="card">
<h3>3つの例外は許可リストを通らない</h3>
<div class="fig roomy"><div class="flow" style="gap:0">
<div class="node"><img src="icons/deployed_code-blue.svg"><b>コンテナ</b></div>
<div class="link stub"></div>
<div class="branches">
<div class="br"><div class="link" style="width:72px"></div><div class="pill"><img src="icons/dns-blue.svg">DNS（宛先を問わない）</div></div>
<div class="br"><div class="link" style="width:72px"></div><div class="pill"><img src="icons/terminal-blue.svg">SSH（宛先を問わない）</div></div>
<div class="br"><div class="link" style="width:72px"></div><div class="pill"><img src="icons/computer-blue.svg">ホスト側ネットワーク</div></div>
</div>
</div></div>
</div>
<div class="card">
<h3>許可先へは攻撃者の認証情報で送れる</h3>
<div class="fig"><div class="col mid" style="gap:0">
<div class="node"><img src="icons/deployed_code-blue.svg"><b>コンテナ</b></div>
<div class="link v lab"><span>攻撃者が用意した認証情報</span></div>
<div class="pill good"><img src="icons/check_circle-ok.svg">許可先（GitHub、npm）</div>
<div class="link v"></div>
<div class="pill mute"><img src="icons/person-blue.svg">攻撃者のアカウント</div>
</div></div>
</div>
</div>

---

<!-- header: '結論 ／ 管理策 ／ 有効性 ／ ぜい弱性 ／ **リスク対応**' -->

# 残留リスクへの対応

## 持ち出しの経路が残っても、構成を変えれば残留リスクは低減できる

<div class="ev"><div class="card">
<h3>どのリスクにも、残留リスクを低減する対応が1つずつある</h3>
<div class="fig">
<table class="avoid" style="table-layout:fixed;width:1040px">
<tr><th style="width:340px">リスク</th><th style="width:300px">残留リスクが大きい構成</th><th style="width:400px">リスク対応</th></tr>
<tr><td>ASI01 目標の乗っ取り</td><td><img src="icons/block-ink.svg">他人の文書を読む</td><td><img src="icons/check_circle-ok.svg">信頼できるリポジトリで使う</td></tr>
<tr><td>ASI02 ツールの悪用</td><td><img src="icons/block-ink.svg">秘密や大事なデータを置く</td><td><img src="icons/check_circle-ok.svg">秘密は絞り、データは控えを取る</td></tr>
<tr><td>ASI03 身元と権限の悪用</td><td><img src="icons/block-ink.svg">認証を引き継ぐ</td><td><img src="icons/check_circle-ok.svg">権限と期限を絞った認証だけ渡す</td></tr>
<tr><td>ASI04 供給網のぜい弱性</td><td><img src="icons/block-ink.svg">外部の部品を取り込む</td><td><img src="icons/check_circle-ok.svg">確かめた部品だけ取り込む</td></tr>
<tr><td>ASI05 想定外のコード実行</td><td><img src="icons/block-ink.svg">成果物をホストで動かす</td><td><img src="icons/check_circle-ok.svg">成果物はコンテナの中で動かす</td></tr>
<tr><td>ASI06 記憶と文脈の汚染</td><td><img src="icons/block-ink.svg">履歴を引き継ぐ</td><td><img src="icons/check_circle-ok.svg">履歴を持ち越さない</td></tr>
<tr><td>ASI07 安全でないエージェント間通信</td><td><img src="icons/block-ink.svg">複数を連携させる</td><td><img src="icons/check_circle-ok.svg">連携させない</td></tr>
<tr><td>ASI08 連鎖的な障害</td><td><img src="icons/block-ink.svg">自動で後工程に流す</td><td><img src="icons/check_circle-ok.svg">後工程に流す前に確かめる</td></tr>
<tr><td>ASI09 人の信頼の悪用</td><td><img src="icons/block-ink.svg">確かめずに承認する</td><td><img src="icons/check_circle-ok.svg">確かめてから承認する</td></tr>
<tr><td>ASI10 暴走エージェント</td><td><img src="icons/block-ink.svg">無人で動かす</td><td><img src="icons/check_circle-ok.svg">人が見ている間だけ動かす</td></tr>
</table>
</div>
</div></div>

---

<!-- header: '結論 ／ 管理策 ／ 有効性 ／ ぜい弱性 ／ リスク対応' -->

# まとめ

## 10のリスクは、4つの管理策に追加のリスク対応を重ねれば低減できる

<div class="ev"><div class="card">
<div class="fig"><div class="col mid" style="gap:0;align-items:flex-start">
<div class="pt"><div class="pill tag"><img src="icons/fact_check-blue.svg"><b>結論</b></div><div class="link plain"></div><div class="ptx"><h3>4つの管理策は6つのリスクを低減するが、起こりやすさは変えない</h3></div></div>
<div class="link v" style="margin-left:64px;height:30px"></div>
<div class="pt"><div class="pill tag"><img src="icons/shield-blue.svg"><b>管理策</b></div><div class="link plain"></div><div class="ptx"><h3>4つの管理策は、ホストとの境界と外部との境界に2つずつ置かれる</h3></div></div>
<div class="link v" style="margin-left:64px;height:30px"></div>
<div class="pt"><div class="pill tag"><img src="icons/rule-blue.svg"><b>有効性</b></div><div class="link plain"></div><div class="ptx"><h3>境界だけでリスクを低減できるのは6つで、4つは低減できない</h3></div></div>
<div class="link v" style="margin-left:64px;height:30px"></div>
<div class="pt"><div class="pill tag"><img src="icons/lock_open-blue.svg"><b>ぜい弱性</b></div><div class="link plain"></div><div class="ptx"><h3>持ち出しの経路など10のぜい弱性が、管理策そのものにも残る</h3></div></div>
<div class="link v" style="margin-left:64px;height:30px"></div>
<div class="pt"><div class="pill tag"><img src="icons/handshake-blue.svg"><b>リスク対応</b></div><div class="link plain"></div><div class="ptx"><h3>持ち出しの経路が残っても、構成を変えれば残留リスクは低減できる</h3></div></div>
</div></div>
</div></div>

---

<!-- _class: source -->
<!-- header: '' -->

# 参考文献

<div class="ev"><div class="card">
<div class="fig">
<table class="big refs">
<tr><td>1.</td><td>OWASP Gen AI Security Project - Agentic Security Initiative,<br>"OWASP Top 10 for Agentic Applications for 2026" (2025);<br><a href="https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/">genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/</a><br>10のリスクの図は、この文献の「Agentic Top 10 At A Glance」をもとに作成（CC BY-SA 4.0）</td></tr>
<tr><td>2.</td><td>Anthropic, claude-code: .devcontainer, commit 1c229fc (2026);<br><a href="https://github.com/anthropics/claude-code/tree/main/.devcontainer">github.com/anthropics/claude-code/tree/main/.devcontainer</a></td></tr>
<tr><td>3.</td><td>Microsoft, Sharing Git credentials with your container, Visual Studio Code Docs (2026);<br><a href="https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials">code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials</a></td></tr>
<tr><td>4.</td><td>Anthropic, Development containers, Claude Code Docs (2026);<br><a href="https://code.claude.com/docs/en/devcontainer">code.claude.com/docs/en/devcontainer</a></td></tr>
</table>
</div>
</div></div>
