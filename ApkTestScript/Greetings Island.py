# -*- coding:utf8 -*-

import time
from appium import webdriver

# com.google.android.apps.walletnfcrel
# com.google.commerce.tapandpay.android.cardlist.CardListActivity
# com.google.android.apps.walletnfcrel.com.google.commerce.tapandpay.android.landingscreen.LandingScreenActivity

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.greetingsisland.sam'
desired_caps['appActivity'] = '.MainActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(40)

# 主页面有搜索框
driver.tap([(957,1697)])

driver.quit()

'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.greetingsisland.sam",
  "appActivity": ".MainActivity"
}
'''