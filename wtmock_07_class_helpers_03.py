from unittest import TestCase, mock, expectedFailure
from wtmock_07_class_helpers_02 import CountryPricer
import unittest

class TestCountryPrices(TestCase):

    @expectedFailure
    def test_patch_constant(self):
        with mock.patch('wtmock_07_class_helpers_02.COUNTRIES',['GB']):
            pricer = CountryPricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'),80)

if __name__ == "__main__":
    unittest.main()
