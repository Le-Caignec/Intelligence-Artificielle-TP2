from asyncio import format_helpers
from random import random,randint, shuffle
from dataclasses import dataclass

@dataclass
class Case:
    number: int = 0
    x_position: int = 0
    y_position: int = 0

class CLI_Sudoku:

    def __init__(self):
        self.grid = [[Case(0, k, i) for i in range(9)] for k in range(9)]

    # Function that enable to display the actual grid
    def DisplayGrid(self):
        for y_position in range(9):
            bool_y=True
            for x_position in range(9):
                bool_x=True
                if (y_position) % 3 == 0 and bool_y and y_position !=0:
                    print("---------------------")
                    bool_y=False
                if (x_position) % 3 == 0 and bool_x and x_position!=0:
                    print("| " + self.displayNumber(x_position, y_position) + " ",
                      end='')
                    bool_x=False
                else:
                    print(self.displayNumber(x_position, y_position) + " ",
                      end='')
            print("")

    def displayNumber(self, x,y):
        num = self.grid[x][y].number
        if num !=0 :
            return str(num)
        else:
            return " "

    def getSudokuFromFile(self):
        file = open("grille.txt", "r")
        line = file.readline()
        for y in range(9):
            for x in range(9):
                self.grid[x][y].number = int(line[x])
            line = file.readline()
    
    