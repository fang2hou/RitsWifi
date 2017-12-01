# RitsuWiFi
無線LANの接続をより便利にしよう。

***立命館大学で利用可能***

[English](https://github.com/fang2hou/RitsuWifi/blob/master/ReadMe.md)| [日本語](https://github.com/fang2hou/RitsuWifi/blob/master/ReadMe.ja_JP.md) | [简体中文](https://github.com/fang2hou/RitsuWifi/blob/master/ReadMe.zh_CN.md)

## プレビュー
<img src="https://cdn.rawgit.com/fang2hou/RitsuWiFi/master/ExampleImages/Main.png" width="250px"/>

## 準備
___Python___: 2.6以降 または 3.3以降

Python 2.7 & 3.6 で RitsuWiFi の実行テストを行う。

macOS Python 3.X で RitsuWiFi を実行する場合、```pip3``` と ```python3``` を活用してください。

___利用したライブラリ___: ```requests```, ```rumps```
## TODO
- [x] POSTでのログイン
- [x] 自動的にログイン
- [x] macOS メニューバー対応
- [ ] マルチプラットフォーム対応
- [x] Macアプリケーションとしてバイナリ化

## 使い方
1. プロジェクトをクローン(Clone)し, もしくは右上の“Download”ボタンよりZIPファイルをダウンロードしてください。
2. パッケージ ```rumps``` と ```requests``` をインストールしてください。pipでインストールするのはオススメである。

    ```shell
    pip install rumps
    pip install requests
    ```

3. ```RitsuWiFi.py``` にユーザネームとパスワードの部分を編集し、保存する。
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
RitsuWiFi をバイナリ化にしたい場合、下の手順で作成できる。

- .app ファイルの生成にアイコン logo.icns が必要である。
- RitsuWiFi がうまく動いていることを確認した上、Buildしてください。
- Alias機能を使う必要があるので、```-A``` コマンドを追加してください。

1. パッケージ ```py2app``` をインストールしてください。。

    ```shell
    pip install py2app
    ```
2. コンパイルする前に ```rm -rf dist build``` を実行し、フォルダにあるファイルの整理は推奨である。
3. ターミナルアプリで ```python setup.py py2app -A``` を実行してください。