from re import X
import numpy as np
class Maze:
    def __init__(self, dimension, probability):
        self.dimension = dimension
        self.probability = probability
        self.grid = np.array([])
    
    def generate_grid(self):
        random_arr = np.random.rand(self.dimension, self.dimension)
        random_arr = random_arr > self.probability
        random_arr[0][0], random_arr[-1][-1] = True, True
        grid = [[Cell(i, j, random_arr[i][j]) for j in range(self.dimension)] for i in range(self.dimension)]
        return grid 
    

class Cell:
    def ___init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.g = 0 # g value of the cell (the distance from start cell to curr cell)
        self.h = 0 # h value of the cell (estimated value of the distance between curr cell and goal cell)
        self.f = 0 # f value of the cell (f = g+h in A*, defines the priority of a node)


    
        