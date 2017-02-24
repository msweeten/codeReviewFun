"""
new_move_car.py

Given a car initial position and command
Provides end position
"""

class Vehicle(object):
    def __init__(self, x, y, start_dir):
        self.x = x
        self.y = y
        self.start_dir = start_dir
    def change(self, command):
        movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
        change_direction = new_direction(command, self.start_dir)
        if change_direction:
            self.start_dir = change_direction
        else:
            new_x = self.x + movement[self.start_dir]
            new_y = self.y + movement[self.start_dir]
        
        

    
def new_direction(command, start_direction):
    directions = ['N', 'E', 'S', 'W']    
    commands = {'L': -1, 'R': 1, 'B': 2}
    if command in commands:
        cmd = commands[command]        
        new_dir = directions[(directions.index(start_direction) + cmd)%len(directions)]
        return new_dir
    else:
        return None
            
    
            

def user_input():
    pass

def new_vehicle():
    pass

if __name__ == "__main__":
    pass
    
