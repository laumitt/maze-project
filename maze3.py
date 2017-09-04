Matrix = [["0110", "1010", "1010", "1100", "0110", "1100"],
          ["0101", "0110", "1000", "0111", "1001", "0001"],
          ["0011", "1001", "0110", "1001", "0010", "1100"],
          ["0110", "1010", "1011", "1110", "1010", "1101"],
          ["0101", "0110", "1000", "0101", "0110", "1001"],
          ["0011", "1011", "1010", "1001", "0011", "1000"]]
# a  6 by 6 matrix with each row numbered 0-5
# defines each position's possible movement directions
# at position 0, 0, you can't go north, you can go east, you can go south, you can't go west
class Maze:
    global x
    global y
    global position
    def check(position):
        if position[0] == "1":
            print("You can GO NORTH.")
        if position[1] == "1":
            print("You can GO EAST.")
        if position[2] == "1":
            print("You can GO SOUTH.")
        if position[3] == "1":
            print("You can GO WEST.")
        # say where you can go
    def movement(move):
        global x
        global y
        global position
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

if __name__ == "__main__":
    x, y = 0, 0
    position = Matrix[x][y]
    print("Welcome to The Maze. Your objective is to reach 5, 5.")
    print("You are now at " + str(x) + ", " + str(y))
    game = "inProgress"
    # say where you start
    while game == "inProgress":
        Maze.check(Matrix[x][y])
        move = input()
        Maze.movement(move);
        if x == 5 and y == 5:
        # if you get to the bottom right corner
            print("Congrats! You won!")
            game = "won"
            # you won
            break
            # end program
