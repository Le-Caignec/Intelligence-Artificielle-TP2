from random import randint, shuffle

class SudokuController:

    def __init__(self, cli_sudoku):
        self.cli_sudoku = cli_sudoku

    def getZeros(self):
            listVar = []
            for x in range(9):
                for y in range(9):
                    if self.cli_sudoku.grid[x][y].number == 0:
                        listVar.append((x,y))
            return listVar
        
    def fillGrid(self, assignement):
        for key in assignement:
            x = int(key[1])
            y = int(key[4])
            self.cli_sudoku.grid[x][y].number = assignement[key]
    
    def getConstraintX(self,x):
        L=[]
        for y in range(9):
            if self.cli_sudoku.grid[x][y].number != 0:
                L.append(self.cli_sudoku.grid[x][y].number)
        return L
    
    def getConstraintY(self,y):
        L=[]
        for x in range(9):
            if self.cli_sudoku.grid[x][y].number != 0:
                L.append(self.cli_sudoku.grid[x][y].number)
        return L
    
    def getDomain(self, var, assignement):
        ## la fct intéréssante
        x = var[0]
        y = var[1]
        numbers = [1,2,3,4,5,6,7,8,9]
        Constraint = self.Merge(self.getConstraintX(x),self.getConstraintY(y))
        Constraint = self.Merge(Constraint, self.getConstraint(assignement, x, y))
        for value in Constraint:
            if value in numbers:
                numbers.remove(value)
        return numbers

    def Merge(self, L1, L2):
        L=L1[:]
        for val in L2:
            if val not in L1:
                L.append(val)
        return L
    
    def getConstraint(self, assignement, x, y):
        Constraint = []
        for key in assignement:
            if int(key[1]) == x:
                Constraint.append(assignement[key])
            elif int(key[4]) == y and assignement[key] not in Constraint:
                Constraint.append(assignement[key])
        SquareConstraint = self.getSquareConstraint(assignement, x, y)
        for el in SquareConstraint:
            if el not in Constraint:
                Constraint.append(el)
        return Constraint

    def getSquareConstraint(self, assignement, x, y):
        Constraint = []
        xSquare=x//3
        ySquare=y//3
        for i in range(xSquare*3,xSquare*3+3):
            for j in range(ySquare*3,ySquare*3+3):
                if self.cli_sudoku.grid[i][j] != 0:
                    Constraint.append(self.cli_sudoku.grid[i][j].number)
        for key in assignement:
            if int(key[1])//3 == xSquare:
                if int(key[4])//3 == ySquare and assignement[key] not in Constraint:
                    Constraint.append(assignement[key])
        return Constraint

    def withdrawSudoku(self, level):
        listValues = self.getNonZeros()
        if level < 1:
            level =1
        elif level > 6:
            level = 6
        num = 40 + 5*level
        for k in range(num):
            i = randint(0, len(listValues) - 1)
            x = listValues[i][0]
            y = listValues[i][1]
            self.cli_sudoku.grid[x][y].number = 0
            listValues.pop(i)
    
    def getNonZeros(self):
        listVar = []
        for x in range(9):
            for y in range(9):
                if self.cli_sudoku.grid[x][y].number != 0:
                    listVar.append((x,y))
        return listVar
    
    def FullSudokuRandom(self):
        for i in range(0,81):
            print(i)
            x=i//9 
            y=i%9
            #find next empty cell
            if self.cli_sudoku.grid[x][y].number == 0:
                numbers = self.getDomain((x,y),{})
                shuffle(numbers)
                for number in numbers:
                    self.cli_sudoku.grid[x][y].number = number
                    if self.getZeros == []:
                        return True
                    else:
                        if self.FullSudokuRandom():
                            #if the grid is full
                            return True
                break
        self.cli_sudoku.grid[x][y].number = 0  
        return False  

    def getWeightNumbers(self):
        dict = {}
        for i in range(9):
            dict[str(i+1)] = 0
        for var in self.getNonZeros():
            case = self.cli_sudoku.grid[var[0]][var[1]]
            dict[str(case.number)]+=1
        return dict
