#サーバー側の処理を書くファイル

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Usage')
def Usage():
    return render_template('usage.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
