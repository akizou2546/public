---
marp: true
theme: dads
size: 16:9
paginate: true
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Claude CodeのDev Containerを<br>ISMSで運用する流れ

<div class="who">（氏名）</div>
<div class="who">2026年10月4日</div>

---

<!-- header: 全体 ／ 計画 ／ 運用 ／ 評価 ／ 改善 ／ 承認 -->

# この資料の目的

## Dev Containerの運用を、ISMSの4つの段階に沿って整理する

<div class="ev">
<div class="card">
<h3>前回の資料は10のリスクで管理策を評価した<sup>1</sup></h3>
<div class="fig"><div class="flow" style="gap:0">
<div class="node desc"><img src="icons/deployed_code-blue.svg"><b>Claude Codeの<br>Dev Container</b><span>AIがコードを書く道具を<br>隔離して動かす環境</span><span>実機では検証していない</span></div>
<div class="link stub"></div>
<div class="branches">
<div class="br"><div class="link"></div><div class="pill">4つの管理策を評価</div></div>
<div class="br"><div class="link"></div><div class="pill"><img src="icons/check_circle-ok.svg">6つは低減できる</div></div>
<div class="br"><div class="link"></div><div class="pill"><img src="icons/do_not_disturb_on-out.svg">4つは低減できない</div></div>
<div class="br"><div class="link"></div><div class="pill"><img src="icons/lock_open-blue.svg">10のぜい弱性が残る</div></div>
</div>
</div></div>
</div>
<div class="card">
<h3>ISMSでは3つの承認を得て4つの段階を回す<sup>2</sup></h3>
<div class="fig"><div class="flow" style="gap:0">
<div class="node desc"><img src="icons/verified_user-blue.svg"><b>ISMS</b><span>情報セキュリティを<br>組織で管理する仕組み</span><span>現行の規格の本文とは<br>突き合わせていない</span></div>
<div class="link stub"></div>
<div class="branches">
<div class="br" style="padding:8px 0"><div class="link"></div><div class="pill"><b>承認</b>3つを得て始める</div></div>
<div class="br" style="padding:8px 0"><div class="link"></div><div class="pill"><b>計画</b>リスク対応を決める</div></div>
<div class="br" style="padding:8px 0"><div class="link"></div><div class="pill"><b>運用</b>3つの場面で実行する</div></div>
<div class="br" style="padding:8px 0"><div class="link"></div><div class="pill"><b>評価</b>記録と監査で確かめる</div></div>
<div class="br" style="padding:8px 0"><div class="link"></div><div class="pill"><b>改善</b>見直して計画に戻す</div></div>
</div>
</div></div>
</div>
</div>

---

# まとめ

## Dev Containerは、3つの承認を得てISMSの4つの段階で運用する

<div class="ev"><div class="card">
<div class="fig"><div class="col mid" style="gap:0;align-items:flex-start">
<div class="pt"><div class="pill tag"><img src="icons/map-blue.svg"><b>全体</b></div><div class="link plain"></div><div class="ptx"><h3>4つの段階は、計画、運用、評価、改善の順に回り、承認で始まる</h3><div class="subs"><span class="sub">段階ごとの担当と記録</span></div></div></div>
<div class="link v" style="margin-left:64px;height:18px"></div>
<div class="pt"><div class="pill tag"><img src="icons/edit_note-blue.svg"><b>計画</b></div><div class="link plain"></div><div class="ptx"><h3>計画では、10のリスクごとにリスク対応と担当を決める</h3><div class="subs"><span class="sub">基盤の担当が強制する設定</span><span class="sub">附属書Aとの比較</span><span class="sub">残留リスク</span></div></div></div>
<div class="link v" style="margin-left:64px;height:18px"></div>
<div class="pt"><div class="pill tag"><img src="icons/play_circle-blue.svg"><b>運用</b></div><div class="link plain"></div><div class="ptx"><h3>承認を得たら、利用開始、日々の利用、事故の3つの場面で運用する</h3><div class="subs"><span class="sub">利用開始の流れ</span><span class="sub">日々の利用の決まり</span><span class="sub">事故のときの流れ</span></div></div></div>
<div class="link v" style="margin-left:64px;height:18px"></div>
<div class="pt"><div class="pill tag"><img src="icons/fact_check-blue.svg"><b>評価</b></div><div class="link plain"></div><div class="ptx"><h3>報告と日々の記録は、内部監査で決まりどおりかを評価する</h3><div class="subs"><span class="sub">評価に残る課題</span></div></div></div>
<div class="link v" style="margin-left:64px;height:18px"></div>
<div class="pt"><div class="pill tag"><img src="icons/autorenew-blue.svg"><b>改善</b></div><div class="link plain"></div><div class="ptx"><h3>課題と評価の結果は、マネジメントレビューで見直して計画に戻す</h3></div></div>
<div class="link v" style="margin-left:64px;height:18px"></div>
<div class="pt"><div class="pill tag"><img src="icons/approval-blue.svg"><b>承認</b></div><div class="link plain"></div><div class="ptx"><h3>計画を運用に移すには、3つの承認が要る</h3></div></div>
</div></div>
</div></div>

