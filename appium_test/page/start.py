# -*- coding: utf-8 -*-
from appium import webdriver

from appium_test.page.main_page import MainPage


class Start:
    # 初始化企业微信
    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            # 不清空缓存启动app
            'noReset': 'true',
            "autoGrantPermissions": "true"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待3s
        self.driver.implicitly_wait(3)

    # 前往首页
    def goto_main(self):
        return MainPage(self.driver)
