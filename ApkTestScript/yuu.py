# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.yuurewards.app'
desired_caps['appActivity'] = 'com.dfg.anfield.activity.SplashActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)


'''
requires the page in the reward page

'''

el = driver.find_elements_by_class_name("android.widget.ImageView")[0]
el.click()

driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.yuurewards.app",
  "appActivity": "com.dfg.anfield.activity.SplashActivity"
}
'''