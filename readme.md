# YOLO、Flaskを用いた簡単な画像認識WEBアプリ

最終更新：2022/7/30

## 概要
webカメラを使用して作業場所を移し、特定の場所に人が入ったらアラートを出すwebアプリ（の試作）

## DEMO

### 通常
<img width="512" alt="1" src="https://user-images.githubusercontent.com/27219001/181904715-f1776a9f-e592-413f-ad0d-067bdd846496.png">

### 危険エリアに人が検知された場合
<img width="495" alt="2" src="https://user-images.githubusercontent.com/27219001/181904720-5c261b4f-8174-43b6-bf81-c61588c9c758.png">


## 背景
製造現場にて、人が入ったら危ない場所がある。そこに近づいた人をリアルタイムに認識し、アラートを出せるアプリが欲しかった。

### 使用したモジュール、モデル
- webアプリ化：Flask
- 物体検出：YOLO
  - 最初は2022/7にリリースされたv7を使用したが、自身のpcが低スペック（gpu未搭載）なため、cpuだけで快適に動作するv5を使用。

# Requirement

requirements.txtを別途参照のこと。

# Installation

## requirementsで示したライブラリ

pipでinstall可能。

## YOLOv5の導入

```bash
!git clone https://github.com/ultralytics/yolov5
```
でcloneしてください。

# Usage

Herokuにデプロイしたサイトを近日公開予定。

# License

This web app is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).



