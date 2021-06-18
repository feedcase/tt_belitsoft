import pytest
from selenium import webdriver


@pytest.fixture(autouse=False, scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()

