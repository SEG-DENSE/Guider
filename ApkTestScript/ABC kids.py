# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.rvappstudios.abc_kids_toddler_tracing_phonics'
desired_caps['appActivity'] = 'com.unity3d.player.UnityPlayerActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)


# home page
driver.tap([(1700,980)])



driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.rvappstudios.abc_kids_toddler_tracing_phonics",
  "appActivity": "com.unity3d.player.UnityPlayerActivity"
}
'''