---

<!-- header: '**全体** ／ 計画 ／ 運用 ／ 評価 ／ 改善 ／ 承認' -->

# 運用フローの全体像

## 4つの段階は、計画、運用、評価、改善の順に回り、承認で始まる

<div class="ev"><div class="card">
<h3>4つの段階は規格の箇条6、8、9、10に当たる</h3>
<div class="fig">
<div class="glance" style="width:1046px;height:320px">
<div class="node desc" style="left:0;top:0;width:150px;height:205px;min-width:0"><img src="icons/approval-blue.svg"><b>承認</b><span>リスク所有者が<br>計画と受容を<br>承認する</span></div>
<div class="link" style="left:150px;top:101px;width:44px"></div>
<div class="node desc" style="left:194px;top:0;width:180px;height:205px"><img src="icons/edit_note-blue.svg"><b>計画</b><span style="margin-bottom:6px">箇条6</span><span>リスクごとに<br>リスク対応を決める</span></div>
<div class="link" style="left:374px;top:101px;width:44px"></div>
<div class="node desc" style="left:418px;top:0;width:180px;height:205px"><img src="icons/play_circle-blue.svg"><b>運用</b><span style="margin-bottom:6px">箇条8</span><span>3つの場面で<br>実行する</span></div>
<div class="link" style="left:598px;top:101px;width:44px"></div>
<div class="node desc" style="left:642px;top:0;width:180px;height:205px"><img src="icons/fact_check-blue.svg"><b>評価</b><span style="margin-bottom:6px">箇条9</span><span>記録と内部監査で<br>確かめる</span></div>
<div class="link" style="left:822px;top:101px;width:44px"></div>
<div class="node desc" style="left:866px;top:0;width:180px;height:205px"><img src="icons/autorenew-blue.svg"><b>改善</b><span style="margin-bottom:6px">箇条10</span><span>結果を見直して<br>計画に戻す</span></div>
<div class="link v plain" style="left:955px;top:205px;height:60px"></div>
<div class="link plain" style="left:284px;top:264px;width:673px"></div>
<div class="link v up" style="left:283px;top:205px;height:60px"></div>
<div style="left:284px;top:275px;width:673px;text-align:center;font-size:20px">見直した結果を次の計画に戻す</div>
</div>
</div>
</div></div>

---

# 段階ごとの担当と記録

## 計画から改善までの段階ごとに、担当と残す記録を決める

<div class="ev"><div class="card">
<h3>4つの段階を5つの役割が担当する</h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1020px">
<tr><th style="width:110px">段階</th><th style="width:280px">やること</th><th style="width:250px">担当</th><th style="width:280px">残す記録</th><th style="width:100px">箇条</th></tr>
<tr><td><img src="icons/edit_note-blue.svg">計画</td><td>リスク対応を決める</td><td>情報セキュリティ責任者</td><td>リスク対応計画、適用宣言書</td><td>6</td></tr>
<tr><td><img src="icons/play_circle-blue.svg">運用</td><td>3つの場面で実行する</td><td>利用者、基盤の担当</td><td>申請、点検、事故の報告</td><td>8</td></tr>
<tr><td><img src="icons/fact_check-blue.svg">評価</td><td>記録と内部監査で確かめる</td><td>内部監査の担当</td><td>内部監査の報告</td><td>9</td></tr>
<tr><td><img src="icons/autorenew-blue.svg">改善</td><td>結果を見直して計画に戻す</td><td>経営層</td><td>マネジメントレビューの記録</td><td>10</td></tr>
</table>
</div>
</div></div>

---

<!-- header: '全体 ／ **計画** ／ 運用 ／ 評価 ／ 改善 ／ 承認' -->

