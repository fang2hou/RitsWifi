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
import threading
import time
# ---------------------------------------
# Setting Area
# ---------------------------------------
softVersion = "0.1.1 Beta"
wifiName = "Rits-Webauth"
loginPagePath = "https://webauth.ritsumei.ac.jp"

myUsername = "is0385rx"
myPassword = "fang1234"

autoDelay = 10
# ---------------------------------------
# Functions
# ---------------------------------------
def GetOperatingSystem():
	platformText = platform.platform()
	if "Darwin" in platformText:
		return "macOS"
	elif "Windows" in platformText:
		return "Windows"
	else:
		return "Linux"
# End of GetOperatingSystem()

def IsSSIDConnected(operatingSystem):
	if operatingSystem == "macOS":
		systemOutput = str(subprocess.Popen("/System/Library/PrivateFrameworks/Apple8*/Versions/A/Resources/airport -I | grep SSID", shell=True, stdout=subprocess.PIPE).stdout.read())
		if wifiName in systemOutput:
			return True
		else:
			return False
# End of IsSSIDConnected()

def GetNetworkStatus():
	statusText = requests.get("http://httpbin.org/ip");
	if "\"origin\":" in statusText.text:
		return "outer"
	else:
		return "inner"
# End of GetNetworkStatus()

def LogInWifi():
	loginData = {'username': myUsername, 'password': myPassword, 'buttonClicked': "4", 'redirect_url': "", 'err_flag': "0"}
	resultText = requests.post(loginPagePath + "/login.html", data=loginData).text
	
	# Error text is same as Cisco Wi-Fi Network login page
	if "Login Successful" in resultText:
		return "[Success] Connected."
	elif "statusCode=1" in resultText:
		return "[Error] You are already logged in. No further action is required on your part."
	elif "statusCode=2" in resultText:
		return "[Error] You are not configured to authenticate against web portal. No further action is required on your part."
	elif "statusCode=3" in resultText:
		return "[Error] The username specified cannot be used at this time. Perhaps the username is already logged into the system?"
	elif "statusCode=4" in resultText:
		return "[Error] The User has been excluded. Please contact the administrator."
	elif "statusCode=5" in resultText:
		return "[Error] Invalid User ID and password. Please try again."
	else:
		return "Error - Unknown issue"
# End of LogInWifi()

def LogOutWifi():
	loginData = {'userStatus': "1", 'err_msg': "", 'err_flag': "0"}
	resultText = requests.post(loginPagePath + "/logout.html", data=loginData).text
	if "To complete the log off process" in resultText:
		return "[Success] Disconnected."
	else:
		return "[Error] Unknown issue"
# End of LogOutWifi()

def Main(method):
	if IsSSIDConnected(operatingSystem):
		if "inner" in GetNetworkStatus():
			if method is "connect":
				return LogInWifi()
			elif method is "disconnect":
				return "You have not connected!"
		else:
			if method is "connect":
				return "You are connected"
			elif method is "disconnect":
				return LogOutWifi()
	else:
		return "Please connect to \"Rits-Webauth\"!"
# End of Main()
	
# End of AutoLogIn()
# ---------------------------------------
# Class Defination
# ---------------------------------------
class AutoLogInThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.isRunning = False

	def run(self):
		while self.isRunning:
			time.sleep(autoDelay)
			if self.isRunning and IsSSIDConnected(operatingSystem) and "inner" in GetNetworkStatus():
				LogInWifi()

	def stop(self):
		self.isRunning = False

# End of AutoLogInThread
class MacOSMenuBar(rumps.App):
	def __init__(self):
  		super(MacOSMenuBar, self).__init__("RitsuWifi", icon="icon.png",quit_button=rumps.MenuItem('Quit RitsuWiFi', key='q'))
  		self.menu = ["Connect", "Disconnect", "Auto-login", "About", None, wifiName, softVersion, None, ]

	@rumps.clicked('Connect')
	def btn_connect(self, _):
		result = Main("connect")
		rumps.alert(title="Connect information", message=result)

	@rumps.clicked('Disconnect')
	def btn_disconnect(self, _):
		result = Main("disconnect")
		rumps.alert(title="Disconnect information", message=result)

	@rumps.clicked('Auto-login')
	def btn_auto(self, sender):
		if autoThread.isRunning:
			autoThread.stop()
		else:
			autoThread.isRunning = True
			autoThread.start()
			# rumps.alert(title="Auto-login", message="[Error] unable to start thread")
		sender.state = not sender.state

	@rumps.clicked('About')
	def btn_about(self, _):
		rumps.alert(title="About", message="Current Version: " + softVersion + "(Python)\n\nAuthor List:\nFang Zhou (is0385rx@ed.ritsumei.ac.jp)")
# ---------------------------------------
operatingSystem = GetOperatingSystem()
autoThread = AutoLogInThread(1,"Thread-1")
if __name__ == "__main__" and operatingSystem == "macOS":
    MacOSMenuBar().run()