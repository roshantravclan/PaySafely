import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PaySafely:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_paysafely_page(self):
        self.driver.get("http://s4.mytripkart.in/www.systemthinking.in/pay")

    def fill_payment_form(self, name, number, email, amount):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys(name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))).send_keys(number)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='amount']"))).send_keys(amount)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[1]"))).click()

    def select_payment_method(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Net Banking*']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Pay INR')]"))).click()
        # source = self.wait.until(
        #         EC.presence_of_element_located((By.XPATH, "(//iframe[@class='razorpay-checkout-frame'])[2]")))
        time.sleep(5)
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "(//iframe[@class='razorpay-checkout-frame'])[2]"))
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Pay using Netbanking')]"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='bank-radio-SBIN']"))).click()
        time.sleep(2)
        # print(self.driver.page_source)
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='footer-cta']")))
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class ='success']"))).click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        lasttext  = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h3"))).text

        assert "Thank You. Your Payment was Successful!" == self.wait.until(EC.presence_of_element_located((By.XPATH, "//h3"))).text
