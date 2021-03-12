# -*- coding: utf-8 -*-
from appium_test.page.base_page import BasePage


class AddmemberPage(BasePage):
    def input_information(self, name, phone):
        # 将name、phone赋值给steps中的send方法
        self._params["value"] = name
        self._params["value2"] = phone
        # 加载添加成员动作
        self.steps("../data/addmember_step.yaml")
        # 返回toast值
        return self.get_toast_text()
