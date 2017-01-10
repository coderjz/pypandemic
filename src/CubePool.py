from . import Enums

#Stores the amount of cubes available for the game for each color
class CubePool:
    MAX_NUM_CUBES = 24

    numRedCubes = MAX_NUM_CUBES
    numBlueCubes = MAX_NUM_CUBES
    numYellowCubes = MAX_NUM_CUBES
    numBlackCubes = MAX_NUM_CUBES

    #Function to call when cubes for any color are not available to be taken
    cubesUnavailableCallback = None

    def __init__(self, callback):
        self.cubesUnavailableCallback = callback

    def Take(self, numToTake, color):
        if numToTake <= 0:
            raise ValueError("Invalid parameter numToTake passed, value = " + numToTake)

        if color == Enums.Color.Blue:
            if self.numBlueCubes >= numToTake:
                self.numBlueCubes -= numToTake
            else:
                self.numBlueCubes = 0
                if self.cubesUnavailableCallback is not None:
                    self.cubesUnavailableCallback()
        elif color == Enums.Color.Red:
            if self.numRedCubes >= numToTake:
                self.numRedCubes -= numToTake
            else:
                self.numRedCubes = 0
                if self.cubesUnavailableCallback is not None:
                    self.cubesUnavailableCallback()
        elif color == Enums.Color.Yellow:
            if self.numYellowCubes >= numToTake:
                self.numYellowCubes -= numToTake
            else:
                self.numYellowCubes = 0
                if self.cubesUnavailableCallback is not None:
                    self.cubesUnavailableCallback()
        elif color == Enums.Color.Black:
            if self.numBlackCubes >= numToTake:
                self.numBlackCubes -= numToTake
            else:
                self.numBlackCubes = 0
                if self.cubesUnavailableCallback is not None:
                    self.cubesUnavailableCallback()
        else:
            raise ValueError("Invalid parameter passed for color, value = " + color)


    def Return(self, numToReturn, color):
        if numToReturn <= 0:
            raise ValueError("Invalid parameter numToReturn , value = " + numToReturn)

        if color == Enums.Color.Blue:
            self.numBlueCubes += numToReturn
            if self.numBlueCubes > self.MAX_NUM_CUBES:
                self.numBlueCubes -= numToReturn
                raise ValueError("Attempt to return cubes so that there are more blue cubes than we started with.")
        elif color == Enums.Color.Red:
            self.numRedCubes += numToReturn
            if self.numRedCubes > self.MAX_NUM_CUBES:
                self.numRedCubes -= numToReturn
                raise ValueError("Attempt to return cubes so that there are more red cubes than we started with.")
        elif color == Enums.Color.Yellow:
            self.numYellowCubes += numToReturn
            if self.numYellowCubes > self.MAX_NUM_CUBES:
                self.numYellowCubes -= numToReturn
                raise ValueError("Attempt to return cubes so that there are more yellow cubes than we started with.")
        elif color == Enums.Color.Black:
            self.numBlackCubes += numToReturn
            if self.numBlackCubes > self.MAX_NUM_CUBES:
                self.numBlackCubes -= numToReturn
                raise ValueError("Attempt to return cubes so that there are more black cubes than we started with.")
        else:
            raise ValueError("Invalid parameter passed for color, value = " + color)
