import allure
from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.burger_page import BurgerPage
from data_for_test.urls import Urls


class TestAcc:
    @allure.title("Личный кабинет")
    @allure.step("переход по клику на «Личный кабинет»")
    def test_switch_to_acc(self, driver):
        main_page  = MainPage(driver)
        main_page.personal_acc_open()
        assert main_page.get_page_url() == Urls.acc_url
    
    @allure.step("переход в раздел «История заказов»")
    def test_enter_to_order_history(self, driver, create_user_data):
        main_page  = MainPage(driver)
        burger_page = BurgerPage(driver)
        user_page = UserPage(driver)
        main_page.personal_acc_open()
        user_page.user_login(create_user_data)
        burger_page.ing_visible()
        main_page.personal_acc_open()
        user_page.user_orders_page_open()
        assert main_page.get_page_url() == Urls.userorder_url
        
    @allure.step("выход из аккаунта")
    def test_logout_from_acc(self, driver, create_user_data):
        main_page  = MainPage(driver)
        burger_page = BurgerPage(driver)
        user_page = UserPage(driver)
        main_page.personal_acc_open()
        user_page.user_login(create_user_data)
        burger_page.ing_visible()
        main_page.personal_acc_open()
        user_page.exit_of_user()
        user_page.enter_bttn_visible()
        assert main_page.get_page_url() == Urls.acc_logout_url

