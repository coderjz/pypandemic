from .CityCubes import CityCubes
class City:
    def __init__(self, name, color, boardCubePool, outbreakCallback):
        self.name = name 
        self.color = color
        self.cubes = CityCubes(boardCubePool, outbreakCallback)


    def AddCube(self, numToAdd, color):
        self.cityCubes.Add(numToAdd, color)

    def RemoveCube(self, numToRemove, color):
        self.cityCubes.Remove(numToRemove, color)
