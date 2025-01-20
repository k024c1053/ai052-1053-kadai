from flask import Flask, render_template, request, redirect, url_for, session
from gacha import Gacha
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'bXlfc2VsZWN0X2tleQ=='  # セッション用のキー(エンコーダ済み) 2025.1.20
app.permanent_session_lifetime = timedelta(days=90)  # セッションの有効期限 2025.1.20

gacha = Gacha()


# セッションデータを初期化する関数 2025.1.20
def initialize_session():
    session['play_count'] = 0
    session['single_count'] = 0
    session['eleven_count'] = 0
    session['cost'] = 0
    session['collected_characters'] = {  # 初期時点ではリストで管理 2025.1.20
        "N": [],
        "N+": [],
        "R": [],
        "R+": [],
        "SR": [],
        "SR+": []
    }


@app.route('/')
def index():

    # セッションが未初期化の場合、初期化を行う 2025.1.20
    if 'play_count' not in session:
        initialize_session()

    summary = gacha.get_summary(session)
    return render_template("index.html", summary=summary)


@app.route('/gacha', methods=['POST'])
def gacha_draw():
    if request.method == 'POST':
        gacha_type = request.form['gacha_type']

        # ガチャを引く処理
        if gacha_type == "single":
            results = [gacha.draw_single(session)]
        elif gacha_type == "eleven":
            results = gacha.draw_eleven(session)

        # ガチャ結果をセッションに保存 2025.1.20
        session['last_results'] = results

        # PRGパターン:
        # PRG パターンでは、POSTリクエストを処理した後に、redirectを用いてユーザーをGETリクエストのページ（通常は結果表示用ページ）にリダイレクトします。
        # これにより、再読み込み時にブラウザがPOSTを再送信しなくなります。ChatGPT先生より引用 2025.1.20
        return redirect(url_for('gacha_results'))

    return redirect(url_for('index'))


# ガチャ結果を表示するためのページを新たに追加するメソッド 2025.1.20
@app.route('/gacha_results', methods=['GET'])
def gacha_results():

    # セッションからガチャ結果を取得
    results = session.pop('last_results', None)  # 一度取得したら削除
    summary = gacha.get_summary(session)
    return render_template("index.html", results=results, summary=summary)


@app.route('/reset', methods=['POST'])
def reset():
    # セッションデータを初期化
    initialize_session()
    # リダイレクトして再読み込み時のPOST再送信を防ぐ 2025.1.20
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
