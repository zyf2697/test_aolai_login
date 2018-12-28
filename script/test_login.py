import os, sys
sys.path.append(os.getcwd())
import pytest
from page.navigation_page import NavigationPage
from base.base_driver import init_driver
import time
from base.read_yaml_data import read_yaml_data


def get_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")
        passwd = data2.get("password")
        tag = data2.get("tag")
        except_msg = data2.get("except_msg")
        get_toast_msg = data2.get("get_toast_msg")
        data_list.append((name, passwd, tag, get_toast_msg, except_msg))
    print(data_list)
    return data_list


class TestLogin:

    def setup_class(self):
        self.driver = init_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navigation_page = NavigationPage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    # @pytest.mark.parametrize("username,password", get_data())
    # def test_login(self, username, password):
    #     time.sleep(2)
    #     # 点击我的
    #     self.navigation_page.get_home_page_obj().click_my_button()
    #     # 点击已有账号
    #     self.navigation_page.get_sign_in_page_obj().click_exist_accout()
    #     # 输入用户名,密码
    #     self.navigation_page.get_login_page_obj().login_in(username,password)
    #     # 进入个人中心 点击设置
    #     self.navigation_page.get_person_center_page_obj().click_person_center_setting()
    #     # 点击退出
    #     self.navigation_page.get_setting_page_obj().logout_accout()

    # @pytest.mark.parametrize("username, password,tag, get_toast_msg, except_msg", get_data())
    # def test_login2(self, username, password,tag,get_toast_msg, except_msg):
    #     time.sleep(2)
    #     # 点击我的
    #     self.navigation_page.get_home_page_obj().click_my_button()
    #     # 点击已有账号
    #     self.navigation_page.get_sign_in_page_obj().click_exist_accout()
    #     # 输入用户名,密码
    #     self.navigation_page.get_login_page_obj().login_in(username,password)
    #     # 获取真正弹出吐司的消息
    #     toast_msg = self.navigation_page.get_person_center_page_obj().get_toast_message(get_toast_msg)
    #     print(toast_msg)
    #     assert toast_msg == except_msg
    #     # 点击退出
    #     self.navigation_page.get_login_page_obj().close_login_page()

    @pytest.mark.parametrize("username, password, tag, get_toast_msg, except_msg", get_data())
    def test_login(self, username, password,tag, get_toast_msg, except_msg):
        # 点击我的
        self.navigation_page.get_home_page_obj().click_my_button()
        # 点击已有账号
        self.navigation_page.get_sign_in_page_obj().click_exist_accout()
        # 输入用户名,密码
        self.navigation_page.get_login_page_obj().login_in(username,password)
        if tag == 1:
            try:
                login_state = self.navigation_page.get_person_center_page_obj().is_login_success()
                # 进入个人中心 点击设置
                self.navigation_page.get_person_center_page_obj().click_person_center_setting()
                # 点击退出
                self.navigation_page.get_setting_page_obj().logout_accout()
                assert login_state, self.navigation_page.get_person_center_page_obj().get_screen()
            except:
                # 6.截图 在哪一个页面出现的问题
                self.navigation_page.get_person_center_page_obj().get_screen()
                self.navigation_page.get_login_page_obj().close_login_page()
        else:
            try:
                toast_message = self.navigation_page.get_person_center_page_obj().get_toast_message(get_toast_msg)
                assert toast_message == except_msg, self.navigation_page.get_person_center_page_obj().get_screen()
            finally:
                # 5.关闭当前登录页面
                self.navigation_page.get_login_page_obj().close_login_page()