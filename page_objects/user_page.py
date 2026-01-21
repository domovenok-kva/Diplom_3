import allure
from page_objects.base_page import BasePage
from locators.login_user_page_locators import LoginUserPageLocators
from locators.login_page_locators import LoginPageLocators

class UserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ввод почты в поле на странице авторизации")
    def email_inpt_fillin(self, email):
        self.fill_inpt(LoginPageLocators.email_inpt, email)

    @allure.step("Ввод пароля в поле на странице авторизации")
    def password_inpt_fillin(self, password):
        self.fill_inpt(LoginPageLocators.psswrd_inpt, password)

    @allure.step("Нажатие на кнопку Войти")
    def enter_bttn_click(self):
        self.click_element(LoginPageLocators.login_bttn)

    @allure.step("Залогин")
    def user_login(self, user_data):
        self.email_inpt_fillin(user_data['email'])
        self.password_inpt_fillin(user_data['password'])
        self.enter_bttn_click()

    @allure.step("Открытие страницы истории заказов пользователя")
    def user_orders_page_open(self):
        self.click_element(LoginUserPageLocators.history_of_orders)

    @allure.step("Получить номер заказа пользователя в истории")
    def get_user_order_number_in_history(self):
        ing_counter = self.element_visability(LoginUserPageLocators.number_user_order)
        return str(ing_counter.text)

    @allure.step("Выход из ЛК")
    def exit_of_user(self):
        self.find_element(LoginUserPageLocators.exit_bttn)
        self.click_element(LoginUserPageLocators.exit_bttn)

    @allure.step("Видимость кнопки Входа")
    def enter_bttn_visible(self):
        self.find_element(LoginPageLocators.login_bttn)

        
