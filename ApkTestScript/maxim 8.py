# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.taxsee.taxsee'
desired_caps['appActivity'] = '.ui.activities.SplashScreen'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)



'''
requires the page in the main page
'''

el = driver.find_element_by_android_uiautomator("new UiSelector().text(\"GORI\")")
el.click()


driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.taxsee.taxsee",
  "appActivity": ".ui.activities.SplashScreen"
}
'''