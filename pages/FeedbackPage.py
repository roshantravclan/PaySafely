import re
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.utility import LocalStorage as ls, LocalStorage


class FeedbackPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_feedback_page(self):
        self.driver.get("http://s4.travclan.com/control-panel")
        LS = LocalStorage(self.driver)
        LS.set("user",
               '{"result_code":1001,"status":"success","data":{"member":{"id":27778,"code":"mjdnz",'
               '"email":"nitinmadeshia@gmail.com","phone":"918860646291","username":"nitinmadeshia_9997596",'
               '"name":"Nitin Madeshia","family_name":"","company_name":"Adventure Travel","active":true,'
               '"deleted":false,"blocked":false,"website":"","created_at":"2021-10-19T17:46:18.985519",'
               '"updated_at":"2022-04-21T06:21:17.980700","nationality_id":null,"nationality":"<built-in method title '
               'of str object at 0x7f8acb7d48b8>","member_hash_id":"caa85af0a845849b141636f0c661b442a4f39415",'
               '"chat_password":"b)UBiZ#@KnmAV4{UUCbILKHbo0~h;~UZi6CfA4!Hwn;QKaOsjH"},"auth_tokens":{'
               '"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
               '.eyJleHAiOjE2NjI1NDk0NjIsImlhdCI6MTY2MTk0NDY2Miwic3ViIjoyNzc3OH0.mQCoOLUtceH1DIKt'
               '-6riyovncMQsoRy280G0QMrJZSg",'
               '"refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
               '.eyJleHAiOjE2NjIwMTAxMTgsImlhdCI6MTY1OTQxODExOCwic3ViIjoyNzc3OH0'
               '.ev5dMQX7RgFlw8ZpROJyFQ7que2BHgVH6Nr0fuT0P9E"}},"message":"OTP Verified","http_status_code":200}')
        self.driver.get("http://s4.travclan.com/control-panel")

    def send_feedback_link(self, date_value):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Feedback']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='customer_name']"))).send_keys(
            "Selenium")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='destination']"))).send_keys("Europe")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='date_of_travel']"))).click()
        dates = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='presentation']/button")))
        for date in dates:
            if date_value == date.text:
                date.click()
                break

        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[12]"))).click()
        url = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@role='dialog']//div//div//div//div[@id='copyTextAreaContainer']"))).text
        new_url = re.sub("www.", "", url, count=1)
        new_url = re.sub("staging","s4",new_url,count=1)
        new_url = re.sub("https","http",new_url,count=1)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
        self.driver.execute_script("window.open('');")

        # Switch to the new window and open new URL
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(new_url)
        # print(self.driver.page_source)
        self.driver.get(new_url)
        # print(self.driver.page_source)
        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='details-button']"))).click()
        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Proceed')]"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Write your feedback here']"))).send_keys("Testing selenium feedback")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Submit']"))).click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()




