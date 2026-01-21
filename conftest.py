import pytest
import requests
from faker import Faker
from selenium import webdriver
from data_for_test.urls import Urls
from data_for_test.browsers import Browsers

@pytest.fixture(params=[Browsers.Firefox, Browsers.Chrome])
def driver(request):
    
    if request.param == Browsers.Firefox:
        driver = webdriver.Firefox()
    elif request.param == Browsers.Chrome:
        driver = webdriver.Chrome()
    
    driver.get(Urls.main_url)
        
    yield driver
    driver.quit()
        

@pytest.fixture
def create_user_data():
    fake = Faker("en_US")
    payload = { 'email': fake.email(), 'password': fake.password(), 'name': fake.name()}
    requests.post(Urls.create_user_url, data = payload)
    yield payload
    requests.delete(Urls.user_del, headers={'Authorization': 'accessToken'})



