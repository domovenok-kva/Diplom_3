import allure
from page_objects.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.reset_pass_locators import ResetPassLocators

class ResetPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def reset_password_page_open(self):
        self.click_element(LoginPageLocators.recovery_pass)

    @allure.step("Заполнение инпута почты")
    def fill_email_inpt(self, email):
        self.fill_inpt(ResetPassLocators.pass_inpt, email)

    @allure.step("клик по кнопке «Восстановить»")
    def restore_bttn_click(self):
        self.click_element(ResetPassLocators.restore_bttn)

    @allure.step("клик по кнопке показать/скрыть пароль")
    def show_pass_bttn_click(self):
        self.wait_loading(ResetPassLocators.hide_icon)
        self.find_element(ResetPassLocators.hide_icon)
        self.click_element(ResetPassLocators.hide_icon)

    @allure.step("поле пароль подсвечивается")
    def pass_inpt_hilighted(self):
        self.find_element(ResetPassLocators.pass_inpt)
        return self.element_visability(ResetPassLocators.inpt_backlight)
    @allure.step("Кнопка сохранить видна")
    def save_bttn_visible(self):
        self.find_element(ResetPassLocators.save_bttn)
        