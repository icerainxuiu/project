import json
import logging
import unittest
import time

from parameterized import parameterized
from selenium.webdriver.common.by import By


from config import BASE_DIR
from page.device_management import DeviceManagementProxy
from utils import DriverUtil, exist_text


def build_select_data():
    test_data = []
    with open(BASE_DIR + "/data/data_select.json", 'r', encoding='utf8') as f:
        json_data = json.load(f)
        for list_select in json_data:
            test_data.append((list_select.get('device_name'),
                              list_select.get('device_ip'),
                              list_select.get('device_sn')))
    print(json_data)
    return test_data

class TestDeviceSelect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.device_management_proxy = DeviceManagementProxy()

    def setUp(self):
        self.driver.get("http://192.168.40.15/pages/home/index.html")
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.find_element(By.ID, 'btnLogin').click()

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    @parameterized.expand(build_select_data)
    def test_select(self, device_name, device_ip, device_sn):
        logging.info("device_name={}, device_ip={}, device_sn={}".format(device_name, device_ip, device_sn))
        self.device_management_proxy.select_test(device_name, device_ip, device_sn)
        time.sleep(2)
        try:
            self.assertTrue(exist_text(device_name))
        except Exception as e:
            img_path = "./img{}.png".format(time.strftime("%Y%m%d%H%M%D"))
            self.driver.get_screenshot_as_file(img_path)
            raise e