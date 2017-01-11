import unittest
import env

from src.BoardCubePool import BoardCubePool
from src import Enums

#Unit testing framework will automatically consider any method starting with test as
#We use this and put all unit tests in a single class to use the setup feature
class TestBoardCubePool(unittest.TestCase):
    wasCallbackCalled = False
    cubePool = None

    #Between each test we want to reset the callback to having not been called
    #Also we initiaze cube pool here to get reference to this object's callback function 
    def setUp(self):
        self.wasCallbackCalled = False
        self.cubePool = BoardCubePool(self.invokeCallback)
        
    #Set flag to indicate we called the callback
    def invokeCallback(self):
        self.wasCallbackCalled = True

    def testNoCallbackCallOnce(self):
        self.cubePool.Take(1, Enums.Color.Red)
        self.assertFalse(self.wasCallbackCalled)
        

    def testCallbackTake25(self):
        self.cubePool.Take(25, Enums.Color.Red)
        self.assertTrue(self.wasCallbackCalled)

    def testNoCallbackTake24Times(self):
        for i in range(24):
            self.cubePool.Take(1,Enums.Color.Yellow)
        self.assertFalse(self.wasCallbackCalled)


    def testCallbackTake25Times(self):
        for i in range(25):
            self.cubePool.Take(1,Enums.Color.Black)
        self.assertTrue(self.wasCallbackCalled)

    def testNoCallbackTakeEach10Times(self):
        for i in range(10):
            self.cubePool.Take(1, Enums.Color.Blue)
            self.cubePool.Take(1, Enums.Color.Black)
            self.cubePool.Take(1, Enums.Color.Red)
            self.cubePool.Take(1, Enums.Color.Yellow)

        self.assertFalse(self.wasCallbackCalled)



    def testCallbackTakeEach10TimesAndTakeBlueMore(self):
        for i in range(10):
            self.cubePool.Take(1, Enums.Color.Blue)
            self.cubePool.Take(1, Enums.Color.Black)
            self.cubePool.Take(1, Enums.Color.Red)
            self.cubePool.Take(1, Enums.Color.Yellow)

        for i in range(15):
            self.cubePool.Take(1, Enums.Color.Blue)

        self.assertTrue(self.wasCallbackCalled)


    def testNoCallbackTakeAndReturn(self):
        for i in range(10):
            self.cubePool.Take(1, Enums.Color.Yellow)

        self.cubePool.Return(1, Enums.Color.Yellow)

        for i in range(15):
            self.cubePool.Take(1, Enums.Color.Yellow)

        self.assertFalse(self.wasCallbackCalled)


    def testCallbackTakeAndReturnDifferentCube(self):
        for i in range(10):
            self.cubePool.Take(1, Enums.Color.Yellow)

        self.cubePool.Take(1, Enums.Color.Red)
        self.cubePool.Return(1, Enums.Color.Red)

        for i in range(15):
            self.cubePool.Take(1, Enums.Color.Yellow)

        self.assertTrue(self.wasCallbackCalled)


    def testExceptionsThrown(self):
        raised = False
        try:
            self.cubePool.Take(1, None)
        except:
            raised = True

        self.assertTrue(raised, "Exception was not raised")


        raised = False
        try:
            self.cubePool.Take(0, Enums.Colors.Blue)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")

        raised = False
        try:
            self.cubePool.Return(1, None)
        except:
            raised = True

        self.assertTrue(raised, "Exception was not raised")


        raised = False
        try:
            self.cubePool.Return(0, Enums.Colors.Blue)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")


    def testCannotReturnCubesNotTaken(self):
        raised = False
        try:
            self.cubePool.Return(1, Enums.Colors.Blue)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")


        raised = False
        try:
            self.cubePool.Take(3, Enums.Colors.Red)
            self.cubePool.Return(4, Enums.Colors.Red)
        except:
            raised = True
        self.assertTrue(raised, "Exception was not raised")

