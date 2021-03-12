# -*- coding: utf-8 -*-
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._params = {}
        self.driver = driver

    # 查找元素封装
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 显示等待方法
    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    # 页面执行动作
    def steps(self, path):
        with open(path, encoding="UTF-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if 'wait' == step["action"]:
                        self.wait_for_click(5, step["locator"])
                    if "send" == step["action"]:
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        element.send_keys(content)

    # 滑动点击操作
    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    # 获取toast提示
    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result
