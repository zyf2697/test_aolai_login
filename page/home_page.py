import allure

from base.base_action import BaseAction
import page


class HomePage(BaseAction):

    #
    def __init__(self,driver):
        BaseAction.__init__(self, driver)

    @allure.step('点击我的')
    def click_my_button(self):
        self.click_element(page.home_my_button)