# リスク対応の選択

## 計画では、10のリスクごとにリスク対応と担当を決める

<div class="ev"><div class="card">
<h3>10のうち6つは低減し、4つは回避する<sup>3</sup></h3>
<div class="fig">
<table class="avoid" style="table-layout:fixed;width:1060px">
<tr><th style="width:335px">リスク</th><th style="width:220px">4つの管理策の有効性</th><th style="width:80px">選択肢</th><th style="width:300px">追加のリスク対応</th><th style="width:125px">担当</th></tr>
<tr><td>ASI01 目標の乗っ取り</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td><td>低減</td><td>信頼できるファイルだけ持ち込む</td><td>利用者</td></tr>
<tr><td>ASI02 ツールの悪用</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td><td>低減</td><td>秘密は絞り、データは控えを取る</td><td>基盤の担当</td></tr>
<tr><td>ASI03 身元と権限の悪用</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td><td>回避</td><td>認証を渡さない</td><td>基盤の担当</td></tr>
<tr><td>ASI04 供給網のぜい弱性</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td><td>低減</td><td>確かめた部品だけ取り込む</td><td>基盤の担当</td></tr>
<tr><td>ASI05 想定外のコード実行</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td><td>低減</td><td>成果物はコンテナの中で動かす</td><td>利用者</td></tr>
<tr><td>ASI06 記憶と文脈の汚染</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td><td>回避</td><td>履歴を持ち越さない</td><td>利用者</td></tr>
<tr><td>ASI07 安全でないエージェント間通信</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td><td>回避</td><td>連携させない</td><td>基盤の担当</td></tr>
<tr><td>ASI08 連鎖的な障害</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td><td>回避</td><td>後工程につながない</td><td>利用者</td></tr>
<tr><td>ASI09 人の信頼の悪用</td><td class="out"><img src="icons/do_not_disturb_on-out.svg">低減できない</td><td>低減</td><td>確かめてから承認する</td><td>利用者</td></tr>
<tr><td>ASI10 暴走エージェント</td><td class="ok"><img src="icons/check_circle-ok.svg">低減できる</td><td>低減</td><td>人が見ている間だけ動かす</td><td>基盤の担当</td></tr>
</table>
</div>
</div></div>

---

# 基盤の担当が強制する設定

## 担当のうち基盤の担当は、5つのリスク対応を設定で強制する

<div class="ev"><div class="card">
<h3>5つのリスクと3つのぜい弱性に、設定で強制する対応がある<sup>4</sup></h3>
<div class="fig">
<table class="avoid" style="table-layout:fixed;width:1040px">
<tr><th style="width:340px">対象</th><th style="width:420px">基盤の担当が強制する設定</th><th style="width:280px">設定の場所</th></tr>
<tr><td>ASI02 ツールの悪用</td><td><img src="icons/shield-blue.svg">秘密は基盤から配る</td><td>コンテナの設定</td></tr>
<tr><td>ASI03 身元と権限の悪用</td><td><img src="icons/shield-blue.svg">Gitの認証を配らない</td><td>コンテナの設定</td></tr>
<tr><td>ASI04 供給網のぜい弱性</td><td><img src="icons/shield-blue.svg">通信の許可先を社内の部品置き場にする</td><td>コンテナの設定</td></tr>
<tr><td>ASI07 安全でないエージェント間通信</td><td><img src="icons/shield-blue.svg">連携先を許可したものに限る</td><td>Claude Codeの管理設定</td></tr>
<tr><td>ASI10 暴走エージェント</td><td><img src="icons/shield-blue.svg">許可確認を省く動かし方を禁じる</td><td>Claude Codeの管理設定</td></tr>
<tr><td>持ち出しの経路（SSHの宛先が無制限）</td><td><img src="icons/shield-blue.svg">SSHの宛先を許可先だけにする</td><td>コンテナの設定</td></tr>
<tr><td>設定のぜい弱性（版が未固定）</td><td><img src="icons/shield-blue.svg">版を固定し、自動更新を止める</td><td>コンテナの設定</td></tr>
<tr><td>監視のぜい弱性（記録がない）</td><td><img src="icons/shield-blue.svg">履歴の保存日数を決める</td><td>Claude Codeの管理設定</td></tr>
</table>
</div>
</div></div>

---

# 附属書Aとの比較

