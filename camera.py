# camera.py

import cv2
import torch

class VideoCamera(object):
    def __init__(self):
        # webカメラを動画ソースとして設定
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        # 終了時にwebカメラをオフにする
        self.video.release()

    def get_frame(self, model):
        #動画の読み込み
        success, image = self.video.read()

        #動画の認識
        image = recog(model, image, size=160, pos_x=300)

        #読み込んだ動画(raw images)をjpgへ変換
        ret, jpeg = cv2.imencode('.jpg', image)

        # numpy.ndarray型のjpgをbytes型へ変換
        return jpeg.tobytes()
    

# 物体検出
def recog(model, imgs, size, pos_x):

    results = model(imgs, size=size)

    # --- 出力 ---
    # --- 検出結果を画像に描画して表示 ---
    #--- 各検出について
    for *box, conf, cls in results.xyxy[0]:  # xyxy, confidence, class

        # Debug用
        # print(results.xyxy[0])

        # --- ヒットしたかどうかで枠色（cc）と文字色（cc2）の指定
        if int(box[0]) < pos_x:
            s = "DANGER!!"
            cc = (0, 0, 250)
            cc2 = (128, 0, 0)
            # print(s)
            # messagebox.showerror(s, "危険エリアに人を検知しました。作業を再開しますか？")
        else:
            s = model.names[int(cls)]+":"+'{:.1f}'.format(float(conf)*100)
            cc = (0, 255, 255)
            cc2 = (0, 128, 128)

        #--- 枠描画
        cv2.rectangle(
            imgs,
            (int(box[0]), int(box[1])),
            (int(box[2]), int(box[3])),
            color=cc,
            thickness=2,
        )
        #--- 文字枠と文字列描画
        cv2.rectangle(imgs, (int(box[0]), int(box[1])-20),
                    (int(box[0])+len(s)*10, int(box[1])), cc, -1)
        cv2.putText(imgs, s, (int(box[0]), int(
            box[1])-5), cv2.FONT_HERSHEY_PLAIN, 1, cc2, 1, cv2.LINE_AA)

    #--- ヒットエリアのラインを描画
    cv2.line(imgs, (pos_x, 0), (pos_x, 640), (128, 128, 128), 3)

    #--- 描画した画像を表示
    # cv2.imshow('color', imgs)

    return imgs