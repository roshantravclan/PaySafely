import unittest

import ipdb
import pytest

from pages.PaySafelyPage import PaySafely
from ddt import ddt, unpack, data

from utils.utility import read_data_from_excel, read_data_from_csv


@pytest.mark.usefixtures("setUp")
@ddt
class TestWeb(unittest.TestCase):
    @data(*read_data_from_csv("/home/roshan/PycharmProjects/Payment/csv_file.csv"))
    @unpack
    def test_web(self, name, number, email, amount):
        print(name)
        pay_safely = PaySafely(self.driver, self.wait)
        pay_safely.open_paysafely_page()
        pay_safely.fill_payment_form(name, number, email, amount)
        pay_safely.select_payment_method()