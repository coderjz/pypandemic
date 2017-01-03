import unittest
import env

from src.ConnectionList import ConnectionList 
from src.CityList import CityList 

#Check one city length as sanity check
class TestNumConnectionsMontreal(unittest.TestCase):
    def runTest(self):
        self.assertEqual(len(ConnectionList["Montreal"]), 3)

#Check each key of connection is a valid city entry, catch typos
class TestAllKeysAreCities(unittest.TestCase):
    def runTest(self):
        for key in ConnectionList:
            self.assertTrue(key in CityList)

#Check each item in array value of connection is a valid city entry, catch typos
class TestAllValuesAreCities(unittest.TestCase):
    def runTest(self):
        for key in ConnectionList:
            for value in ConnectionList[key]:
                self.assertTrue(value in CityList, "City " + value + " not in City List")

#Every city must be connected at least once
class TestAllCitiesAreInConnection(unittest.TestCase):
    def runTest(self):
        for key in CityList:
            self.assertTrue(key in ConnectionList)

#For all connections if from city a to city b connects,
#Then from city b to city a should also connect
class TestAllConnectionsBidirectional(unittest.TestCase):
    def runTest(self):
        #TODO this test.
        self.assertTrue(False)
