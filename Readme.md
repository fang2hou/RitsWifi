# RitsuWiFi
Make better experience in Ritsu-Auth WiFi login.
***Just be used in Ritsumeikan University***
## How to use
1. Clone this repo, or you can download the zip file via the button upper right.
2. Install package ```rumps``` and ```requests```. For most people, installation via pip is recommended.
    ```shell
    pip install rumps
    pip install requests
    ```

3. Edit ```RitsumeiWiFi.py``` to add your username and password.
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
4. Run ```python RitsumeiWiFi.py``` in Terminal.app or other terminal application you prefer.

## Build as standalone application
If you wanna get a standalone version of RitsumeiWiFi, here is the solution.

- The .app file will be created with the icon (logo.icns).
- You should build standalone version after you confirmed RitsuWiFi works.

1. Install package ```py2app```.
    ```shell
    pip install py2app
    ```
2. Before building, use ```rm -rf dist build``` to clean up the build folder is better.
3. Run ```python setup.py py2app``` in Terminal.app or other terminal application you prefer.

