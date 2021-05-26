# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'org.mozilla.firefox'
desired_caps['appActivity'] = '.App'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)


# home page
el = driver.find_element_by_id("org.mozilla.firefox:id/tabs")
el.click()

el = driver.find_element_by_accessibility_id("Private")
el.click()


driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "org.mozilla.firefox",
  "appActivity": ".App"
}
'''