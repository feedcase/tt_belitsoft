import pytest
from test_petstore_api import data, url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture(autouse=False, scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()

