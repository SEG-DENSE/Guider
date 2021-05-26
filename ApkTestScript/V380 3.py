# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.macrovideo.v380pro'
desired_caps['appActivity'] = '.activities.LaunchActivityOverseaNew'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)


# test case 1 click on single;requirement: in the screen add camera

el = driver.find_element_by_id("com.macrovideo.v380pro:id/tv_single_camera")
el.click()


driver.quit()




'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.macrovideo.v380pro",
  "appActivity": ".activities.LaunchActivityOverseaNew"
}
'''