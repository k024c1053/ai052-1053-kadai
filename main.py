from flask import Flask, render_template, request, redirect, url_for, make_response
from gacha import Gacha
from datetime import datetime

app = Flask(__name__)

gacha = Gacha()

# Cookieの有効期限の定義
COOKIE_MAX_AGE = 60 * 60 * 24 * 90  # 90日

# Cookieを読み込むメソッド
def load_cookies():
    gacha.play_count = int(request.cookies.get('play_count', 0))
    gacha.single_count = int(request.cookies.get('single_count', 0))
    gacha.eleven_count = int(request.cookies.get('eleven_count', 0))
    gacha.cost = int(request.cookies.get('cost', 0))

    # 各ランクの収集状況を読み込む
    for rank in gacha.collected_characters.keys():
        cookie_value = request.cookies.get(f'collected_{rank}', '')
        if cookie_value:
            gacha.collected_characters[rank] = set(cookie_value.split(','))

# Cookieを保存するメソッド
def save_cookies(response):
    expires = int(datetime.now().timestamp()) + COOKIE_MAX_AGE
    response.set_cookie('play_count',
                        str(gacha.play_count),
                        max_age=COOKIE_MAX_AGE,
                        expires=expires)
    response.set_cookie('single_count',
                        str(gacha.single_count),
                        max_age=COOKIE_MAX_AGE,
                        expires=expires)
    response.set_cookie('eleven_count',
                        str(gacha.eleven_count),
                        max_age=COOKIE_MAX_AGE,
                        expires=expires)
    response.set_cookie('cost',
                        str(gacha.cost),
                        max_age=COOKIE_MAX_AGE,
                        expires=expires)

    # 各ランクの収集状況を保存
    for rank, characters in gacha.collected_characters.items():
        response.set_cookie(f'collected_{rank}',
                            ','.join(characters),
                            max_age=COOKIE_MAX_AGE,
                            expires=expires)


@app.route('/')
def index():
    load_cookies()  # Cookieを読み込むメソッドを呼び出す
    summary = gacha.get_summary()
    return render_template("index.html", summary=summary)


@app.route('/gacha', methods=['GET', 'POST'])
def gacha_draw():
    if request.method == 'GET':
        return redirect(url_for('index'))

    load_cookies()  # Cookieを読み込むメソッドを呼び出す

    # ガチャを引く
    gacha_type = request.form['gacha_type']
    if gacha_type == "single":
        results = [gacha.draw_single()]
    elif gacha_type == "eleven":
        results = gacha.draw_eleven()

    # 結果をテンプレートに渡す
    summary = gacha.get_summary()
    response = make_response(
        render_template("index.html", results=results, summary=summary))

    # Cookieに保存するメソッド呼び出し
    save_cookies(response)
    return response


@app.route('/reset', methods=['GET', 'POST'])  # GETとPOSTを許可
def reset():
    if request.method == 'GET':
        return redirect(url_for('index'))

    # ガチャデータをリセット
    gacha.reset()

    # Cookieもリセット
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('play_count')
    response.delete_cookie('single_count')
    response.delete_cookie('eleven_count')
    response.delete_cookie('cost')

    # 各ランクの収集状況のCookieも削除
    for rank in gacha.collected_characters.keys():
        response.delete_cookie(f'collected_{rank}')

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
