import os, sys
sys.path.append(os.getcwd())
import pytest
from page.navigation_page import NavigationPage
from base.base_driver import init_driver
import time
from base.read_yaml_data import read_yaml_data
import page

def get_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")
        passwd = data2.get("password")
        data_list.append((name, passwd))
    return data_list


class TestLogin:

    def setup_class(self):
        self.driver = init_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navigation_page = NavigationPage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("username,password", get_data())
    def test_login(self, username, password):
        time.sleep(5)
        # 点击我的
        self.navigation_page.get_home_page_obj().click_my_button()
        # 点击已有账号
        self.navigation_page.get_sign_in_page_obj().click_exist_accout()
        # 输入用户名,密码
        self.navigation_page.get_login_page_obj().login_in(username,password)
        toast_text = self.navigation_page.get_sign_in_page_obj().find_element(page.toast)
        print(toast_text.text)

