import allure

from base.base_action import BaseAction
import page


class SettingPage(BaseAction):
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('退出账号')
    def logout_accout(self):
        allure.attach('退出账号', '向上滑动')
        self.swipe_screen(1)
        allure.attach('退出账号', '点击退出按钮')
        self.click_element(page.setting_center_login_out_btn)
        allure.attach('退出账号', '点击确认按钮')
        self.click_element(page.setting_center_login_dialog_confirm_btn)




