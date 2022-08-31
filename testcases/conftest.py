import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from utils.utility import LocalStorage


@pytest.fixture(scope="class")
def setUp(request):
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://s4.mytripkart.in/www.systemthinking.in/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    storage = LocalStorage(driver)
    storage.set("b2b2cUser",
                '{"data":{"auth_tokens":{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZW1iZXJfaWQiOiJ0YWNfMjA4YzYwNDUzYjA0MGI5ZGFkNzkzZDYyZDk5YjVjOTZfMTY2MDA3MDc0Ni45ODY2MTUiLCJmdWxsX25hbWUiOiJSb3NoYW4iLCJleHAiOjE2NjMzOTkyNDV9.AHvp8NLfMBBSWFa2M47hZQlKnmwn0_ZaJRobNv1PY7M"}},"username":"Roshan"}')
    driver.get("http://s4.mytripkart.in/www.systemthinking.in/")

    request.cls.driver = driver
    request.cls.wait = wait
