# RitsuWiFi
構内無線LANの接続をより簡単に。

***立命館大学構内で利用可能***

[English](https://github.com/fang2hou/RitsuWifi)| [日本語](https://github.com/fang2hou/RitsuWifi/blob/master/Readme.ja-JP.md) | [简体中文](https://github.com/fang2hou/RitsuWifi/blob/master/Readme.zh-CN.md)

## プレビュー
<img src="https://cdn.rawgit.com/fang2hou/RitsuWiFi/master/ExampleImages/Main.png" width="250px"/>

## 準備
___Python___: 2.6以降 / 3.3以降

Python 2.7 & 3.6 で RitsuWiFi のビルドと実行テストを行う。

RitsuWiFi を　macOS Python 3.X で実行する場合、```pip``` や ```python``` ではなく、```pip3``` と ```python3``` を活用してください。

___追加ライブラリ___: ```requests```、```rumps```
## TODO
- [x] POSTメソッドでのログイン
- [x] 自動的にログイン(バックエンド)
- [x] macOS メニューバー対応
- [ ] マルチプラットフォーム対応
- [x] Macアプリケーションとしてバイナリ化

## 使い方
1. プロジェクトをクローン(Clone)し、もしくは右上の「Download」ボタンよりZIPファイルをダウンロードしてください。
2. パッケージ ```rumps``` と ```requests``` をインストールしてください。pipでインストールするのはオススメである。

    ```shell
    pip install rumps
    pip install requests
    ```

3. ```RitsuWiFi.py``` にある「Setting Area」で自分とのユーザネームとパスワードを編集してください。
    - __配置の例__
    
    ```python
    # ---------------------------------------
    # Setting Area
    # ---------------------------------------
    wifiName = "Rits-Webauth"
    loginPagePath = "https://webauth.ritsumei.ac.jp"

    myUsername = "is1234rj"
    myPassword = "12345678"
    ```
4. ターミナルアプリで ```python RitsuWiFi.py``` を実行する。

## Macアプリとしてバイナリ化
RitsuWiFi をバイナリ化にしたい場合、下の手順に従って作成できる。

- .app ファイルの生成にアイコンファイル(logo.icns)が必要である。
- RitsuWiFi がうまく動いていることを確認した上、Buildしてください。
- Alias機能を使う必要があるので、```-A``` コマンドを追加してください。

1. パッケージ ```py2app``` をインストールしてください。

    ```shell
    pip install py2app
    ```
2. コンパイルする前に```rm -rf dist build``` を実行し、ビルドフォルダの整理は推奨である。
3. ターミナルアプリで ```python setup.py py2app -A``` を実行してください。