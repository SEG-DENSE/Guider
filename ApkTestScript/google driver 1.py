# -*- coding:utf8 -*-

import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import sys
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['platformVersion'] = '7.0'
#desired_caps['automationName'] = 'UIAutomator2'
desired_caps['deviceName'] = 'emulator-5554'

desired_caps['appPackage'] = 'com.google.android.apps.docs'
desired_caps['appActivity'] = 'com.google.android.apps.docs.app.NewMainProxyActivity'
#desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True
'''
make sure the screen is under the screen "file"
'''

# test action 1 click on more options
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

el = driver.find_element_by_accessibility_id("More actions for paperRecord")
el.click()

# ......

driver.quit()
