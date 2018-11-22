# RitsWiFi
立命館大学無線 LAN への接続をより簡単に。

***立命館大学構内で利用可能***

[English](https://github.com/fang2hou/RitsWifi) | [日本語](https://github.com/fang2hou/RitsWifi/blob/master/extra/Readme.ja-JP.md) | [简体中文](https://github.com/fang2hou/RitsWifi/blob/master/extra/Readme.zh-CN.md)

## プレビュー
<img src="https://cdn.rawgit.com/fang2hou/RitsWiFi/master/extra/example.png" width="250px"/>

## 準備
**Python**: 2.6以降 / 3.3以降

**Python 3 はおすすめです。** もし Python 2 で実行もしくはコンパイルするとき、`pip3` と `python3`ではなく、 `pip` と `python` を使ってください。

**利用したライブラリ**: `requests`、`rumps`

## 使い方
1. プロジェクトをクローン(Clone)し、もしくは右上の「Download」ボタンより Zip ファイルをダウンロードします。
2. パッケージ `rumps` と `requests` をインストールしてください。pip経由でインストールするのは手軽いです。
    ```shell
    pip3 install rumps
    pip3 install requests
    ```

3. ```RitsWiFi.py``` にある「Setting Area」で自分との RAINBOW ID とパスワードを編集してください。
__設定の一例__
    ```python
    # ---------------------------------------
    # Setting Area
    # ---------------------------------------
    wifiName = "Rits-Webauth"
    loginPagePath = "https://webauth.ritsumei.ac.jp"

    myUsername = "is1234rj"
    myPassword = "12345678"
    ```
4. **ターミナル**で `python3 RitsWiFi.py` を実行することで RitsWiFi を起動します。

## Mac アプリにコンパイル
RitsWiFi をバイナリ化にしたい場合、下の手順に従って作成できます。

- アプリの生成にはアイコンファイル(logo.icns)が必要です。
- **注意**: RitsWiFi がうまく動いていることを確認した上、Buildしてください。
- Alias 機能を使う必要があるので、`-A` コマンドを追加してください。

1. パッケージ `py2app` をインストールしてください。
    ```shell
    pip3 install py2app
    ```
2. コンパイルする前に `rm -rf dist build` を実行し、ビルドフォルダの整理は推奨である。
3. **ターミナル**で `python3 setup.py py2app -A` を実行してください。