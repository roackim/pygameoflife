

class mouse :
    __initialized = False
    _grid = None # reference to the grid object

    def __init__( self ) :
        if mouse.__initialized:
            raise Exception("Can't create more than 1 instance of mouse")
        mouse.__initialized = True

        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        # left, middle, right, wheel_up, wheel_down
        self.button = [0, 0, 0, 0, 0]

                
    def get_pos():
        return (self.x, self.y)

    def set_pos( self, pos ):
        self.x, self.y = pos    

    def get_cell( self ):
        CellSize = cell.size + cell.outline
        # get Grid coordinate, center cells origin
        x = self.x - mouse._grid.margin_width  - CellSize / 2
        y = self.y - mouse._grid.margin_height - CellSize / 2
        x = int(round( x / CellSize ))
        y = int(round( y / CellSize ))
        # case if mouse is outside of grid
        if (( x < 0 ) or
            ( y < 0 ) or
            ( x > cell._grid.width  - 1 ) or
            ( y > cell._grid.height - 1 )) :
            return mouse._grid.T[0][0]
        # case if mouse is not outside of grid
        else :
            return mouse._grid.__getitem__(x, y)

    def set_cell( self, state ):
        focused_cell = self.get_cell()
        if( focused_cell.state != state ):
            focused_cell.state = state
            focused_cell.next_state = state # Needed (don't know why yet)
        










        
            
