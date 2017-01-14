from . import Enums

#Stores the amount of cubes on the city
class CityCubes: 
    MAX_NUM_CUBES = 3

    def __init__(self, boardCubePool, callback):
        self.cubeTooManyCallback = callback
        self.boardCubePool = boardCubePool
        self.numCubes = {
            Enums.Color.Blue: 0,
            Enums.Color.Red: 0,
            Enums.Color.Yellow: 0,
            Enums.Color.Black: 0
        }

    def getTotalCubes(self):
        return sum(self.numCubes.values())

    def Add(self, numToAdd, color):
        if numToAdd <= 0:
            raise ValueError("Invalid parameter numToAdd passed, value = " + str(numToAdd))

        if color not in self.numCubes:
            raise ValueError("Invalid parameter passed for color, value = " + str(color))

        raiseTooMany = False

        if numToAdd + self.getTotalCubes() > self.MAX_NUM_CUBES:
            numToAdd = self.MAX_NUM_CUBES - self.getTotalCubes()
            raiseTooMany = True
        
        if numToAdd > 0:
            self.boardCubePool.Take(numToAdd, color)
            self.numCubes[color] += numToAdd

        if raiseTooMany and self.cubeTooManyCallback is not None:
            self.cubeTooManyCallback()



    def Remove(self, numToRemove, color):
        if numToRemove <= 0:
            raise ValueError("Invalid parameter numToRemove , value = " + numToRemove)

        if color not in self.numCubes:
            raise ValueError("Invalid parameter passed for color, value = " + color)

        if self.numCubes[color] < numToRemove:
            raise ValueError("Attempt to remove " + color + " cubes, more than the number that exist on the city")

        self.boardCubePool.Return(numToRemove, color)
        self.numCubes[color] -= numToRemove
