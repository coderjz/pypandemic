import unittest
import env

from src.CityList import CityList as CityList

class TestCityList(unittest.TestCase):
    def setUp(self):
        self.cityList = CityList(None, None)

    def testLength(self):
        numCities = 0
        for city in self.cityList:
            numCities += 1
        self.assertEqual(numCities, 48)

    def testContainsLosAngeles(self):
        self.assertTrue("Los Angeles" in self.cityList)
