授業:  Web開発実習  
担当:  末吉先生  
出題:  2024/11/12  
期限:  2025/01/20

# 要件
1. 「ガチャ」「11連ガチャ」を引けて結果を表示させることができる。  

2. 結果の累計を表示し、リセットボタン等で累計を初期化することができる。
   
3. 全種類のSR+が出るまでいくらかかるかを表示できる。  
   ※ガチャを回し続けた結果でも良いですし、11連ガチャを回し続けた結果でも良いです。
   
   例）_通常ガチャの場合_  
   > -通常ガチャの結果-  
   > R  
   > -今までの結果-  
   > 通常ガチャ 4回  
   > 11連ガチャ 1回  
   > 累計プレイ 5回  
   > 総課金額 1400円、購入枚数 15枚  
   > N 10枚、R 3枚、SR+ 2枚

   例）_11連ガチャの場合_  
   > -11連ガチャの結果-  
   > R、R、SR、N、N+、  
   > N+、R+、R+、N+、R、  
   > SR  
   > -今までの結果-  
   > 通常ガチャ 4回  
   > 11連ガチャ 1回  
   > 累計プレイ 5回  
   > 総課金額 1400円、購入枚数 15枚  
   > N 10枚、R 3枚、SR+ 2枚

5. 画像とCSSフレームワークを使っている。(加点)  
   なお、画像はN、N+、R、R+、SR、SR+で各10種類以上異なるものが用意されていること。  
   例）
   > N: 20種類  N+: 20種類  
   > R: 15種類  R+: 15種類  
   > SR: 10種類  SR+: 10種類

※数字(1~4)は難易度が易しい順。  
※今回はJavaScriptを用いても良いですが、CookieやWebStrageの使用は不可。2.や3.はサーバに記録していること。

# ガチャガチャシミュレータの仕様
## 画像
画像を使う場合はこのページに添付しているもののみとします。  
添付しているものは、配布元の一部の画像を「縮小専用。」というソフトでリサイズしたものです。自身でリサイズしても可。  
> **縮小専用。の詳細情報: Vector ソフトを探す！**  
https://www.vector.co.jp/soft/win95/art/se153674.html?ds

画像の配布元は以下のサイトになります。  
> **星宝転生ジュエルセイバーよ永遠に**
http://www.jewel-s.jp/about/

※著作権表示をアプリに表示させること。（最低限、[]内の文字のみでも可）  
> タイトル: [ジュエルセイバーFREE]  
> URL: [http://www.jewel-s.jp/]

カード以外の部分の画像は、利用規約に反しないものであれば利用可とします。    
利用する場合、配布元の表示をしてください。

## 音、音楽  
なし。

## 画面デザイン  
CSSフレームワークの使用は、「Bootstrap」または「new.css」のみとします。  
※Bootstrap、new.cssは前期のWeb技術基礎で扱いました。  

## カードの種類とその値段  
### ガチャの種類  
「ノーマル」：1回100円、1回だけ引く。  
「１１連続」：1回1000円、11回だけ引く。

※1回引くごとにカードを1枚入手できる。

### カードのレアリティと確率
レアリティというのは希少度と訳されます。希少度の高いほうが価値も高くなります。

| ランク | 種類 | 通常ガチャの出現率 | 11連ガチャの出現率（単発） |
|---|---|---:|---:|
| N | 20 | 33% | 33% |
| N+ | 20 | 25% | 25% |
| R | 15 | 20% | 57% |
| R+ | 15 | 15% | 30% |
| SR | 10 | 5% | 10% |
| SR+ | 10 | 2% | 3% |

※ただし11連ガチャではボーナスとして、最後の1枚は必ず「SR」が当選します。

## 実装機能
・ノーマルガチャ（1回100円）  
・11連ガチャ（1回1000円）  
・これまでの課金額の確認（合計、ノーマル、11連、それぞれに対応）  
・コレクション別獲得状況の確認（コンプリートしたからといって演出とかはない）  
・記録の破棄（確認メッセージ付、課金額や獲得状況などがすべて破棄される）  

## SR+の種類
SR+を入手することがガチャガチャを引く目的です。このSR+のカードはキャラ1から10までの10種類あります。  
SR+が当選した場合、このキャラのいずれか1枚が等確率で入手できるものとします。

## クレジット
開発環境: Replit  
開発言語: Python 3.12.x(?)  
開発者:  Takemase