## リスク対応に要る管理策は、附属書Aと見比べて見落としを確かめる

<div class="ev"><div class="card">
<h3>附属書Aの93のうち14と見比べ、見落としが1つあった<sup>5</sup></h3>
<div class="fig">
<table class="avoid" style="table-layout:fixed;width:1060px;font-size:16px">
<tr><th style="width:250px">決めた管理策</th><th style="width:680px">見比べた附属書Aの管理策</th><th style="width:130px">結果</th></tr>
<tr><td>通信の許可リスト</td><td>8.20 ネットワークセキュリティ、8.22 ネットワークの分離、8.23 ウェブフィルタリング</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>非root実行</td><td>8.2 特権アクセス権</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>ファイルの隔離</td><td>8.3 情報へのアクセス制限</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>起動時の検証</td><td>8.9 構成管理</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>認証を渡さない決まり</td><td>5.17 認証情報</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>部品を確かめる決まり</td><td>5.21 ICTサプライチェーンにおける情報セキュリティの管理</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>10の決まりを定めること</td><td>5.10 情報およびその他の関連資産の利用の許容範囲</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>利用開始のときの教育</td><td>6.3 情報セキュリティの意識向上、教育および訓練</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>事故の報告と対応</td><td>6.8 情報セキュリティ事象の報告、5.26 情報セキュリティインシデントへの対応</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>ローカルの履歴を記録に残す</td><td>8.15 ログ取得</td><td class="ok"><img src="icons/check_circle-ok.svg">重なる</td></tr>
<tr><td>当たる管理策がない</td><td>8.16 監視活動</td><td class="part"><img src="icons/warning-part.svg">見落とし</td></tr>
</table>
</div>
</div></div>

---

# 残留リスク

## 管理策を講じた後の残留リスクは、リスク所有者が受容を承認する

<div class="ev"><div class="card">
<h3>6種類の残留リスクは、3つの条件を守る前提で受容する<sup>6</sup></h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1040px">
<tr><th style="width:220px">残留リスク</th><th style="width:70px">数</th><th style="width:440px">中身</th><th style="width:310px">受容の条件</th></tr>
<tr><td>判断に関わるリスク</td><td>4つ</td><td>4つの管理策が効かず、決まりに頼る</td><td>信頼できるファイルだけ持ち込む</td></tr>
<tr><td>持ち出しの経路</td><td>3つ</td><td>DNS、許可先、ホスト側ネットワーク</td><td>ホストの秘密を持ち込まない</td></tr>
<tr><td>設定のぜい弱性</td><td>2つ</td><td>許可IPの固定、IPv6</td><td>ホストの秘密を持ち込まない</td></tr>
<tr><td>ホスト側への波及</td><td>2つ</td><td>作業フォルダ経由の実行、認証の引き継ぎ</td><td>信頼できるファイルだけ持ち込む</td></tr>
<tr><td>監視のぜい弱性</td><td>1つ</td><td>監視がなく、記録は書き換えられる</td><td>Claudeの動作を監視する</td></tr>
<tr><td>強制の抜け道</td><td>1つ</td><td>設定を入れたイメージは差し替えられる</td><td>信頼できるファイルだけ持ち込む</td></tr>
</table>
</div>
</div></div>

---

<!-- header: '全体 ／ 計画 ／ **運用** ／ 評価 ／ 改善 ／ 承認' -->

# 運用の3つの場面

## 承認を得たら、利用開始、日々の利用、事故の3つの場面で運用する

<div class="ev"><div class="card">
<h3>3つの場面のどれにも利用者が関わる</h3>
<div class="fig roomy"><div class="flow" style="gap:0">
<div class="node desc"><img src="icons/login-blue.svg"><b>利用開始</b><span>申請、承認、払い出し、教育</span><span>利用者、基盤の担当、<br>情報セキュリティ責任者</span></div>
<div class="link" style="width:56px"></div>
<div class="node desc"><img src="icons/terminal-blue.svg"><b>日々の利用</b><span>10の決まりを守る</span><span>利用者<br>&nbsp;</span></div>
<div class="link" style="width:56px"></div>
<div class="node desc"><img src="icons/warning-blue.svg"><b>事故のとき</b><span>報告、封じ込め、再発防止</span><span>利用者、基盤の担当、<br>情報セキュリティ責任者</span></div>
</div></div>
</div></div>

---

# 利用開始の流れ

## 利用開始では、申請と承認を経て環境を払い出す

<div class="ev"><div class="card">
<h3>4つの手順を3つの役割が分担する</h3>
<div class="fig roomy"><div class="flow" style="gap:0">
<div class="node desc"><img src="icons/description-blue.svg"><b>申請</b><span>利用者</span><span>使う目的を<br>書く</span></div>
<div class="link" style="width:40px"></div>
<div class="node desc"><img src="icons/approval-blue.svg"><b>承認</b><span>情報セキュリティ責任者</span><span>使う目的を<br>確かめる</span></div>
<div class="link" style="width:40px"></div>
<div class="node desc"><img src="icons/deployed_code-blue.svg"><b>払い出し</b><span>基盤の担当</span><span>設定を入れたイメージを渡す<br>認証は渡さない</span></div>
<div class="link" style="width:40px"></div>
<div class="node desc"><img src="icons/school-blue.svg"><b>教育</b><span>利用者</span><span>10の決まりを学んで<br>使い始める</span></div>
</div></div>
</div></div>

---

# 日々の利用の決まり

## 払い出した環境では、10の決まりのうち5つを利用者が守る

<div class="ev"><div class="card">
<h3>10のうち5つは設定で強制し、5つは利用者が守る</h3>
<div class="fig">
<table class="avoid" style="table-layout:fixed;width:1050px">
<tr><th style="width:330px">リスク</th><th style="width:310px">決まり</th><th style="width:180px">守らせ方</th><th style="width:230px">残す記録</th></tr>
<tr><td>ASI01 目標の乗っ取り</td><td>信頼できるファイルだけ持ち込む</td><td><img src="icons/person-blue.svg">利用者が守る</td><td>自己点検の記録</td></tr>
<tr><td>ASI02 ツールの悪用</td><td>秘密は絞り、データは控えを取る</td><td><img src="icons/shield-blue.svg">設定で強制</td><td>払い出しの記録</td></tr>
<tr><td>ASI03 身元と権限の悪用</td><td>認証を渡さない</td><td><img src="icons/shield-blue.svg">設定で強制</td><td>払い出しの記録</td></tr>
<tr><td>ASI04 供給網のぜい弱性</td><td>確かめた部品だけ取り込む</td><td><img src="icons/shield-blue.svg">設定で強制</td><td>払い出しの記録</td></tr>
<tr><td>ASI05 想定外のコード実行</td><td>成果物はコンテナの中で動かす</td><td><img src="icons/person-blue.svg">利用者が守る</td><td>自己点検の記録</td></tr>
<tr><td>ASI06 記憶と文脈の汚染</td><td>履歴を持ち越さない</td><td><img src="icons/person-blue.svg">利用者が守る</td><td>自己点検の記録</td></tr>
<tr><td>ASI07 安全でないエージェント間通信</td><td>連携させない</td><td><img src="icons/shield-blue.svg">設定で強制</td><td>払い出しの記録</td></tr>
<tr><td>ASI08 連鎖的な障害</td><td>後工程につながない</td><td><img src="icons/person-blue.svg">利用者が守る</td><td>自己点検の記録</td></tr>
<tr><td>ASI09 人の信頼の悪用</td><td>確かめてから承認する</td><td><img src="icons/person-blue.svg">利用者が守る</td><td>自己点検の記録</td></tr>
<tr><td>ASI10 暴走エージェント</td><td>人が見ている間だけ動かす</td><td><img src="icons/shield-blue.svg">設定で強制</td><td>払い出しの記録</td></tr>
</table>
</div>
</div></div>

---

# 事故のときの流れ

## 利用者は、事故に気付いたら報告し、封じ込めから再発防止へ進める

<div class="ev"><div class="card">
<h3>5つの手順を3つの役割が分担する</h3>
<div class="fig roomy"><div class="flow" style="gap:0">
<div class="node desc" style="padding-left:12px;padding-right:12px"><img src="icons/search-blue.svg"><b>検知</b><span>利用者</span><span>異常に<br>気付く</span></div>
<div class="link"></div>
<div class="node desc" style="padding-left:12px;padding-right:12px"><img src="icons/campaign-blue.svg"><b>報告</b><span>利用者</span><span>責任者へ<br>すぐ伝える</span></div>
<div class="link"></div>
<div class="node desc" style="padding-left:12px;padding-right:12px"><img src="icons/block-blue.svg"><b>封じ込め</b><span>基盤の担当</span><span>コンテナを止め<br>認証を無効にする</span></div>
<div class="link"></div>
<div class="node desc" style="padding-left:12px;padding-right:12px"><img src="icons/troubleshoot-blue.svg"><b>調査</b><span>情報セキュリティ責任者</span><span>原因と範囲を<br>調べる</span></div>
<div class="link"></div>
<div class="node desc" style="padding-left:12px;padding-right:12px"><img src="icons/build-blue.svg"><b>再発防止</b><span>情報セキュリティ責任者</span><span>決まりと設定を<br>見直す</span></div>
</div></div>
</div></div>

