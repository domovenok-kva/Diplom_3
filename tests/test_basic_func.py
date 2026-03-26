import allure
from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.burger_page import BurgerPage
from data_for_test.urls import Urls


class TestBesicFunc:

    @allure.title("Проверка основного функционала")

    @allure.step("переход по клику на «Конструктор»")
    def test_click_on_constructor(self, driver):
        main_page  = MainPage(driver)
        main_page.constructor_open()
        assert main_page.get_page_url() == Urls.main_url

    @allure.step("переход по клику на «Лента заказов»")
    def test_click_on_order_tape(self, driver):
        main_page  = MainPage(driver)
        main_page.order_tape_open()
        assert main_page.get_page_url() == Urls.feed_url

    @allure.step("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_modal_window_open_after_click_on_ingridient(self, driver):
        burger_page  = BurgerPage(driver)
        burger_page.ingridient_click()
        assert burger_page.ingridient_modal_name_get()

    @allure.step("всплывающее окно закрывается кликом по крестику")
    def test_modal_window_closed(self, driver):
        burger_page  = BurgerPage(driver)
        burger_page.ingridient_click()
        burger_page.ingridient_modal_window_closed()
        assert burger_page.ing_visible()

    @allure.step("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_adding_ing_increase_counter(self, driver):
        burger_page  = BurgerPage(driver)
        burger_page.ingridient_move_to_order()
        assert burger_page.get_ingridient_counter_value() == 2
       
    @allure.step("залогиненный пользователь может оформить заказ")
    def test_user_inlogin_can_make_order(self, driver, create_user_data):
        main_page  = MainPage(driver)
        burger_page  = BurgerPage(driver)
        user_page = UserPage(driver)
        main_page.personal_acc_open()
        user_page.user_login(create_user_data)
        burger_page.ingridient_move_to_order()
        burger_page.create_order_bttn_click()
        assert burger_page.order_status_from_modal()
        
        