# -*- coding: utf-8 -*-
# @Author  : lidonghui
import pytest
import yaml

from appium_test.page.start import Start


class TestAddmember:
    def setup(self):
        # 实例化start方法
        self.start = Start()

    def teardown(self):
        self.start.driver.quit()

    @pytest.mark.parametrize("name, phone", yaml.safe_load(open(r"../data/contract_add.yaml", encoding="UTF-8")))
    def test_add_contact(self, name, phone):
        # 链式调用添加联系人，并将添加结果toast值返回给result
        result =self.start.goto_main().goto_contract_list_page().add_member().choose_manual_way().input_information(name, phone)
        assert "添加成功" == result