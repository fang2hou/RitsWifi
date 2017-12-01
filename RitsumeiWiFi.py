#! python3
# coding: utf-8
# -------------------------
# RitsumeiWiFi
# for Ritsumeikan Univ.
# Author: Zhou Fang (is0385rx@ed.ritsumei.ac.jp)
import os
import rumps
import platform
import subprocess
import requests
# ---------------------------------------
# Setting Area
# ---------------------------------------
wifiName = "Rits-Webauth"
loginPagePath = "https://webauth.ritsumei.ac.jp"

myUsername = "Your username"
myPassword = "Your password"
# ---------------------------------------
# Functions
# ---------------------------------------
def getOperatingSystem():
	platformText = platform.platform()
	if "Darwin" in platformText:
		return "macOS"
	elif "Windows" in platformText:
		return "Windows"
	else:
		return "Linux"
# End of getOperatingSystem()

def isSSIDConnected(operatingSystem):
	if operatingSystem == "macOS":
		systemOutput = str(subprocess.Popen("/System/Library/PrivateFrameworks/Apple8*/Versions/A/Resources/airport -I | grep SSID", shell=True, stdout=subprocess.PIPE).stdout.read())
		if wifiName in systemOutput:
			return True
		else:
			return False
# End of isSSIDConnected()

def getNetworkStatus():
	statusText = requests.get("http://httpbin.org/ip");
	if "\"origin\":" in statusText.text:
		return "outer"
	else:
		return "inner"
# End of getStatus()

def loginWifi():
	account = {'username': myUsername, 'password': myPassword, 'buttonClicked': "4", 'redirect_url': "", 'err_flag': "0"}
	resultText = requests.post(loginPagePath + "/login.html", data=account).text
	
	# Error text is same as Cisco Wi-Fi Network login page
	if "Login Successful" in resultText:
		return "Success"
	elif "statusCode=1" in resultText:
		return "Error - You are already logged in. No further action is required on your part."
	elif "statusCode=2" in resultText:
		return "Error - You are not configured to authenticate against web portal. No further action is required on your part."
	elif "statusCode=3" in resultText:
		return "Error - The username specified cannot be used at this time. Perhaps the username is already logged into the system?"
	elif "statusCode=4" in resultText:
		return "Error - The User has been excluded. Please contact the administrator."
	elif "statusCode=5" in resultText:
		return "Error - Invalid User ID and password. Please try again."
	else:
		return "Error - Unknown issue"
# End of loginWifi()

def mainStatus():
	if isConnected:
		if "outer" in getNetworkStatus():
			return loginWifi()
		else:
			return "You logged in Wi-Fi!"
	else:
		return "Please connect to \"Rits-Webauth\"!"
# End of mainStatus()

class macOSMenuBar(rumps.App):
	def __init__(self):
  		super(macOSMenuBar, self).__init__("RitsumeiWifi", icon="icon.png")
  		self.menu = ["Auto-Login(test)", "Connect", "Disconnect", "About"]

	@rumps.clicked('Connect')
	def btn_connect(self, _):
		rumps.alert(title="Connect information", message=mainStatus())

	# @rumps.clicked('Auto-Login(test)')
	# def btn_disconnect(self, sender):
		# sender.state = not sender.state

	@rumps.clicked('About')
	def btn_about(self, _):
		rumps.alert(title="About", message="Current Version: 0.1 Beta (Python)\n\nAuthor List:\nFang Zhou (is0385rx@ed.ritsumei.ac.jp)")
# ---------------------------------------
operatingSystem = getOperatingSystem()
isConnected = isSSIDConnected(operatingSystem)

if __name__ == "__main__" and operatingSystem == "macOS":
    macOSMenuBar().run()