from . import Enums

#Stores the amount of cubes available for the game for each color
class BoardCubePool:
    MAX_NUM_CUBES = 24

    def __init__(self, callback):
        self.cubesUnavailableCallback = callback
        self.numCubes = {
            Enums.Color.Blue: self.MAX_NUM_CUBES,
            Enums.Color.Red: self.MAX_NUM_CUBES,
            Enums.Color.Yellow: self.MAX_NUM_CUBES,
            Enums.Color.Black: self.MAX_NUM_CUBES
        }

    def Take(self, numToTake, color):
        if numToTake <= 0:
            raise ValueError("Invalid parameter numToTake passed, value = " + numToTake)

        if color not in self.numCubes:
            raise ValueError("Invalid parameter passed for color, value = " + color)

        if self.numCubes[color] >= numToTake:
            self.numCubes[color] -= numToTake
        else:
            self.numCubes[color] = 0
            if self.cubesUnavailableCallback is not None:
                self.cubesUnavailableCallback()


    def Return(self, numToReturn, color):
        if numToReturn <= 0:
            raise ValueError("Invalid parameter numToReturn , value = " + numToReturn)

        if color not in self.numCubes:
            raise ValueError("Invalid parameter passed for color, value = " + color)

        self.numCubes[color] += numToReturn
        if self.numCubes[color] > self.MAX_NUM_CUBES:
            self.numCubes[color] -= numToReturn
            raise ValueError("Attempt to return " + color + " cubes so that there are more cubes than we started with.")
