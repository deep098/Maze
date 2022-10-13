import heapq
from maze import Maze, Cell
STEP = 1
class AStar(Maze, Cell):
    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
 
    def init_grid(self, dim, probability):
        self.dim = dim
        self.cells = Maze(dim, probability).generate_grid()
        self.start = self.cells[0][0]
        self.end = self.cells[dim - 1][dim - 1]

    def get_heuristic(self, cell):
        return abs(cell.x - self.end.x) + abs(cell.y - self.end.y)

    def get_adjacent_cells(self, cell):
        """Returns adjacent cells to a cell.
        Clockwise starting from the one on the right.
        @param cell get adjacent cells for this cell
        @returns adjacent cells list.
        """
        cells = []
        if cell.x < self.dim - 1:
            cells.append(self.cells[cell.x + 1][cell.y])
        if cell.y > 0:
            cells.append(self.cells[cell.x][cell.y - 1])
        if cell.x > 0:
            cells.append(self.cells[cell.x - 1][cell.y])
        if cell.y < self.dim - 1:
            cells.append(self.cells[cell.x][cell.y + 1])
        return cells

    def get_path(self):
        cell = self.end
        path = [(cell.x, cell.y)]
        while cell.parent is not self.start:
            cell = cell.parent
            path.append((cell.x, cell.y))

        path.append((self.start.x, self.start.y))
        path.reverse()

        return path

    def update_cell(self, adj, cell):
        """Update adjacent cell.
        @param adj adjacent cell to current cell
        @param cell current cell being processed
        """
        adj.g = cell.g + STEP
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def solve(self):
        """Solve maze, find path to ending cell.
        @returns path or None if not found.
        """
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while self.opened:
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # if ending cell, return found path
            if cell is self.end:
                return self.get_path()
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)

            for adj_cell in adj_cells:
                
                if not adj_cell.block and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found
                        # for this adj cell.
                        if adj_cell.g > cell.g + STEP:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))

if __name__ == '__main__':
    star = AStar()
    star.init_grid(5, 0.3)
    path = star.solve()
    print(path)
    # import pdb;pdb.set_trace()
