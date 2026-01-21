from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #Поиск элемента
    def find_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*locator)
    
    def wait_loading(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    #Клик по элементу
    def click_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).click()

    #Ввод значения в инпут
    def fill_inpt(self, locator, data_in):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).send_keys(data_in)

    #Видимость элемента
    def element_visability(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    
    #Получить значение элемента
    def get_value_of_element(self,locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).text()
    
    #Перетащить элемент
    def move_element(self, begin_point, end_point):      
        action = ActionChains(self.driver)
        action.click_and_hold(begin_point)        
        action.move_to_element(end_point)       
        action.release()                              
        action.perform()                             

    #Получить URL
    def page_url(self):
        return self.driver.current_url
    #Дождаться пока элемент исчезнет
    def invisible(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))
    
