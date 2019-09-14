import json

from selenium import webdriver

from config import BASE_DIR


def load_test_data(file_name):
    with open(BASE_DIR + "/data" + format(file_name), 'r', encoding='utf-8') as f:
        return json.load(f)


def exist_text(text):  # 判断页面是否有指定文本内容，用来断言
    try:
        xpath = '//*[contains(text(),"{}")]'.format(text)
        element = DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element is not None
    except:
        print("current page is not contains[{}]".format(text))
        return False


class DriverUtil:
    _driver = None  # 定义类属性保存驱动对象
    _auto_quit = True

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def set_auto_quit(cls, auto_quit):
        cls._auto_quit = auto_quit

    @classmethod
    def quit_driver(cls):
        if cls.set_auto_quit and cls._driver is not None:
            cls._driver.quit()
            cls._driver = None









