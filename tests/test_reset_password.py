import allure
from page_objects.main_page import MainPage
from page_objects.reset_page import ResetPage
from data_for_test.urls import Urls

class TestResetPass:
    @allure.title("Восстановление пароля")
    
    @allure.step("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_switch_on_reset_pass_page(self, driver):
        main_page  = MainPage(driver)
        reset_page = ResetPage(driver)
        main_page.personal_acc_open()
        reset_page.reset_password_page_open()
        assert main_page.get_page_url() == Urls.forgot_pass

    @allure.step("ввод почты и клик по кнопке «Восстановить»")
    def test_email_enter_and_resetbttn_click(self, driver, create_user_data):
        main_page  = MainPage(driver)
        reset_page = ResetPage(driver)
        main_page.personal_acc_open()
        reset_page.reset_password_page_open()
        email = create_user_data['email']
        reset_page.fill_email_inpt(email)
        reset_page.restore_bttn_click() 
        reset_page.save_bttn_visible()
        assert main_page.get_page_url() == Urls.reset_pass

    @allure.step("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его") 
    def test_click_show_hide_buttn_in_passinpt(self, driver, create_user_data):
        main_page  = MainPage(driver)
        reset_page = ResetPage(driver)
        main_page.personal_acc_open()
        reset_page.reset_password_page_open()
        email = create_user_data['email']
        reset_page.fill_email_inpt(email)
        reset_page.restore_bttn_click() 
        reset_page.show_pass_bttn_click()
        assert reset_page.pass_inpt_hilighted()


