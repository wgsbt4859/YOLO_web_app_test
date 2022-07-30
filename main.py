# main.py
# ルーティンの設定

# 下記サイトを参考
# https://qiita.com/Gyutan/items/1f81afacc7cac0b07526

# Flaskモジュールの読み込み
from flask import Flask, render_template, Response

# camera.pyからVideoCameraクラスの読み込み
from camera import VideoCamera
import torch

app = Flask(__name__)

# indexページ
@app.route('/')
def index():
    return render_template('index.html')

# カメラから取得した画像の生成
def gen(camera):
    
    #認識モデルの読み込み
    model = get_model()

    while True:
        #VideoCamera クラスのget_frame関数
        frame = camera.get_frame(model)

        # Content-Type（送り返すファイルの種類として）multipart/x-mixed-replace を利用
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# モデルの読み込み
def get_model():
    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

    #model_path = 'local path'

    # モデルの読み込み
    #YOLOv7
    # model = torch.hub.load('WongKinYiu/yolov7', 'custom', model_path)

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    model.to(device)

    # 検出の設定
    model.conf = 0.5  # 検出下限値。設定しなければすべて検出
    model.classes = [0]  # personだけを検出する

    return model

#/video_feedページ
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(debug=True)