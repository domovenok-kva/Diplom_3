import allure
from page_objects.base_page import BasePage
from locators.burger_constr_locators import BurgerConstrLocators
from locators.order_tape_locators import OrderTapeLocators

class BurgerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по ингридиенту")
    def ingridient_click(self):
        self.click_element(BurgerConstrLocators.one_ingridient)

    def ing_visible(self):
        return self.element_visability(BurgerConstrLocators.one_ingridient)
    
    @allure.step("Получить имя модального окна")
    def ingridient_modal_name_get(self):
       return self.find_element(BurgerConstrLocators.ingridient_name_in_modal_wind)

    @allure.step("Закрыть окно ингридиента")
    def ingridient_modal_window_closed(self):
        self.click_element(BurgerConstrLocators.modal_window_close_bttn)

    @allure.step("Переместить ингридиент")
    def ingridient_move_to_order(self):
        ingridient = self.find_element(BurgerConstrLocators.one_ingridient)
        order_busket = self.find_element(BurgerConstrLocators.burger_busket)
        self.move_element(ingridient, order_busket)

    @allure.step("Получить значение счётчика ингридиента")
    def get_ingridient_counter_value(self):
        ing_counter = self.find_element(BurgerConstrLocators.ingrid_counter)
        return int(ing_counter.text)
    
    @allure.step("нажать на кнопку Оформить заказ")
    def create_order_bttn_click(self):
        self.click_element(BurgerConstrLocators.order_bttn)

    @allure.step("Статус заказа из окна подтверждения")
    def order_status_from_modal(self):
        return self.element_visability(BurgerConstrLocators.order_status)

    @allure.step("Номер заказа из окна подтверждения")
    def order_number_from_modal(self):
        ing_counter = self.element_visability(BurgerConstrLocators.order_number_modal)
        return str(ing_counter.text)
    
    @allure.step("Клик на заказ")
    def order_in_tape_open(self):
        self.click_element(OrderTapeLocators.list_of_orders)

    @allure.step("Появление модального окна")
    def modal_wind_opens(self):
        return self.element_visability(OrderTapeLocators.order_number_in_modal)
    
    @allure.step("Получить количество заказов за день")
    def sum_of_orders_today(self):
        ing_counter = self.element_visability(OrderTapeLocators.complited_today)
        return str(ing_counter.text)
    
    @allure.step("Получить количество заказов за всё время")
    def sum_of_orders_all_time(self):
        ing_counter = self.element_visability(OrderTapeLocators.complited_for_all_time)
        return str(ing_counter.text)
        
    @allure.step("Получаем номер заказа из колонки В работе")
    def num_of_order_in_progress(self):
        ing_counter = self.element_visability(OrderTapeLocators.preparing_orders)
        return str(ing_counter.text)
    
    @allure.step("Получаем список номеров заказов из ленты заказов")
    def getting_num_of_orders_in_list(self):
        ing_counter = self.element_visability(OrderTapeLocators.order_number_in_list)
        return str(ing_counter.text)
    
    @allure.step("Дождаться появления текста")
    def wait_until_text_visible(self):
        self.element_visability(BurgerConstrLocators.get_order_modal)
    
    @allure.step("Дождаться закрытия модального окна")
    def order_wind_close(self):
        self.wait_loading(BurgerConstrLocators.order_modal_close)
        self.find_element(BurgerConstrLocators.order_modal_close)
        self.click_element(BurgerConstrLocators.order_modal_close)

    @allure.step("Убеждаемся, что номер заказа не 9999")
    def incorrect_number_invisible(self):
        self.invisible(BurgerConstrLocators.incorr_numb)
  
           

    