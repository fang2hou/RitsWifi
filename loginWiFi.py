#!/usr/bin/python
# -------------------------
# Login WiFi
# for Ritsumeikan Univ.
# Author: Fang2hou
import os
import platform
import commands
import requests

wifiName = "Rits-Webauth"
loginPagePath = "https://webauth.ritsumei.ac.jp"

myUsername = ""
myPassword = ""

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
		systemOutput = commands.getoutput("/System/Library/PrivateFrameworks/Apple8*/Versions/A/Resources/airport -I | grep SSID")
		if wifiName in systemOutput:
			return True
		else:
			return False
# End of isSSIDConnected()

def getNetworkStatus():
	statusText = requests.get("http://httpbin.org/ip");
	if "\"origin\":" in statusText:
		return "out"
	else:
		return "in"
# End of getStatus()	

def loginWifi():
	account = {'username': myUsername, 'password': myPassword}
	resultText = requests.post(loginPagePath + "/login.html", data=account)
	return resultText

operatingSystem = getOperatingSystem()
isConnected = isSSIDConnected(operatingSystem)
if isConnected:
	# if getNetworkStatus() == "in":
	print loginWifi()