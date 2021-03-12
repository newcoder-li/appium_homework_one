# -*- coding: utf-8 -*-
from appium_test.page.addmember_page import AddmemberPage
from appium_test.page.base_page import BasePage


class ChooseAddmemberWayPage(BasePage):
    def choose_manual_way(self):
        # 加载页面操作
        self.steps("../data/choose_manual_way_step.yaml")
        return AddmemberPage(self.driver)