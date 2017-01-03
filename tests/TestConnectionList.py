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


#No city should connect to itself
class TestNoCityConnectsToSelf(unittest.TestCase):
    def runTest(self):
        for key in CityList:
            for value in ConnectionList[key]:
                self.assertNotEqual(key, value)

#For all connections if from city a to city b connects,
#Then from city b to city a should also connect
class TestAllConnectionsBidirectional(unittest.TestCase):
    def runTest(self):
        #Build all connections
        allConnections = []
        for key in ConnectionList:
            for value in ConnectionList[key]:
                allConnections.append((key, value))
                
        for connection in allConnections:
            if (connection[1], connection[0]) not in allConnections:
                self.assertTrue(False, "Could not find " + connection[1] + ":" + connection[0] + " in connection list") 

        self.assertTrue(True)
