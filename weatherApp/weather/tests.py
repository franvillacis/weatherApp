from django.test import TestCase
from .helpers import *
# Create your tests here.


class TestHelpersCase(TestCase):
    def test_toCelsius(self):
        self.assertNotEqual(20, toCelsius(50))
        self.assertTrue(10, toCelsius(50))

    def test_parseTime(self):
        self.assertEqual('18:22:21', parseTime(1653693741, -18000))
        self.assertNotEqual('18:12:21', parseTime(1643693741, -18000))

    def test_degToCompass(self):
        self.assertEqual('South -> SouthWest', degToCompass(200))
        self.assertNotEqual('South', degToCompass(200))
