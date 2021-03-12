# -*- coding: utf-8 -*-

import pytest
import yaml
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_test.page.base_page import BasePage
from appium_test.page.contract_list_page import ContractListPage


class MainPage(BasePage):
    # 前往联系人页
    def goto_contract_list_page(self):
        # 加载页面操作
        self.steps('../data/message_step.yaml')
        return ContractListPage(self.driver)