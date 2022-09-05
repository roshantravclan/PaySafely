from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ServicePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_services_page(self):
        self.driver.get("http://s4.mytripkart.in/www.systemthinking.in/pages/services")

    def fill_service_form(self):

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys("Services")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='phone_no']"))).send_keys("8555858585")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys("test@gmail.com")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='destination']"))).send_keys("Delhi")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))).send_keys(
            "selenium-testing")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Submit']"))).click()

