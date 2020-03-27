#サーバー側の処理を書くファイル
import os

#request フォームから送信した情報を扱うためのモジュール
#redirect ページの移動
#url_for　アドレス遷移
from flask import Flask,flash, request, redirect, url_for, render_template
#ファイル名をチェックする関数
from werkzeug.utils import secure_filename
#画像のダウンロード
from flask import send_from_directory

#初期設定
UPLOAD_FOLDER='./Testdata'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1203"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#アップロードされた画像の拡張子の確認
def allowed_file(filename):
    #.があるかどうかのチェック & 拡張子の確認
    # OKなら1, だめなら0
    return '.' in  filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Home
@app.route('/')
def index():
    return render_template('index.html')

#Usage
@app.route('/Usage')
def Usage():
    return render_template('usage.html')

#Detection
#detectionページでの画像アップロード
@app.route('/detection', methods=['GET', 'POST'])
def uploads_file():
    #リクエストがポストかどうかの判別
    if request.method == 'POST':
        #ファイルが無かった場合の処理
        if 'file' not in request.files:
            flash("マスク画像を選択してください")
            return redirect(request.url)
        #データの取り出し
        file = request.files['file']
        #ファイル名がなかった場合の処理
        if file.filename == '':
            flash('マスク画像を選択してください')
            return redirect(request.url)
        #ファイルのチェック
        if file and allowed_file(file.filename):
            #危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            #ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #アップロード後のページに転送
            return redirect(url_for('uploaded_file', filename=filename))
    
    return render_template('detection.html')

@app.route('/detection/<filename>')
#ファイルを表示する
def uploaded_file(filename):
    return render_template('result.html', filename=filename)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
