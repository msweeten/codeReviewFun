"""
move_car.py

Given a car initial position and command
Provides end position
"""

directions = ['N','E','S','W']
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move', 'B': 'backup'}

#No user input prompt
print 'Enter x and y of car as follows: x y'
user_input = raw_input()
GRID_MAX_X, GRID_MAX_Y = map(int, user_input.split())

#Initializes first_vehicle
#What's the first vehicle?
first_vehicle_x = None
first_vehicle_y = None

#no self.dir rename self.dir_
class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir_ = face

    def turn_left(self):
        self.dir_ = directions[(directions.index(self.dir_)-1)%len(directions)]
        
    def turn_right(self):
        self.dir_ = directions[(directions.index(self.dir_)+1)%len(directions)]
    def backup(self):
        self.dir_ = directions[(directions.index(self.dir_)+2)%len(directions)]

    def move(self):
        """Assigns new location based on current direction
        
        Checks if location is position of first_vehicle
        """
        
        new_x = self.x + movement[self.dir_][0]
        new_y = self.y + movement[self.dir_][1]

        #What's the or statement doing?
        #Do we want an "and"?

        #Why just the first_vehicle?
        #Reference to a global variable here

        #first vehicle can go off grid?
        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            #What's the xrange doing?
            
            #Unit Test Perhaps for if moving
            #along x if y changes
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y

#No user input prompt
#How does user know to enter 3 things? n things?
print 'Enter x y and initial direction as: x y dir'
vehicle_one_pos = raw_input().split()
print 'Enter move commands (L R M B) separated by a space'
vehicle_one_commands = raw_input()


#What if more than three commands are entered?
vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])

#evaluates user input, what happens if not an actual command?
#No command what happens?
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command]))

#This is doing nothing for first object
first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y

#No user input prompt
print 'Enter x y and initial direction as: x y dir'
vehicle_two_pos = raw_input().split()
print 'Enter move commands (L R M B) separated by a space'
vehicle_two_commands = raw_input()

#What if more than three commands are entered?
#Same complaints as vehicle one problem
vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_pos[2])#pos
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir
