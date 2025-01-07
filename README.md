授業:  Web開発実習
担当:  末吉先生

出題:  2024/11/12
期限:  2025/01/20

# 要件
1. 「ガチャ」「11連ガチャ」を引けて結果を表示させることができる。
例）ガチャを引いた結果　SR

2. 結果の累計を表示し、リセットボタン等で累計を初期化することができる。
例）今までの結果
    15回（ガチャ4回、11連ガチャ1回）引き1400円使った。
    今までに15枚買った。
    または、Nが10枚、Rが3枚、SR+（キャラ2）、SR+（キャラ5）

3. 全種類のSR+が出るまでいくらかかるかを表示できる
   ※ガチャを回し続けた結果でも良いですし、11連ガチャを回し続けた結果でも良いです。
例）121回引き（ガチャ0回、11連ガチャ11回）11000円使った。

4. 画像とCSSフレームワークを使っている。(加点)
なお、画像はN、N+、R、R+、SR、SR+で各10種類以上異なるものが用意されていること。
例）N:20種類、N+:20種類、R:15種類、R+:15種類、SR:10種類、SR+:10種類

※数字(1~4)は難易度が易しい順。
※今回はJavaScriptを用いても良いですが、CookieやWebStrageの使用は不可。2.や3.はサーバに記録していること。

# ガチャガチャシミュレータの仕様
## 画像
画像を使う場合はこのページに添付しているもののみとします。
添付しているものは、配布元の一部の画像を「縮小専用。」というソフトでリサイズしたものです。自身でリサイズしても可。
**縮小専用。の詳細情報: Vector ソフトを探す！**
https://www.vector.co.jp/soft/win95/art/se153674.html?ds

画像の配布元は以下のサイトになります。
**星宝転生ジュエルセイバーよ永遠に**
http://www.jewel-s.jp/about/
※著作権表示をアプリに表示させること。（最低限、[]内の文字のみでも可）
タイトル: [ジュエルセイバーFREE]
URL: [http://www.jewel-s.jp/]

カード以外の部分の画像は、利用規約に反しないものであれば利用可とします。利用する場合、配布元の表示をしてください。

## 音、音楽
使用不可。

## 画面デザイン
CSSフレームワークの使用は、「Bootstrap」または「new.css」のみとします。
※Bootstrap、new.cssは前期のWeb技術基礎で扱いました。

## カードの種類とその値段
### ガチャの種類
「ノーマル」：1回100円、1回だけ引く。
「１１連続」：1回1000円、11回だけ引く。
※1回引くごとにカードを1枚入手できる。

### カードのレアリティ
レアリティというのは希少度と訳されます。希少度の高いほうが価値も高くなります。

### レアリティの種類（価値が低い順）：説明　
N    (20種類)
N+   (20種類)
R    (15種類)
R+   (15種類)
SR   (10種類)
SR+  (10種類) ←これを入手するのが目的

## 当選確率
「通常ガチャ」の当選確率は次の通りです。
N    33％
N+   25％
R    20％
R+   15％
SR    5％
SR+   2％

「11連ガチャ」の当選確率は次の通りです。
N    33％（通常ガチャと同じ）
N+   25％（通常ガチャと同じ）
R    57％
R+   30％
SR   10％
SR+   3％

※ただし11連ガチャではボーナスとして、最後の1枚は必ず「SR」が当選します。

## SR+の種類
SR+を入手することがガチャガチャを引く目的です。このSR+のカードはキャラ1から10までの10種類あります。
SR+が当選した場合、このキャラのいずれか1枚が等確率で入手できるものとします。

## クレジット
開発環境: Replit
開発言語: Python 3.12.x(?)
開発者:  Takemase