---

<!-- header: '全体 ／ 計画 ／ 運用 ／ **評価** ／ 改善 ／ 承認' -->

# 残す記録

## 報告と日々の記録は、内部監査で決まりどおりかを評価する

<div class="ev"><div class="card">
<h3>5つの記録を3つの場面で作る</h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1020px">
<tr><th style="width:280px">記録</th><th style="width:160px">作る人</th><th style="width:160px">場面</th><th style="width:420px">内部監査で確かめること</th></tr>
<tr><td><img src="icons/description-blue.svg">利用の申請</td><td>利用者</td><td>利用開始</td><td>使う目的が承認されているか</td></tr>
<tr><td><img src="icons/description-blue.svg">払い出しの記録</td><td>基盤の担当</td><td>利用開始</td><td>強制する設定を入れて渡しているか</td></tr>
<tr><td><img src="icons/description-blue.svg">自己点検の記録</td><td>利用者</td><td>日々の利用</td><td>利用者が守る5つを守っているか</td></tr>
<tr><td><img src="icons/description-blue.svg">ローカルの履歴</td><td>Claude Code</td><td>日々の利用</td><td>事故のときに動作をたどれるか</td></tr>
<tr><td><img src="icons/description-blue.svg">事故の報告</td><td>利用者</td><td>事故のとき</td><td>再発防止まで済んでいるか</td></tr>
</table>
</div>
</div></div>

---

# 評価に残る課題

## 評価するための記録と検証には、まだ2つの課題がある

<div class="ev">
<div class="card">
<h3>ローカルの履歴は利用者が書き換えられる</h3>
<div class="fig"><div class="col mid" style="gap:0">
<div class="pill mute"><img src="icons/visibility_off-blue.svg"><b>課題</b>記録を守る仕組みがない</div>
<div class="link v lab"><span>当面</span></div>
<div class="pill"><img src="icons/visibility-blue.svg">人が見ている間だけ動かす</div>
<div class="link v lab"><span>対処</span></div>
<div class="pill good"><img src="icons/check_circle-ok.svg">記録の守り方を次の計画で決める</div>
</div></div>
</div>
<div class="card">
<h3>強制する設定とぜい弱性は実機で試していない</h3>
<div class="fig"><div class="col mid" style="gap:0">
<div class="pill mute"><img src="icons/lock_open-blue.svg"><b>課題</b>文書を読んだだけの評価</div>
<div class="link v lab"><span>当面</span></div>
<div class="pill"><img src="icons/approval-blue.svg">ぜい弱性があるものとして受容する</div>
<div class="link v lab"><span>対処</span></div>
<div class="pill good"><img src="icons/check_circle-ok.svg">実機での検証を次の計画に入れる</div>
</div></div>
</div>
</div>

---

<!-- header: '全体 ／ 計画 ／ 運用 ／ 評価 ／ **改善** ／ 承認' -->

# 見直しのきっかけ

## 課題と評価の結果は、マネジメントレビューで見直して計画に戻す

<div class="ev"><div class="card">
<h3>見直しは定期のほか4つのきっかけで行う</h3>
<div class="fig"><div class="flow" style="gap:0">
<div class="branches merge">
<div class="br" style="padding:8px 0"><div class="pill"><img src="icons/event-blue.svg">定期の見直し</div><div class="link plain"></div></div>
<div class="br" style="padding:8px 0"><div class="pill"><img src="icons/settings-blue.svg">設定例が更新された</div><div class="link plain"></div></div>
<div class="br" style="padding:8px 0"><div class="pill"><img src="icons/fact_check-blue.svg">10のリスクが改訂された</div><div class="link plain"></div></div>
<div class="br" style="padding:8px 0"><div class="pill"><img src="icons/warning-blue.svg">事故が起きた</div><div class="link plain"></div></div>
<div class="br" style="padding:8px 0"><div class="pill"><img src="icons/block-blue.svg">残留リスクが大きい構成を始める</div><div class="link plain"></div></div>
</div>
<div class="link" style="width:40px"></div>
<div class="node desc"><img src="icons/groups-blue.svg"><b>マネジメント<br>レビュー</b><span>経営層が<br>結果を見直す</span></div>
<div class="link" style="width:40px"></div>
<div class="node desc"><img src="icons/edit_note-blue.svg"><b>計画</b><span>リスクを評価し直し<br>リスク対応を決め直す</span></div>
</div></div>
</div></div>

