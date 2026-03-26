from selenium.webdriver.common.by import By

class BurgerConstrLocators:

    order_bttn = (By.XPATH, "//button[text()='Оформить заказ']")
    one_ingridient = (By.XPATH, "//p[text() = 'Флюоресцентная булка R2-D3']")
    get_order_modal = (By.XPATH, ".//p[text()= 'Ваш заказ начали готовить']")
    burger_busket = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
  
    ingridient_name_in_modal_wind = (By.XPATH, "//*[text()='Детали ингредиента']")
    modal_window_close_bttn = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/*/button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    ingrid_counter = ( By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]")
    order_number_modal = (By.XPATH, "//h2[contains(@class,'title_shadow')]")
    order_modal_close =(By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/*/button[contains(@class, "Modal_modal__close_modified__3V5XS")]')
    order_status = (By.XPATH, "//*[contains(@class, 'Modal_modal__text')]/p[1]")
    incorr_numb = (By.XPATH, "//h2[contains(.,'9999')]")
