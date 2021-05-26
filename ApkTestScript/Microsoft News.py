# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.microsoft.amp.apps.bingnews'
desired_caps['appActivity'] = 'microsoft.msn.news.android.activities.LaunchActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

# edition page; scroll to the page end
el = driver.find_elements_by_id("com.microsoft.amp.apps.bingnews:id/setting_name")[-4]
el.click()

driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.microsoft.amp.apps.bingnews",
  "appActivity": "microsoft.msn.news.android.activities.LaunchActivity"
}
'''