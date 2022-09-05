import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ChatBotPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_chatbot_page(self):
        self.driver.get("http://s4.mytripkart.in/www.systemthinking.in/")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//body/div[@id='root']/div/div/div/div/button[1]"))).click()

    def fill_form(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys("918574859652")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//cf-input[@tag-type='tel']//div//cf-input-button"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Domestic']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Himachal']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='5 - 6 nights']"))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//cf-radio-button[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys("12/12/2025")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//cf-input[@tag-type='tel']//div//cf-input-button"))).click()
        time.sleep(3)
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys(
            "3")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='cf-input-button typing']"))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Standard- 3 Star']"))).click()
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys(
            "chatbot-testing")
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='cf-input-button typing']"))).click()

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys(Keys.ENTER)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys("2")
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys(Keys.ENTER)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Standard- 3 Star']"))).click()
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys("chatbot-testing")
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type your answer here ...']"))).send_keys(Keys.ENTER)

