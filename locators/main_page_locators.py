from selenium.webdriver.common.by import By

class MainPageLocators:
    burger_constructor_page = (By.XPATH,"//*[text() = 'Конструктор']" )
    order_tape_page = (By.XPATH,"//*[text() = 'Лента Заказов']" )
    personal_account = (By.XPATH,"//*[text() = 'Личный Кабинет']" )
    