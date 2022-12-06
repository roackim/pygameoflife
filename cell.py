

class cell :
    size = 14
    outline = 1 # recommended between 0 and 3
    color = [Gray, Green]
    _grid = None # reference to the grid object
    
    def __init__( self, x, y, state = 0 ):
        self.x = x
        self.y = y
        self.state = state      # is the cell alive
        self.next_state = 0     # buffer for evolution
        self.rect = pygame.Rect(
                            self.x * (cell.size + cell.outline)
                            + cell._grid.margin_width,
                            self.y * (cell.size + cell.outline)
                            + cell._grid.margin_height,
                            cell.size,
                            cell.size
                            )
        
    def display( self ):
        pygame.draw.rect(Screen, cell.color[self.state], self.rect, 0 )

    def blit(self, color) :
        pygame.draw.rect(Screen, color, self.rect, 0 )
        
    def get_neighbours_state( self ):
        count = 0
        # check every adjacent cell, except itself
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                x, y = self.x + dx, self.y + dy
                if not (( x < 0 ) or
                        ( y < 0 ) or
                        ( x > cell._grid.width  - 1 ) or
                        ( y > cell._grid.height - 1 )) :
                    if not( dx == 0 and dy == 0 ):
                            count += self._grid.T[x][y].state

        return count


    def step(self):
        self.state = self.next_state
                

    """
    def pre_step(self): # Maze
        neigh = self.get_neighbours_state()
        if self.state == 1 :
            if( neigh < 1 ) or ( neigh > 5 ):
                self.next_state = 0
        elif self.state == 0 :
            if neigh == 3 :
                self.next_state = 1

    """
    def pre_step(self): # Conway's Game of life
        neigh = self.get_neighbours_state()
        if self.state == 1 :
            if( neigh < 2 ) or ( neigh > 3 ):
                self.next_state = 0
        elif self.state == 0 :
            if neigh == 3 :
                self.next_state = 1
    


        





















    
    ''' # HardCoded Version : 

    def get_neighbours_state( self ):
        count = 0
        x, y = self.x, self.y
        table = cell._grid.T
       
        count += table[ x-1 ][ y-1 ].state
        count += table[ x-1 ][  y  ].state
        count += table[ x-1 ][ y+1 ].state
        count += table[  x  ][ y-1 ].state
        count += table[  x  ][ y+1 ].state
        count += table[ x+1 ][ y-1 ].state
        count += table[ x+1 ][  y  ].state
        count += table[ x+1 ][ y+1 ].state
        
        return count
    '''














