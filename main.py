from flask import Flask, render_template, request, redirect, url_for
from gacha import Gacha

app = Flask(__name__)
# app.secret_key = 'your_secret_key'
gacha = Gacha()

@app.route('/')
def index():
    # 累計情報を取得してテンプレートへ
    summary = gacha.get_summary()
    return render_template("index.html", summary=summary)

@app.route('/gacha', methods=['POST'])
def gacha_draw():
    # ガチャの種類に応じて結果を取得
    gacha_type = request.form['gacha_type']
    if gacha_type == "single":
        results = [gacha.draw_single()]
    elif gacha_type == "eleven":
        results = gacha.draw_eleven()
    else:
        results = None

    summary = gacha.get_summary()
    return render_template("index.html", results=results, summary=summary)

@app.route('/reset', methods=['POST'])
def reset():
    # 累計情報をリセット
    gacha.reset()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
