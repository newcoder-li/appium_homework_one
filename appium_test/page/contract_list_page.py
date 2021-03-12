# -*- coding: utf-8 -*-
from appium_test.page.base_page import BasePage
from appium_test.page.choose_addmember_way_page import ChooseAddmemberWayPage


class ContractListPage(BasePage):
    def add_member(self):
        # 滑动点击操作
        self.swip_click("添加成员")
        return ChooseAddmemberWayPage(self.driver)
