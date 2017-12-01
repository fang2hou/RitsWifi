from setuptools import setup

APP = ['RitsumeiWiFi.py']
APP_NAME = 'RitsumeiWiFi'
DATA_FILES = ['icon.png']
OPTIONS = {
	'argv_emulation': False, 
	'plist': {
		'LSUIElement': True,
	},
	'iconfile': 'logo.icns',
	'includes': ['rumps','requests','os','platform','subprocess'],
}

setup(
	app=APP,
	data_files=DATA_FILES,
	options={'py2app': OPTIONS},
	setup_requires=['py2app'],
)