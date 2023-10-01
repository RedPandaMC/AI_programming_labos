"""Doe deze oefening nog eens. Als er meer tijd is."""
class RobotHoover:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    """
    y
    ⭡
    │       (0, 1)
    │ (-1,0)  Ro  ( 1,0)
    │       (0,-1)
    O———————————————————⭢x
    
    Coords (x, y)
    """
    def __init__(self):
        self.location = {'x': 0, 'y': 0}
        self.has_been_cleaned = {}
        self.current_direction = 0
    
    def clean(self, warehouse):
        while True:
            # check if the current tile is dirty
            if warehouse[self.location['x']][self.location['y']] == 1: 
                self.clean_tile()

            # move in the current direction
            new_location = {'x': self.location['x'] + self.DIRECTIONS[self.current_direction][0], 
                            'y': self.location['y'] + self.DIRECTIONS[self.current_direction][1]}

            # check if the next cell in the current direction is outside the grid or is an obstacle
            if (new_location['x'] < 0 or new_location['x'] >= len(warehouse) or 
                new_location['y'] < 0 or new_location['y'] >= len(warehouse[0]) or 
                warehouse[new_location['x']][new_location['y']] == 'obstacle'):
                # change direction (turn right)
                self.current_direction = (self.current_direction + 1) % 4
            else:
                self.move_down()
                
    def clean_tile(self):
        self.has_been_cleaned[(self.location['x'], self.location['y'])] = True
        print(f'Cleaning tile at location: ({self.location["x"]}, {self.location["y"]})')

    def move_down(self):
        self.location['x'] += self.DIRECTIONS[self.current_direction][0]
        self.location['y'] += self.DIRECTIONS[self.current_direction][1]
        print(f'Moving to location: ({self.location["x"]}, {self.location["y"]})')

warehouse = [[1 for _ in range(5)] for _ in range(2)]
h = RobotHoover()
h.clean(warehouse)