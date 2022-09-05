from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ContactusPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_contactus_page(self):
        self.driver.get("http://s4.mytripkart.in/www.systemthinking.in/contact")

    def fill_contactus_page(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys("ContactUs")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='phone_no']"))).send_keys("8574785968")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys(
            "contact@gmail.com")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='destination']"))).send_keys("Kerala")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))).send_keys(
            "Contactus-Testing")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Submit']"))).click()
        thankyou_text = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(.,'Thank')]")))
        print(thankyou_text.text)
        assert thankyou_text.text == "Thank you for submitting the detail! We will get back to you shortly!"
