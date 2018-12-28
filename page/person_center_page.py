import allure

from base.base_action import BaseAction
import page


class PersonCenterPage(BaseAction):
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('进入个人中心设置页面')
    def click_person_center_setting(self):
        self.click_element(page.person_center_setting_btn)

    @allure.step('判断是否登录成功')
    def is_login_success(self):
        try:
            allure.attach('个人中心', '找到全部订单,说明登录成功')
            self.find_element(page.person_center_all_order)
            return True
        except:
            return False



