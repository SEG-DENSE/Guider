# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.google.android.youtube'
desired_caps['appActivity'] = '.app.honeycomb.Shell$HomeActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

# home page
el = driver.find_element_by_accessibility_id("Impossible Challenge S2 20161218 Basketball Shooting & Brain Wave Control | CCTV - 1 hour, 37 minutes - Go to channel - CCTV中国中央电视台 - 1.5M views - 4 years ago - play video")
el.click()

driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.google.android.youtube",
  "appActivity": ".app.honeycomb.Shell$HomeActivity"
}
'''