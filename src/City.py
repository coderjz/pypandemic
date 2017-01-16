from .CityCubes import CityCubes
class City:
    def __init__(self, name, color, boardCubePool, outbreakCallback):
        self.name = name 
        self.color = color
        self.cubes = CityCubes(boardCubePool, outbreakCallback)


    def addCube(self, numToAdd, color):
        self.cityCubes.add(numToAdd, color)

    def removeCube(self, numToRemove, color):
        self.cityCubes.remove(numToRemove, color)
