# -*- coding:utf8 -*-

import time
from appium import webdriver

# com.google.android.apps.fitness
# com.google.android.apps.fitness.welcome.WelcomeActivity
# com.google.android.apps.fitness.shared.account.selector.FitSelectAccountActivity

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.google.android.apps.fitness'
desired_caps['appActivity'] = '.welcome.WelcomeActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

'''
require the page in the time setting page
'''

el = driver.find_elements_by_id("android:id/numberpicker_input")[1]
el.click()
driver.quit()

'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.google.android.apps.fitness",
  "appActivity": ".welcome.WelcomeActivity"
}
'''
