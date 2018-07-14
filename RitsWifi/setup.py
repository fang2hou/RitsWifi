from setuptools import setup

APP = ['RitsuWiFi.py']
APP_NAME = 'RitsuWiFi'
DATA_FILES = ['icon.png']
OPTIONS = {
	'argv_emulation': True, 
	'plist': {
		'LSUIElement': True,
	},
	'iconfile': 'logo.icns',
	'strip': False,
	'includes': ['os','rumps','platform','subprocess','requests','threading','time'],
	'packages': ['requests'],
}

setup(
	app=APP,
	data_files=DATA_FILES,
	options={'py2app': OPTIONS},
	setup_requires=['py2app'],
)