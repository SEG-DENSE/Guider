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
make sure the screen is under the screen "share"
'''

# test action 3 edit on message
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

# after updated: com.google.android.apps.docs:id/add_collaborator_chips_textbox
el = driver.find_element_by_id("com.google.android.apps.docs:id/collaborator_recipient_text_view")
el.send_keys("people 1")

# after updated: com.google.android.apps.docs:id/add_collaborator_message
el = driver.find_element_by_id("com.google.android.apps.docs:id/message")
el.send_keys("message 1")

# ......

driver.quit()
