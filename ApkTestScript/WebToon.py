# -*- coding:utf8 -*-

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.naver.linewebtoon'
desired_caps['appActivity'] = '.splash.SplashActivity'
desired_caps['newCommandTimeout'] = '1000'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(18)


# download page
el = driver.find_element_by_android_uiautomator("new UiSelector().text(\"63 Episode 63\")")
el.click()

el = driver.find_elements_by_class_name("android.widget.TextView")[0]
el.click()

driver.quit()


'''
{
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "noReset": true,
  "appPackage": "com.naver.linewebtoon",
  "appActivity": ".splash.SplashActivity"
}
'''