# RitsWiFi
Get better experience with free WiFi service in Ritsumeikan University.

***Just can be used in Ritsumeikan University***

[English](https://github.com/fang2hou/RitsWifi) | [日本語](https://github.com/fang2hou/RitsWifi/blob/master/extra/Readme.ja-JP.md) | [简体中文](https://github.com/fang2hou/RitsWifi/blob/master/extra/Readme.zh-CN.md)

## Preview
<img src="https://cdn.rawgit.com/fang2hou/RitsWiFi/master/extra/example.png" width="250px"/>

## Requirements
**Python Version**: 2.6+ / 3.3+

**Python 3 is recommended.** If you try to build and use RitsWiFi with Python 2, please use `pip` and `python` instead of `pip3` and `python3`.

**Additional Library**: ```requests```, ```rumps```

## How to use
1. Clone this repo, or just download the zip file directly from github.
2. Install package ```rumps``` and ```requests```. For most people, installation via pip is recommended.
    ```shell
    pip3 install rumps
    pip3 install requests
    ```

3. Edit ```RitsWiFi.py``` to add your RAINBOW ID and password.  
__Example below__
    ```python
    # ---------------------------------------
    # Setting Area
    # ---------------------------------------
    wifiName = "Rits-Webauth"
    loginPagePath = "https://webauth.ritsumei.ac.jp"

    myUsername = "is1234rj"
    myPassword = "12345678"
    ```
4. Run `python3 RitsWiFi.py` in Terminal.

## Build as standalone application
If you wanna get a standalone version of RitsWiFi, here is the solution.

- The standalone application will be created with the icon file (logo.icns).
- **Notice**: Build standalone version only if you have confirmed RitsWiFi works.
- Please use ```-A``` to build RitsWiFi using alias.

1. Install package ```py2app```.  
    ```shell
    pip3 install py2app
    ```
2. Before building, use `rm -rf dist build` to clean up the build folder is better.
3. Run `python3 setup.py py2app -A` in Terminal.
