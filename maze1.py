x = 0
x < 6
y = 0
y < 6
game = True
north = True
east = True
south = True
west = True

class Directions
    def __init__(x, y):
        if x == 0 and y == 0:
            north = False
            east = True
            south = True
            west = False
        if x == 0 and y == 1:
            north = False
            east = True
            south = False
            west = True
        if x == 0 and y == 2:
            north = False
            east = False
            south = True
            west = True
        if x == 0 and y == 3:
            north = False
            east = True
            south = True
            west = False
        if x == 0 and y == 4:
            north = False
            east = True
            south = False
            west = True
        if x == 0 and y == 5:
            north = False
            east = False
            south = True
            west = True
        if x == 1 and y == 0:
            north = True
            east = False
            south = True
            west = False
        if x == 1 and y == 1:
            north = False
            east = True
            south = True
            west = False
        if x == 1 and y == 2:
            north = True
            east = False
            south = False
            west = True
        if x == 1 and y == 3:
            north = True
            east = False
            south = True
            west = False
        if x == 1 and y == 4:
            north = False
            east = True
            south = True
            west = False
        if x == 1 and y == 5:
            north = True
            east = False
            south = True
            west = True
        if x == 2 and y == 0:
            north = True
            east = False
            south = True
            west = False
        if x == 2 and y == 1:
            north = True
            east = False
            south = False
            west = False
        if x == 2 and y == 2:
            north = False
            east = True
            south = True
            west = False
        if x == 2 and y == 3:
            north = True
            east = False
            south = True
            west = True
        if x == 2 and y == 4:
            north = True
            east = False
            south = False
            west = False
        if x == 2 and y == 5:
            north = True
            east = False
            south = True
            west = False
        if x == 3 and y == 0:
            north = True
            east = True
            south = False
            west = False
        if x == 3 and y == 1:
            north = False
            east = True
            south = True
            west = True
        if x == 3 and y == 2:
            north = True
            east = False
            south = False
            west = True
        if x == 3 and y == 3:
            north = True
            east = True
            south = True
            west = False
        if x == 3 and y == 4:
            north = False
            east = True
            south = False
            west = True
        if x == 3 and y == 5:
            north = True
            east = False
            south = False
            west = True
        if x == 4 and y == 0:
            north = False
            east = True
            south = True
            west = False
        if x == 4 and y == 1:
            north = True
            east = False
            south = False
            west = True
        if x == 4 and y == 2:
            north = False
            east = False
            south = True
            west = False
        if x == 4 and y == 3:
            north = True
            east = False
            south = True
            west = False
        if x == 4 and y == 4:
            north = False
            east = True
            south = True
            west = False
        if x == 4 and y == 5:
            north = False
            east = False
            south = True
            west = True
        if x == 5 and y == 0:
            north = True
            east = True
            south = False
            west = False
        if x == 5 and y == 1:
            north = False
            east = False
            south = False
            west = True
        if x == 5 and y == 2:
            north = True
            east = True
            south = False
            west = False
        if x == 5 and y == 3:
            north = True
            east = True
            south = False
            west = True
        if x == 5 and y == 4:
            north = True
            east = False
            south = False
            west = True
        if x == 5 and y == 5:
            north = True
            east = False
            south = False
            west = False
    def update(north, east, south, west):
        

print('Welcome to The Maze.')
#print('Type START to start.')
# start = input()
#    if start == 'START':
x = 0
y = 0
print('You are now at ' + str(x) + ', ' + str(y))

while -1 < x < 6 and -1 < y < 6:
    if north == True:
        print('You can GO NORTH.')
    if east == True:
        print('You can GO EAST.')
    if south == True:
        print('You can GO SOUTH.')
    if west == True:
        print('You can GO WEST.')
    direction = input()
    if direction == 'GO NORTH' and north == True:
        x = x
        y = y - 1
        print('You are now at ' + str(x) + ', ' + str(y))
    elif direction == 'GO EAST' and east == True:
        x = x + 1
        y = y
        print('You are now at ' + str(x) + ', ' + str(y))
    elif direction == 'GO SOUTH' and south == True:
        x = x
        y = y + 1
        print('You are now at ' + str(x) + ', ' + str(y))
    elif direction == 'GO WEST' and west == True:
        x = x - 1
        y = y
        print('You are now at ' + str(x) + ', ' + str(y))
    else:
        print('Invalid response. Please try again.')
    if x == 5 and y == 5:
        print('You found the end! Congratulations!')
        print('Type DONE to claim your reward and end the game.')
        done = input()
        if done == 'DONE':
            print('You won $200,000,000!')
            break
        
