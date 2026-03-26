from selenium.webdriver.common.by import By

class OrderTapeLocators:
    list_of_orders = (By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]")
    order_number_in_list = (By.XPATH, "//*[contains(text(), '#')]")
    preparing_orders = (By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")
    order_number_in_modal  = (By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[1]")
    complited_for_all_time = (By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]")
    complited_today = (By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]")
