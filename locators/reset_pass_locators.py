from selenium.webdriver.common.by import By

class ResetPassLocators:
    pass_inpt = (By.XPATH, '//input[@name="name"]')
    hide_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    inpt_backlight = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::*')
    restore_bttn = (By.XPATH, "//*[text()='Восстановить']")
    save_bttn = (By.XPATH, "//*[text()='Сохранить']")