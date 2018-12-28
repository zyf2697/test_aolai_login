import allure

from base.base_action import BaseAction
import page


class SignInPage(BaseAction):
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('点击已有账号')
    def click_exist_accout(self):
        self.click_element(page.sign_in_exit_account_id)




