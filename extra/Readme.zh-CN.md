# RitsWiFi
优化立命馆的校内无线网络的体验。

***只能在立命馆大学使用***

[English](https://github.com/fang2hou/RitsWifi) | [日本語](https://github.com/fang2hou/RitsWifi/blob/master/extra/Readme.ja-JP.md) | [简体中文](https://github.com/fang2hou/RitsWifi/blob/master/extra/Readme.zh-CN.md)

## 预览
<img src="https://cdn.rawgit.com/fang2hou/RitsWiFi/master/extra/example.png" width="250px"/>

## 运行环境
**Python版本**: 2.6+ / 3.3+

**推荐使用 Python 3。** 如果一定要用 Python 请使用 `pip` 及 `python` 来替换 `pip3` 和 `python3`。

**第三方库**: `requests`, `rumps`

## 如何使用
1. 克隆(Clone)本项目, 或者你也可以通过右上方的下载按钮来获取zip压缩包。
2. 安装包 `rumps` 及 `requests`。对于大多数人来说，推荐通过pip来完成安装。

    ```shell
    pip3 install rumps
    pip3 install requests
    ```

3. 修改 ```RitsWiFi.py``` 来添加你的 RAINBOW 账号和密码。  
__举个例子__    
    ```python
    # ---------------------------------------
    # Setting Area
    # ---------------------------------------
    wifiName = "Rits-Webauth"
    loginPagePath = "https://webauth.ritsumei.ac.jp"

    myUsername = "is1234rj"
    myPassword = "12345678"
    ```
4. 在**终端**中执行 ```python3 RitsWiFi.py```。

## 编译成独立App
如果你想要一个独立App形式的 RitsWiFi，这里有一个解决方案。

- 创建 .app 文件时，会采用 logo.icns 来作为图标。
- **注意**: 请你务必在确认 RitsWiFi 能够正常工作后再将其编译成独立App。
- 请追加 ```-A``` 编译命令来启用别名模式

1. 安装包 ```py2app```。

    ```shell
    pip3 install py2app
    ```
2. 在编译之前, 建议执行 `rm -rf dist build` 来清理编译文件夹。
3. 在**终端**中执行 `python3 setup.py py2app -A`。