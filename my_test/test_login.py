import time
import allure
import pytest
from illegal_traffic.base.base_driver import InitDriver
from illegal_traffic.base.base_excel import read_excel
from illegal_traffic.page.page import Page


class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.driver = InitDriver().get_driver()
        cls.page = Page(cls.driver)
        cls.driver.get("http://10.10.29.161/#/login")

    def setup(self):
        time.sleep(1)
        self.driver.get("http://10.10.29.161/#/login")

    def teardown(self):
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        InitDriver().quit_driver()

    @pytest.mark.order("10")
    @pytest.mark.parametrize("args",read_excel("test_data.xlsx", "login"))
    def test_login(self,args):
        username = args[0]
        passwd = args[1]
        massege = args[2]
        depict = args[3]
        if_success = args[4]
        allure.attach("测试标题", depict, allure.attach_type.TEXT)
        self.page.login.input_username(username)
        self.page.login.input_passwd(passwd)
        self.page.login.click_login_btn()
        time.sleep(1)

        if if_success == "fail":
            time.sleep(1)
            alert_message = self.page.login.get_massege()
            assert massege in alert_message
        if if_success == "success":
            time.sleep(2)
            title = self.page.home_page.get_title_msg()
            assert massege == title



