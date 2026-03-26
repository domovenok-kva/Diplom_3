from selenium.webdriver.common.by import By

class LoginPageLocators:

    email_inpt = (By.NAME, "name")
    psswrd_inpt = (By.NAME, "Пароль")
    login_bttn = (By.XPATH, "//*[text()='Войти']")
    recovery_pass = (By.LINK_TEXT, 'Восстановить пароль')
