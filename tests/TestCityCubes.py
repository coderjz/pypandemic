import unittest
import env

from src import Enums
from src.CityCubes import CityCubes
from src.BoardCubePool import BoardCubePool

class TestCityCubes(unittest.TestCase):

    #Between each test we want to reset the callback to having not been called
    #Also we initiaze cube cubes here to get reference to this object's callback function 
    def setUp(self):
        self.boardCubePool = BoardCubePool(None)
        self.wasCallbackCalled = False
        self.cityCubes = CityCubes(self.boardCubePool, self.invokeCallback)
        
    #Set flag to indicate we called the callback
    def invokeCallback(self):
        self.wasCallbackCalled = True

    def testNoCallbackCallOnce(self):
        self.cityCubes.add(1, Enums.Color.Red)
        self.assertFalse(self.wasCallbackCalled)


    def testCallbackAdd4(self):
        self.cityCubes.add(4, Enums.Color.Red)
        self.assertTrue(self.wasCallbackCalled)

    def testNoCallbackAdd3Times(self):
        for i in range(3):
            self.cityCubes.add(1,Enums.Color.Yellow)
        self.assertFalse(self.wasCallbackCalled)


    def testCallbackAdd4Times(self):
        for i in range(4):
            self.cityCubes.add(1,Enums.Color.Black)
        self.assertTrue(self.wasCallbackCalled)

    def testNoCallbackAddEach1Time(self):
        self.cityCubes.add(1, Enums.Color.Blue)
        self.cityCubes.add(1, Enums.Color.Black)
        self.cityCubes.add(1, Enums.Color.Red)

        self.assertFalse(self.wasCallbackCalled)



    def testNoCallbackAddAndremove(self):
        for i in range(2):
            self.cityCubes.add(1, Enums.Color.Yellow)

        self.cityCubes.remove(1, Enums.Color.Yellow)

        for i in range(2):
            self.cityCubes.add(1, Enums.Color.Red)

        self.assertFalse(self.wasCallbackCalled)


    def testCallbackAddAndRemoveDifferentCube(self):
        for i in range(2):
            self.cityCubes.add(1, Enums.Color.Yellow)

        self.cityCubes.add(1, Enums.Color.Red)
        self.cityCubes.remove(1, Enums.Color.Red)

        for i in range(2):
            self.cityCubes.add(1, Enums.Color.Yellow)

        self.assertTrue(self.wasCallbackCalled)


    def testExceptionsThrown(self):
        raised = False
        try:
            self.cityCubes.add(1, None)
        except:
            raised = True

        self.assertTrue(raised, "Exception was not raised")


        raised = False
        try:
            self.cityCubes.add(0, Enums.Colors.Blue)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")

        raised = False
        try:
            self.cityCubes.remove(1, None)
        except:
            raised = True

        self.assertTrue(raised, "Exception was not raised")


        raised = False
        try:
            self.cityCubes.remove(0, Enums.Colors.Blue)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")


    def testCannotRemoveCubesNotAddn(self):
        raised = False
        try:
            self.cityCubes.remove(1, Enums.Colors.Blue)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")


        raised = False
        try:
            self.cityCubes.add(3, Enums.Colors.Red)
            self.cityCubes.remove(4, Enums.Colors.Red)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")

