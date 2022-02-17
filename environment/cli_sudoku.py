from asyncio import format_helpers
from random import random,randint
from dataclasses import dataclass


@dataclass
class Case:
    number: int = 0
    x_position: int = 0
    y_position: int = 0


class Sudoku:

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
                    print("| " + self.getNumber(x_position, y_position) + " ",
                      end='')
                    bool_x=False
                else:
                    print(self.getNumber(x_position, y_position) + " ",
                      end='')
            print("")

    def getNumber(self, x,y):
        num = self.grid[x][y].number
        if num !=0 :
            return str(num)
        else:
            return " "

    def getSudokuFromText(self):
        file = open("grille.txt", "r")
        line = file.readline()
        for y in range(9):
            for x in range(9):
                self.grid[x][y].number = int(line[x])
            line = file.readline()
    
    def getZeros(self):
        listVar = []
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    listVar.append((x,y))
        return listVar
    
    def fillGrid(self, assignement):
        for key in assignement:
            x = int(key[1])
            y = int(key[3])
            self.grid[x][y]=assignement[key]
        

    # def Random_sudoku(self, level):
    #     file = open("sudoku.txt", "w")
    #     numbers_x = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
    #     numbers_y = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
    #     for y in range(9):
    #         line = ""
    #         for x in range(9):
    #             bool1 = True
    #             numbers = self.Merge(numbers_x[x], numbers_y[y])
    #             print(numbers)
    #             while bool1:
    #                 i = randint(0,len(numbers)-1)
    #                 index = numbers_y[y].index(numbers[i])
    #                 Test = numbers_y[y][:index] + numbers_y[y][index:]
    #                 bool2=True
    #                 for j in range(x, 9) and bool2:
    #                     if not self.contains(numbers_x[j],Test):
    #                         bool2=False
    #                 if bool2:
    #                     line += str(numbers[i])
    #                     numbers_x[x].remove(numbers[i])
    #                     numbers_y[y].remove(numbers[i])
    #                     bool1=False
    #         file.write(f"{line}\n")
        
    # def Merge(self, list1, list2):
    #     L=[]
    #     for el in list1:
    #         if el in list2:
    #             L.append(el)
    #     return L
    
    # def contains(self, bigList, tinyList):
    #     # a faire
    #     return True