---

<!-- header: '全体 ／ 計画 ／ 運用 ／ 評価 ／ 改善 ／ **承認**' -->

# ご承認いただきたい3つのこと

## 計画を運用に移すには、3つの承認が要る

<div class="ev"><div class="card">
<h3>3つのうち2つはリスク所有者が承認する</h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1030px">
<tr><th style="width:300px">承認すること</th><th style="width:250px">承認する人</th><th style="width:250px">残す記録</th><th style="width:230px">根拠のスライド</th></tr>
<tr><td><img src="icons/approval-blue.svg">リスク対応の内容</td><td>リスク所有者</td><td>リスク対応計画</td><td>リスク対応の選択<br>附属書Aとの比較</td></tr>
<tr><td><img src="icons/approval-blue.svg">残留リスクの受容</td><td>リスク所有者</td><td>残留リスクの受容の記録</td><td>残留リスク</td></tr>
<tr><td><img src="icons/approval-blue.svg">担当の割り当てと利用開始</td><td>情報セキュリティ責任者</td><td>利用の承認の記録</td><td>段階ごとの担当と記録<br>利用開始の流れ</td></tr>
</table>
</div>
</div></div>

---

<!-- header: 全体 ／ 計画 ／ 運用 ／ 評価 ／ 改善 ／ 承認 -->

# まとめ

## Dev Containerは、3つの承認を得てISMSの4つの段階で運用する

<div class="ev"><div class="card">
<div class="fig"><div class="col mid" style="gap:0;align-items:flex-start">
<div class="pt"><div class="pill tag"><img src="icons/map-blue.svg"><b>全体</b></div><div class="link plain"></div><div class="ptx"><h3>4つの段階は、計画、運用、評価、改善の順に回り、承認で始まる</h3></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/edit_note-blue.svg"><b>計画</b></div><div class="link plain"></div><div class="ptx"><h3>計画では、10のリスクごとにリスク対応と担当を決める</h3></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/play_circle-blue.svg"><b>運用</b></div><div class="link plain"></div><div class="ptx"><h3>承認を得たら、利用開始、日々の利用、事故の3つの場面で運用する</h3></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/fact_check-blue.svg"><b>評価</b></div><div class="link plain"></div><div class="ptx"><h3>報告と日々の記録は、内部監査で決まりどおりかを評価する</h3></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/autorenew-blue.svg"><b>改善</b></div><div class="link plain"></div><div class="ptx"><h3>課題と評価の結果は、マネジメントレビューで見直して計画に戻す</h3></div></div>
<div class="link v" style="margin-left:64px;height:26px"></div>
<div class="pt"><div class="pill tag"><img src="icons/approval-blue.svg"><b>承認</b></div><div class="link plain"></div><div class="ptx"><h3>計画を運用に移すには、3つの承認が要る</h3></div></div>
</div></div>
</div></div>

---

<!-- header: 付録 -->

# 付録1 Claude Codeの管理設定

## Claude Codeの管理設定は、1つのファイルに書いてイメージに入れる

<div class="ev"><div class="card">
<h3>3つの設定は /etc/claude-code/managed-settings.json に書く<sup>7</sup></h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1060px">
<tr><th style="width:330px">強制する設定</th><th style="width:450px">設定の名前</th><th style="width:280px">値</th></tr>
<tr><td>許可確認を省く動かし方を禁じる</td><td>permissions.disableBypassPermissionsMode</td><td>"disable"</td></tr>
<tr><td>連携先を許可したものに限る</td><td>allowedMcpServers</td><td>許可する連携先の一覧</td></tr>
<tr><td>連携先を許可したものに限る</td><td>allowManagedMcpServersOnly</td><td>true</td></tr>
<tr><td>履歴の保存日数を決める</td><td>cleanupPeriodDays</td><td>日数（既定は30、最小は1）</td></tr>
</table>
</div>
</div></div>

