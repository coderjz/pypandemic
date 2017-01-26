from . import Enums
from .MediatorResource import MediatorResource
from .Event import CubesUnavailableEvent

#Stores the amount of cubes available for the game for each color
class BoardCubePool:
    MAX_NUM_CUBES = 24

    def __init__(self):
        self.mediator = MediatorResource.Mediator
        self.cubesUnavailable = CubesUnavailableEvent()
        
        self.numCubes = {
            Enums.Color.Blue: self.MAX_NUM_CUBES,
            Enums.Color.Red: self.MAX_NUM_CUBES,
            Enums.Color.Yellow: self.MAX_NUM_CUBES,
            Enums.Color.Black: self.MAX_NUM_CUBES
        }

    def takeCube(self, numToTake, color):
        if numToTake <= 0:
            raise ValueError("Invalid parameter numToTake passed, value = " + str(numToTake))

        if color not in self.numCubes:
            raise ValueError("Invalid parameter passed for color, value = " + str(color))

        if self.numCubes[color] >= numToTake:
            self.numCubes[color] -= numToTake
        else:
            self.numCubes[color] = 0
            self.mediator.dispatch(self.cubesUnavailable)


    def returnCube(self, numToReturn, color):
        if numToReturn <= 0:
            raise ValueError("Invalid parameter numToReturn , value = " + str(numToReturn))

        if color not in self.numCubes:
            raise ValueError("Invalid parameter passed for color, value = " + str(color))

        self.numCubes[color] += numToReturn
        if self.numCubes[color] > self.MAX_NUM_CUBES:
            self.numCubes[color] -= numToReturn
            raise ValueError("Attempt to return " + color + " cubes so that there are more cubes than we started with.")
