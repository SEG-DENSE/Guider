# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'codematics.universal.tv.remote.control'
desired_caps['appActivity'] = '._FirstScreen'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

'''
config the page in the home page
'''
a = driver.page_source
el = driver.find_elements_by_class_name("android.widget.ImageView")[-2]
el.click()

driver.quit()

'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "codematics.universal.tv.remote.control",
  "appActivity": "._FirstScreen"
}
'''