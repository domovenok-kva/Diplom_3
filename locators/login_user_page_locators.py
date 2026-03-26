from selenium.webdriver.common.by import By

class LoginUserPageLocators:
    history_of_orders = (By.LINK_TEXT, "История заказов")
    exit_bttn =(By.XPATH, '//button[text() = "Выход"]')
    number_user_order =  (By.XPATH, "//*[contains(text(), '#')]")