from math import floor
from math import ceil

Period = 100
CellSize = cell.size + cell.outline

class grid :
    __initialized = False # used to restrict instantiation to only one
    width = int(floor( Win_width / CellSize ))
    height = int(floor( Win_height / CellSize ))
    
    # Calculate margin to center every cells
    margin_width  = ceil(( Win_width  - width  * CellSize ) / 2)
    margin_height = ceil(( Win_height - height * CellSize ) / 2)
    
    def __init__(self):
        # restrict instantiation to one
        if grid.__initialized:
            raise Exception("Can't create more than 1 instance of grid")
        grid.__initialized = True

        self.T = []
        self.running = False
        self.chrono = timer(Period, self.step)
        
        cell._grid  = self # reference to grid object
        mouse._grid = self

        for x in range(grid.width):
            self.T.append([])
            for y in range(grid.height):
                tmp_cell = cell( x, y, 0 )
                self.T[x].append(tmp_cell)

    def blit(self):
        for x in range(grid.width):
            for y in range(grid.height):
                self.T[x][y].display()

    def __getitem__(self, x ,y):
        return self.T[x][y]

    def step(self):
        for x in range(grid.width):
            for y in range(grid.height):
                self.T[x][y].pre_step()
        for x in range(grid.width):
            for y in range(grid.height):
                self.T[x][y].step()
                
    def clear(self):
        for x in range(grid.width):
            for y in range(grid.height):
                self.T[x][y].state = 0
                self.T[x][y].next_state = 0
        
