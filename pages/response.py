import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.utility import LocalStorage
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode


class Response_trav:
    def __init__(self, driver, wait):
        self.browser = None
        self.driver = driver
        self.wait = wait
        self.json_data = None

    def open_page(self):
        # self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.browser.maximize_window()
        # wait = WebDriverWait(self.browser, 30)
        # self.browser.get("http://s4.travclan.com/control-panel")
        # LS = LocalStorage(self.browser)
        # LS.set("user",
        #        '{"result_code":1001,"status":"success","data":{"member":{"id":27778,"code":"mjdnz",'
        #        '"email":"nitinmadeshia@gmail.com","phone":"918860646291","username":"nitinmadeshia_9997596",'
        #        '"name":"Nitin Madeshia","family_name":"","company_name":"Adventure Travel","active":true,'
        #        '"deleted":false,"blocked":false,"website":"","created_at":"2021-10-19T17:46:18.985519",'
        #        '"updated_at":"2022-04-21T06:21:17.980700","nationality_id":null,"nationality":"<built-in method title '
        #        'of str object at 0x7f8acb7d48b8>","member_hash_id":"caa85af0a845849b141636f0c661b442a4f39415",'
        #        '"chat_password":"b)UBiZ#@KnmAV4{UUCbILKHbo0~h;~UZi6CfA4!Hwn;QKaOsjH"},"auth_tokens":{'
        #        '"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
        #        '.eyJleHAiOjE2NjI1NDk0NjIsImlhdCI6MTY2MTk0NDY2Miwic3ViIjoyNzc3OH0.mQCoOLUtceH1DIKt'
        #        '-6riyovncMQsoRy280G0QMrJZSg",'
        #        '"refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
        #        '.eyJleHAiOjE2NjIwMTAxMTgsImlhdCI6MTY1OTQxODExOCwic3ViIjoyNzc3OH0'
        #        '.ev5dMQX7RgFlw8ZpROJyFQ7que2BHgVH6Nr0fuT0P9E"}},"message":"OTP Verified","http_status_code":200}')

        self.driver.get("http://s4.travclan.com/control-panel")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Feedback']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='HISTORY']"))).click()

    def get_response(self):
        for request in self.driver.requests:
            if request.response:
                if request.url.startswith("https://b2b2c-api-staging.travclan.com/accounts/v2/customer-feedback/"):
                    body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                    decoded_body = body.decode('utf-8')
                    self.json_data = json.loads(decoded_body)
                    # print(
                    #     request.url,
                    #     request.response.status_code,
                    #     request.response.headers['Content-Type'],
                    #     # self.json_data
                    # )
        json_object = json.dumps(self.json_data, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        # print(json_object)
        # print(type(json_object))
        with open('sample.json', 'r') as openfile:

            # Reading from json file
            read_json = json.load(openfile)

        # for i in read_json['results']:
        #     print(i['customer_name'])
        first = read_json["results"]
        # print(first[0]['id'])

        assert first[0]['customer_name'] == "Selenium"
        assert first[0]['destination'] == "Europe"
        assert first[0]['date_of_travel'] == "2022-09-15"
        assert first[0]['is_show'] is None

        self.driver.quit()
