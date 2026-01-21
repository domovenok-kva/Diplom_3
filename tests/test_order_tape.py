import allure
from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.burger_page import BurgerPage

class TestOrderTape:
    @allure.title("Раздел «Лента заказов»")
    @allure.step("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_click_open_modal_window(self, driver):
        main_page  = MainPage(driver)
        burger_page= BurgerPage(driver)
        main_page.order_tape_open()
        burger_page.order_in_tape_open()
        assert burger_page.modal_wind_opens()
        
    @allure.step("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_from_history_visible(self, driver, create_user_data):
        main_page  = MainPage(driver)
        burger_page  = BurgerPage(driver)
        user_page = UserPage(driver)
        main_page.personal_acc_open()
        user_page.user_login(create_user_data)
        burger_page.ingridient_move_to_order()
        burger_page.create_order_bttn_click()
        burger_page.incorrect_number_invisible()
        burger_page.wait_until_text_visible()
        burger_page.order_number_from_modal()
        burger_page.order_wind_close()
        main_page.personal_acc_open()
        user_page.user_orders_page_open()
        num = user_page.get_user_order_number_in_history()
        main_page.order_tape_open()
        orders = burger_page.getting_num_of_orders_in_list()
        assert num in orders

    @allure.step("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_alltimecouter_updates_after_new_order(self, driver, create_user_data):
        main_page  = MainPage(driver)
        burger_page  = BurgerPage(driver)
        user_page = UserPage(driver)
        main_page.personal_acc_open()
        user_page.user_login(create_user_data)
        main_page.order_tape_open()
        num1 = burger_page.sum_of_orders_all_time()
        main_page.constructor_open()
        burger_page.ingridient_move_to_order()
        burger_page.create_order_bttn_click()
        burger_page.incorrect_number_invisible()
        burger_page.wait_until_text_visible()
        burger_page.order_number_from_modal()
        burger_page.order_wind_close()
        main_page.order_tape_open()
        num2 = burger_page.sum_of_orders_all_time()
        assert num2 > num1
        

    @allure.step("при создании нового заказа счётчик Выполнено за сегодня увеличивается") 
    def test_todaycounter_updates_after_new_order(self, driver, create_user_data):
        main_page  = MainPage(driver)
        burger_page  = BurgerPage(driver)
        user_page = UserPage(driver)
        main_page.personal_acc_open()
        user_page.user_login(create_user_data)
        main_page.order_tape_open()
        num1 = burger_page.sum_of_orders_today()
        main_page.constructor_open()
        burger_page.ingridient_move_to_order()
        burger_page.create_order_bttn_click()
        burger_page.incorrect_number_invisible()
        burger_page.wait_until_text_visible()
        burger_page.order_number_from_modal()
        burger_page.order_wind_close()
        main_page.order_tape_open()
        num2 = burger_page.sum_of_orders_today()
        assert num2 > num1


    @allure.step("после оформления заказа его номер появляется в разделе В работе")
    def test_number_of_new_order_seen_inwork(self, driver, create_user_data):
        main_page  = MainPage(driver)
        burger_page  = BurgerPage(driver)
        user_page = UserPage(driver)
        main_page.personal_acc_open()
        user_page.user_login(create_user_data)
        burger_page.ingridient_move_to_order()
        burger_page.create_order_bttn_click()
        burger_page.incorrect_number_invisible()
        burger_page.wait_until_text_visible()
        num = burger_page.order_number_from_modal()
        burger_page.order_wind_close()
        main_page.order_tape_open()
        num2 = burger_page.num_of_order_in_progress()
        assert num in num2

    