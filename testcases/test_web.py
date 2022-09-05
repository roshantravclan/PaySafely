import time
import unittest

import ipdb
import pytest

from pages.ChatbotPage import ChatBotPage
from pages.ContactusPage import ContactusPage
from pages.FeedbackPage import FeedbackPage
from pages.PaySafelyPage import PaySafely
from ddt import ddt, unpack, data

from pages.Services import ServicePage
from pages.response import Response_trav
from utils.utility import read_data_from_excel, read_data_from_csv


@pytest.mark.usefixtures("setUp")
@ddt
class TestWeb(unittest.TestCase):
    @pytest.mark.paysafely
    @data(*read_data_from_csv("/home/roshan/PycharmProjects/Payment/csv_file.csv"))
    @unpack
    def test_paysafely(self, name, number, email, amount):
        print(name)
        pay_safely = PaySafely(self.driver, self.wait)
        pay_safely.open_paysafely_page()
        pay_safely.fill_payment_form(name, number, email, amount)
        pay_safely.select_payment_method()

    @pytest.mark.service
    def test_services(self):
        serviceObject = ServicePage(self.driver, self.wait)
        serviceObject.open_services_page()
        serviceObject.fill_service_form()

    @pytest.mark.feedback
    def test_feedback(self):
        feedback = FeedbackPage(self.driver, self.wait)
        feedback.open_feedback_page()
        feedback.send_feedback_link("15")

    @pytest.mark.contactus
    def test_contactus(self):
        contactus = ContactusPage(self.driver, self.wait)
        contactus.open_contactus_page()
        contactus.fill_contactus_page()

    @pytest.mark.chatbot
    def test_contactus(self):
        chatbot = ChatBotPage(self.driver, self.wait)
        chatbot.open_chatbot_page()
        chatbot.fill_form()

    @pytest.mark.feedback
    def test_response(self):
        response_test = Response_trav(self.driver, self.wait)
        response_test.open_page()
        time.sleep(5)
        response_test.get_response()
