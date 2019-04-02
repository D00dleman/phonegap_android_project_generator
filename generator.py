import sys
import os
from PIL import Image

projFolder = sys.argv[1]

cfg = """<?xml version='1.0' encoding='utf-8'?>
<widget id="appId" version="appVersion" xmlns="http://www.w3.org/ns/widgets" xmlns:gap="http://phonegap.com/ns/1.0">
    <name>appName</name>
    <description>appDescription</description>
    <author email="authorEmail">authorName</author>
    <content src="index.html" />
    <preference name="DisallowOverscroll" value="true" />
    <preference name="android-minSdkVersion" value="appMinSdkVersion" />
    <preference name="android-targetSdkVersion" value="appTargetSdkVersion" />
    <preference name="orientation" value="appOrientation" />
    <preference name="fullscreen" value="appFullscreen" />
  
    <platform name="android">
        <icon density="ldpi" src="www/res/icon/android/drawable-ldpi-icon.png" />
        <icon density="mdpi" src="www/res/icon/android/drawable-mdpi-icon.png" />
        <icon density="hdpi" src="www/res/icon/android/drawable-hdpi-icon.png" />
        <icon density="xhdpi" src="www/res/icon/android/drawable-xhdpi-icon.png" />
        <icon density="xxhdpi" src="www/res/icon/android/drawable-xxhdpi-icon.png" />
        <icon density="xxxhdpi" src="www/res/icon/android/drawable-xxxhdpi-icon.png" />
        <splash density="land-ldpi" src="www/res/screen/android/drawable-land-ldpi-screen.png" />
        <splash density="land-mdpi" src="www/res/screen/android/drawable-land-mdpi-screen.png" />
        <splash density="land-hdpi" src="www/res/screen/android/drawable-land-hdpi-screen.png" />
        <splash density="land-xhdpi" src="www/res/screen/android/drawable-land-xhdpi-screen.png" />
        <splash density="land-xxhdpi" src="www/res/screen/android/drawable-land-xxhdpi-screen.png" />
        <splash density="land-xxxhdpi" src="www/res/screen/android/drawable-land-xxxhdpi-screen.png" />
        <splash density="port-ldpi" src="www/res/screen/android/drawable-port-ldpi-screen.png" />
        <splash density="port-mdpi" src="www/res/screen/android/drawable-port-mdpi-screen.png" />
        <splash density="port-hdpi" src="www/res/screen/android/drawable-port-hdpi-screen.png" />
        <splash density="port-xhdpi" src="www/res/screen/android/drawable-port-xhdpi-screen.png" />
        <splash density="port-xxhdpi" src="www/res/screen/android/drawable-port-xxhdpi-screen.png" />
        <splash density="port-xxxhdpi" src="www/res/screen/android/drawable-port-xxxhdpi-screen.png" />
    </platform>
    <access origin="*" />
    <allow-intent href="http://*/*" />
    <allow-intent href="https://*/*" />
    <allow-intent href="tel:*" />
    <allow-intent href="sms:*" />
    <allow-intent href="mailto:*" />
    <allow-intent href="geo:*" />
    <preference name="permissions" value="none"/>
    <platform name="android">
        <allow-intent href="market:*" />
    </platform>
    <platform name="ios">
        <allow-intent href="itms:*" />
        <allow-intent href="itms-apps:*" />
    </platform>
</widget>
"""

icons = [['www/res/icon/android/drawable-hdpi-icon.png', 71, 72],
['www/res/icon/android/drawable-mdpi-icon.png', 48, 48],
['www/res/icon/android/drawable-ldpi-icon.png', 36, 36],
['www/res/icon/android/drawable-xxhdpi-icon.png', 142, 144],
['www/res/icon/android/drawable-xhdpi-icon.png', 95, 96],
['www/res/icon/android/drawable-xxxhdpi-icon.png', 189, 192]]



config = {}

projFolder = sys.argv[1] 

print('Enter project name')
config['appName'] = input(':')

print('Enter project id. Example "com.example.example".')
config['appId'] = input(':')

print('Enter version.')
config['appVersion'] = input(':')

print('Enter email.')
config['authorEmail'] = input(':')

print('Enter author name.')
config['authorName'] = input(':')

print('Enter android minSdkVersion.')
config['appMinSdkVersion'] = input(':')

print('Enter android targetSdkVersion.')
config['appTargetSdkVersion'] = input(':')

print('Enter orientation  (p)ortrait or (l)andscape.')
config['appOrientation'] = input(':')

if(config['appOrientation'] == 'p'):
  config['appOrientation'] = 'portrait'
else:
  config['appOrientation'] = 'landscape'

print('Fullscreen (t)rue or (f)alse.')
config['appFullscreen'] = input(':')

if(config['appFullscreen'] == 't'):
  config['appFullscreen'] = 'true'
else:
  config['appFullscreen'] = 'false'

print('Enter descriprion.')
config['appDescription'] = input(':')

for i in config.keys():
  cfg = cfg.replace(i, config[i]) 

os.system('mkdir -p ' + config['appName'] + '/www/res/icon')
os.system('mkdir  ' + config['appName'] + '/www/res/icon/android')
os.system('mkdir  ' + config['appName'] + '/www/res/icon/ios')
os.system('mkdir  ' + config['appName'] + '/www/res/icon/windows')
os.system('mkdir  ' + config['appName'] + '/www/res/icon/wp8')

conf = open(config['appName'] + '/config.xml', 'w')
conf.write(cfg)
conf.close()

for i in icons:
    icon = Image.open(projFolder + 'icon.png')
    icon.thumbnail((i[1], i[2]))
    icon.save(config['appName'] + '/' + i[0])

os.system('cp ' + projFolder + '* ' + config['appName'] + '/www/')
os.system('cd ' + config['appName'] + '; zip ../' + config['appName'] + ' -r *')