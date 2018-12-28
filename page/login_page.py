import allure

from base.base_action import BaseAction
import page


class LoginPage(BaseAction):
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('登录逻辑')
    def login_in(self, name, pwd):
        allure.attach('登录', '请输入账号')
        self.input_element_content(page.login_username_id,name)
        allure.attach('登录', '请输入密码')
        self.input_element_content(page.login_password_id,pwd)
        allure.attach('登录', '点击登录按钮')
        self.click_element(page.login_login_in_btn)

    def close_login_page(self):
        self.click_element(page.login_login_out_btn)



