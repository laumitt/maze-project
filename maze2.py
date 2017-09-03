Matrix = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
# a 5 by 5 matrix with each row numbers 0-5
Matrix[0][0] = "0110"
# at position 0, 0, you can't go north, you can go east, you can go south, you can't go west
Matrix[1][0] = "0101"
Matrix[2][0] = "0011"
Matrix[3][0] = "0110"
Matrix[4][0] = "0101"
Matrix[5][0] = "0011"
Matrix[0][1] = "1010"
Matrix[1][1] = "0110"
Matrix[2][1] = "1001"
Matrix[3][1] = "1010"
Matrix[4][1] = "0110"
Matrix[5][1] = "1011"
Matrix[0][2] = "1010"
Matrix[1][2] = "1000"
Matrix[2][2] = "0110"
Matrix[3][2] = "1011"
Matrix[4][2] = "1000"
Matrix[5][2] = "1010"
Matrix[0][3] = "1100"
Matrix[1][3] = "0111"
Matrix[2][3] = "1001"
Matrix[3][3] = "1110"
Matrix[4][3] = "0101"
Matrix[5][3] = "1001"
Matrix[0][4] = "0110"
Matrix[1][4] = "1001"
Matrix[2][4] = "0010"
Matrix[3][4] = "1010"
Matrix[4][4] = "0110"
Matrix[5][4] = "0011"
Matrix[0][5] = "1100"
Matrix[1][5] = "0001"
Matrix[2][5] = "1100"
Matrix[3][5] = "1101"
Matrix[4][5] = "1001"
Matrix[5][5] = "1000"
# defining each position's possible movement directions

#print(Matrix)
# prints everything

##if Matrix[0][0][1] == "1":
##    print("true")
### check if the second digit of Matrix[0][0], the starting position, is a 1. If it is, you can move east.
##if Matrix[0][0][2] == "1":
##    print("true again")
### check if the third digit of [0][0] is a 1. If it is, you can move south.

x = 0
y = 0
position = Matrix[x][y]
# start at 0,0
print("Welcome to The Maze. Your objective is to reach 5, 5.")
print("You are now at " + str(x) + ", " + str(y))
# say where you start 
while -1 < x < 6 and -1 < y < 6:
    if position[0] == "1":
        print("You can GO NORTH.")
    if position[1] == "1":
        print("You can GO EAST.")
    if position[2] == "1":
        print("You can GO SOUTH.")
    if position[3] == "1":
        print("You can GO WEST.")
    # say where you can go
    print("Choose a direction to go.")
    move = input()
    # choose a direction
    if move == "GO NORTH" and position[0] == "1":
    # if you said go north and you can go north
        y = y - 1
        # move the y coordinate 1 north
        position = Matrix[x][y]
        # set your position
        print("You are now at " + str(x) + ", " + str(y))
        # say your new position
    elif move == "GO EAST" and position[1] == "1":
        x = x + 1
        position = Matrix[x][y]
        print("You are now at " + str(x) + ", " + str(y))
    elif move == "GO SOUTH" and position[2] == "1":
        y = y + 1
        position = Matrix[x][y]
        print("You are now at " + str(x) + ", " + str(y))
    elif move == "GO WEST" and position[3] == "1":
        x = x - 1
        position = Matrix[x][y]
        print("You are now at " + str(x) + ", " + str(y))
    if x == 5 and y == 5:
    # if you get to the bottom right corner
        print("Congrats! You won!")
        # you won
        break
        # end the program
