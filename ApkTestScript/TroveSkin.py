# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.trove'
desired_caps['appActivity'] = '.activities.MainActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True
#desired_caps["automationName"] = "uiautomator2"


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)


'''
requires the page in the face analyze page
'''
el = driver.find_elements_by_class_name("android.widget.ImageView")[-1]
el.click()

driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.trove",
  "appActivity": ".activities.MainActivity"
}
'''