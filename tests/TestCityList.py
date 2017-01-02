import unittest
import env

from src.CityList import CityList as CityList

class TestLength(unittest.TestCase):
    def runTest(self):
        self.assertEqual(len(CityList), 48)

class TestContainsLosAngeles(unittest.TestCase):
    def runTest(self):
        self.assertTrue("Los Angeles" in CityList)
