import numpy as np
class Maze:
    def __init__(self, dimension, probability):
        self.dimension = dimension
        self.probability = probability

    def generate_grid(self):
        blocked_grid = self.generate_dfs()
        blocked_grid[0][0], blocked_grid[-1][-1] = False, False
        grid = [[Cell(i, j, blocked_grid[i][j]) for j in range(self.dimension)] for i in range(self.dimension)]
        return grid 
    
    
    def generate_dfs(self):
        grid = np.random.rand(self.dimension, self.dimension)
        visited = np.full(grid.shape, False)
        final_grid = np.full(grid.shape, False)
        
        stack = []
        stack.append({'x':0, 'y':0})
        
        while stack:
            last = stack.pop()
            x, y = last['x'], last['y']
            
            if visited[last['x']][last['y']]:
                continue
            
            visited[x][y] = True
            if np.random.rand() <= self.probability:
                final_grid[x][y] = True
            
            if y - 1 >= 0:
                stack.append({'x': x, 'y': y - 1})
            if y + 1 < len(grid):
                stack.append({'x': x, 'y': y + 1})
            if x - 1 >= 0:
                stack.append({'x': x - 1, 'y': y})
            if x + 1 < len(grid):
                stack.append({'x': x + 1, 'y': y})
        
        return final_grid

class Cell:
    def ___init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.g = 0 # g value of the cell (the distance from start cell to curr cell)
        self.h = 0 # h value of the cell (estimated value of the distance between curr cell and goal cell)
        self.f = 0 # f value of the cell (f = g+h in A*, defines the priority of a node)


    
        