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
desired_caps['appPackage'] = 'com.google.android.apps.walletnfcrel'
desired_caps['appActivity'] = 'com.google.commerce.tapandpay.android.cardlist.CardListActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

# 该APP不登入就闪退，在登入了Google账户后的主界面。
el = driver.find_elements_by_class_name("android.widget.TextView")[1]
el.click()

driver.quit()

'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.google.android.apps.walletnfcrel",
  "appActivity": "com.google.commerce.tapandpay.android.cardlist.CardListActivity"
}
'''