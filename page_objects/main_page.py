import allure
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Жмяк на кнопку Лента заказов в хедере")
    def order_tape_open(self):
        self.wait_loading(MainPageLocators.order_tape_page)
        self.find_element(MainPageLocators.order_tape_page)
        self.click_element(MainPageLocators.order_tape_page)

    @allure.step("Жмяк на кнопку Конструктор в хедере")
    def constructor_open(self):
        self.wait_loading(MainPageLocators.burger_constructor_page)
        self.find_element(MainPageLocators.burger_constructor_page)
        self.click_element(MainPageLocators.burger_constructor_page)

    @allure.step("Жмяк на кнопку Личный кабинет в хедере")
    def personal_acc_open(self):
        self.find_element(MainPageLocators.personal_account)
        self.click_element(MainPageLocators.personal_account)

    @allure.step("Получаем адрес страницы")
    def get_page_url(self):
        return self.page_url()
      
   
