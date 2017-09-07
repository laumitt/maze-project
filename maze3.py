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
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = Matrix[self.x][self.y]
    def check(self):
        if self.position[0] == "1":
            print("You can GO NORTH.")
        if self.position[1] == "1":
            print("You can GO EAST.")
        if self.position[2] == "1":
            print("You can GO SOUTH.")
        if self.position[3] == "1":
            print("You can GO WEST.")
        # say where you can go
    def movement(self, move):
        self.x
        self.y
        self.position
        if move == "GO NORTH" and self.position[0] == "1":
        # if you said go north and you can go north
            self.y = self.y - 1
            # move the y coordinate 1 north
            self.position = Matrix[self.x][self.y]
            # set your position
            print("You are now at " + str(self.x) + ", " + str(self.y))
            # say your new position
        elif move == "GO EAST" and self.position[1] == "1":
            self.x = self.x + 1
            self.position = Matrix[self.x][self.y]
            print("You are now at " + str(self.x) + ", " + str(self.y))
        elif move == "GO SOUTH" and self.position[2] == "1":
            self.y = self.y + 1
            self.position = Matrix[self.x][self.y]
            print("You are now at " + str(self.x) + ", " + str(self.y))
        elif move == "GO WEST" and self.position[3] == "1":
            self.x = self.x - 1
            self.position = Matrix[self.x][self.y]
            print("You are now at " + str(self.x) + ", " + str(self.y))

if __name__ == "__main__":
    maze = Maze()
    print("Welcome to The Maze. Your objective is to reach 5, 5.")
    print("You are now at " + str(maze.x) + ", " + str(maze.y))
    game = "inProgress"
    # say where you start
    while game == "inProgress":
        maze.check()
        move = input()
        maze.movement(move);
        if maze.x == 5 and maze.y == 5:
        # if you get to the bottom right corner
            print("Congrats! You won!")
            game = "won"
            # you won
            break
            # end program
