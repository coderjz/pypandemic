import unittest
import env

from src.ConnectionList import ConnectionList 
from src.CityList import CityList 

class TestConnectionList(unittest.TestCase):
    def setUp(self):
        self.cityList = CityList(None)

    #Check one city length as sanity check
    def testNumConnectionsMontreal(self):
        self.assertEqual(len(ConnectionList["Montreal"]), 3)

    #Check each key of connection is a valid city entry, catch typos
    def testAllKeysAreCities(self):
        for key in ConnectionList:
            self.assertTrue(key in self.cityList)

    #Check each item in array value of connection is a valid city entry, catch typos
    def testAllValuesAreCities(self):
        for key in ConnectionList:
            for value in ConnectionList[key]:
                self.assertTrue(value in self.cityList, "City " + value + " not in City List")

    #Every city must be connected at least once
    def testAllCitiesAreInConnection(self):
        for key in self.cityList:
            self.assertTrue(key in ConnectionList)


    #No city should connect to itself
    def testNoCityConnectsToSelf(self):
        for key in self.cityList:
            for value in ConnectionList[key]:
                self.assertNotEqual(key, value)

    #For all connections if from city a to city b connects,
    #Then from city b to city a should also connect
    def testAllConnectionsBidirectional(self):
        #Build all connections
        allConnections = []
        for key in ConnectionList:
            for value in ConnectionList[key]:
                allConnections.append((key, value))
                
        for connection in allConnections:
            if (connection[1], connection[0]) not in allConnections:
                self.assertTrue(False, "Could not find " + connection[1] + ":" + connection[0] + " in connection list") 

        self.assertTrue(True)