---

# 付録2 コンテナの設定

## コンテナの設定は、設定例の2つのファイルを書き換える

<div class="ev"><div class="card">
<h3>5つの設定を2つのファイルで強制する<sup>8</sup></h3>
<div class="fig">
<table class="big same" style="table-layout:fixed;width:1060px">
<tr><th style="width:365px">強制する設定</th><th style="width:185px">ファイル</th><th style="width:510px">書き換える内容</th></tr>
<tr><td>版を固定し、自動更新を止める</td><td>devcontainer.json</td><td>CLAUDE_CODE_VERSION を latest から決めた版にする</td></tr>
<tr><td>版を固定し、自動更新を止める</td><td>devcontainer.json</td><td>containerEnv に DISABLE_AUTOUPDATER を 1 で足す</td></tr>
<tr><td>通信の許可先を社内の部品置き場にする</td><td>init-firewall.sh</td><td>許可先の registry.npmjs.org を社内の部品置き場に替える</td></tr>
<tr><td>SSHの宛先を許可先だけにする</td><td>init-firewall.sh</td><td>22番ポートを宛先を問わず許可する2行を消す</td></tr>
<tr><td>秘密は基盤から配る</td><td>devcontainer.json</td><td>containerEnv で渡し、mounts は足さない</td></tr>
<tr><td>Gitの認証を配らない</td><td>devcontainer.json</td><td>containerEnv と mounts にGitの認証を入れない</td></tr>
</table>
</div>
</div></div>

---

<!-- _class: source -->
<!-- header: '' -->

# 参考文献（1/2）

<div class="ev"><div class="card">
<div class="fig">
<table class="big same refs">
<tr><td>1.</td><td>（氏名）, "Claude CodeのDev Containerで低減できるリスク" (2026)<br>10のリスク、4つの管理策、10のぜい弱性は、この資料による</td></tr>
<tr><td>2.</td><td>一般財団法人日本情報経済社会推進協会, "ISMSユーザーズガイド" JIP-ISMS111-4.0 (2025);<br><a href="https://www.jipdec.or.jp/archives/publications/JIP-ISMS111-4.0.pdf">www.jipdec.or.jp/archives/publications/JIP-ISMS111-4.0.pdf</a></td></tr>
<tr><td>3.</td><td>独立行政法人情報処理推進機構, "中小企業の情報セキュリティ対策ガイドライン 第3.1版<br>リスク分析シート" (2024);<br><a href="https://www.ipa.go.jp/security/sme/f55m8k000000587z-att/outline_guidance_risk.pdf">www.ipa.go.jp/security/sme/f55m8k000000587z-att/outline_guidance_risk.pdf</a></td></tr>
<tr><td>4.</td><td>Anthropic, Development containers, Claude Code Docs (2026);<br><a href="https://code.claude.com/docs/en/devcontainer">code.claude.com/docs/en/devcontainer</a></td></tr>
<tr><td>5.</td><td>ISMS Guide, 管理策一覧（Annex A） (2026);<br><a href="https://isms-guide.com/controls/">isms-guide.com/controls/</a></td></tr>
</table>
</div>
</div></div>

---

<!-- _class: source -->

# 参考文献（2/2）

<div class="ev"><div class="card">
<div class="fig">
<table class="big same refs">
<tr><td>6.</td><td>日本産業標準調査会, "JIS Q 27001:2014 情報セキュリティマネジメントシステム―要求事項" （現行は2025年版） (2014);<br><a href="https://kikakurui.com/q/Q27001-2014-01.html">kikakurui.com/q/Q27001-2014-01.html</a></td></tr>
<tr><td>7.</td><td>Anthropic, Control MCP server access for your organization; Explore the .claude directory, Claude Code Docs (2026);<br><a href="https://code.claude.com/docs/en/managed-mcp">code.claude.com/docs/en/managed-mcp</a><br><a href="https://code.claude.com/docs/en/claude-directory">code.claude.com/docs/en/claude-directory</a></td></tr>
<tr><td>8.</td><td>Anthropic, claude-code: .devcontainer (2026);<br><a href="https://github.com/anthropics/claude-code/tree/main/.devcontainer">github.com/anthropics/claude-code/tree/main/.devcontainer</a></td></tr>
</table>
</div>
</div></div>
