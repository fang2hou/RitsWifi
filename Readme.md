# RitsuWiFi
Make better experience in Ritsu-Auth WiFi login.

***Just can be used in Ritsumeikan University***
## Preview
<img src="https://cdn.rawgit.com/fang2hou/RitsuWiFi/master/ExampleImages/Main.png" width="250px"/>

## Requirement
___Python Version___: 2.6+ / 3.3+

RitsuWiFi is tested under Python 2.7 & 3.6.

___Addtional Library___: ```requests```, ```rumps```
## TODO
- [x] Login via post
- [x] Auto-login
- [x] macOS menubar feature
- [ ] Multi-platform support
- [x] Standalone build (Requests need installed)

## How to use
1. Clone this repo, or you can download the zip file via the button upper right.
2. Install package ```rumps``` and ```requests```. For most people, installation via pip is recommended.

    ```shell
    pip install rumps
    pip install requests
    ```

3. Edit ```RitsuWiFi.py``` to add your username and password.
    - __Example below__
    
    ```python
    # ---------------------------------------
    # Setting Area
    # ---------------------------------------
    wifiName = "Rits-Webauth"
    loginPagePath = "https://webauth.ritsumei.ac.jp"

    myUsername = "is1234rj"
    myPassword = "12345678"
    ```
4. Run ```python RitsuWiFi.py``` in Terminal.app or other terminal application you prefer.

## Build as standalone application
If you wanna get a standalone version of RitsuWiFi, here is the solution.

- The .app file will be created with the icon (logo.icns).
- You should build standalone version after you confirmed RitsuWiFi works.

1. Install package ```py2app```.

    ```shell
    pip install py2app
    ```
2. Before building, use ```rm -rf dist build``` to clean up the build folder is better.
3. Run ```python setup.py py2app``` in Terminal.app or other terminal application you prefer.
