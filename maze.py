x = 0
y = 0

if x == 0 and y == 0:
    location = 'ES'
if x == 0 and y == 1:
     location = 'EW'
if x == 0 and y == 2:
    location = 'SW'
if x == 0 and y == 3:
    location = 'ES'
if x == 0 and y == 4:
    location = 'EW'
if x == 0 and y == 5:
    location = 'SW'
if x == 1 and y == 0:
    location = 'NS'
if x == 1 and y == 1:
    location = 'SE'
if x == 1 and y == 2:
    location =  'NW'
if x == 1 and y == 3:
    location = 'NS'
if x == 1 and y == 4:
    location =  'ES'
if x == 1 and y == 5:
    location = 'NSW'
if x == 2 and y == 0:
    location = 'NS'
if x == 2 and y == 1:
    location = 'N'
if x == 2 and y == 2:
    location = 'ES'
if x == 2 and y == 3:
    location = 'NSW'
if x == 2 and y == 4:
    location = 'N'
if x == 2 and y == 5:
    location = 'NS'
if x == 3 and y == 0:
    location = 'NE'
if x == 3 and y == 1:
    location = 'ESW'
if x == 3 and y == 2:
    location = 'NW'
if x == 3 and y == 3:
    location = 'NES'
if x == 3 and y == 4:
    location = 'EW'
if x == 3 and y == 5:
    location = 'NW'
if x == 4 and y == 0:
    location = 'SE'
if x == 4 and y == 1:
    location = 'NW'
if x == 4 and y == 2:
    location = 'S'
if x == 4 and y == 3:
    location = 'NS'
if x == 4 and y == 4:
    location = 'SE'
if x == 4 and y == 5:
    location = 'SW'
if x == 5 and y == 0:
    location = 'NE'
if x == 5 and y == 1:
    location = 'W'
if x == 5 and y == 2:
    location = 'NE'
if x == 5 and y == 3:
    location = 'NEW'
if x == 5 and y == 4:
    location = 'NW'
if x == 5 and y == 5:
    location = 'N'

print('Type START to start.')
start = input()
print('You are now at ' + str(x) + ', ' + str(y))
while start:
    if location == 'N':
        print('You can only go N.')
        direction = input()
        while direction:
            if direction == N:
                x = x + 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'E':
        print('You can only go E.')
        direction = input()
        while direction:
            if direction == E:
              x = x
              y = y + 1
              print('You are now at ' + str(x) + ', ' + str(y))
              break
            else:
                print('Invalid response. Please try again.')
    if location == 'S':
        print('You can only go S')
        direction = input()
        while direction:
            if direction == S:
                x = x - 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'W':
        print('You can only go W.')
        direction = input()
        while direction:
            if direction == W:
                x = x
                y = y - 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'NE':
        print('Pick a direction: N or E.')
        direction = input()
        while direction:
            if direction == N:
                x = x + 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == E:
              x = x
              y = y + 1
              print('You are now at ' + str(x) + ', ' + str(y))
              break
            else:
                print('Invalid response. Please try again.')
    if location == 'NS':
        print('Pick a direction: N or S.')
        direction = input()
        while direction:
            if direction == N:
                x = x + 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == S:
                x = x - 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'NW':
        print('Pick a direction: N or W.')
        direction = input()
        while direction:
            if direction == N:
                x = x + 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == W:
                x = x
                y = y - 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'ES':
        print('Pick a direction: E or S.')
        direction = input()
        while direction:
            if direction == E:
              x = x
              y = y + 1
              print('You are now at ' + str(x) + ', ' + str(y))
              break
            elif direction == S:
                x = x - 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'EW':
        print('Pick a direction: E or W.')
        direction = input()
        while direction:
            if direction == E:
              x = x
              y = y + 1
              print('You are now at ' + str(x) + ', ' + str(y))
              break
            elif direction == W:
                x = x
                y = y - 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'SW':
        print('Pick a direction: S or W.')
        direction = input()
        while direction:
            if direction == S:
                x = x - 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == W:
                x = x
                y = y - 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'NEW':
        print('Pick a direction: N, E, or W.')
        direction = input()
        while direction:
            if direction == N:
                x = x + 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == E:
              x = x
              y = y + 1
              print('You are now at ' + str(x) + ', ' + str(y))
              break
            elif direction == W:
                x = x
                y = y - 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'NSW':
        print('Pick a direction: N, S, or W.')
        direction = input()
        while direction:
            if direction == N:
                x = x + 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == S:
                x = x - 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == W:
                x = x
                y = y - 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'NES':
        print('Pick a direction: N, E, or S.')
        direction = input()
        while direction:
            if direction == N:
                x = x + 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == E:
                x = x
                y = y + 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == S:
                x = x - 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if location == 'ESW':
        print('Pick a direction: E, S. or W.')
        direction = input()
        while direction:
            if direction == E:
              x = x
              y = y + 1
              print('You are now at ' + str(x) + ', ' + str(y))
              break
            elif direction == S:
                x = x - 1
                y = y
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            elif direction == W:
                x = x
                y = y - 1
                print('You are now at ' + str(x) + ', ' + str(y))
                break
            else:
                print('Invalid response. Please try again.')
    if x == 5 and y == 5:
        print('You found the end! Congratulations!')
        print('Type DONE to claim your reward and end the game.')
        done = input()
        if done == 'DONE':
            print('You won $200,000,000!')
            break
            
