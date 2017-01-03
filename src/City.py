class City:
    name = ""
    color = 0
    numCubes = 0

    def __init__(self, name, color):
        self.name = name 
        self.color = color
        self.numCubes = 0


    #TODO: Make numCubes for each color, add a function addCube(color), removeCube(color) and function for total number of cubes
    #We will need to store number of cubes for each color for when we put in logic for ending the game if all colors of a cube are removed.
