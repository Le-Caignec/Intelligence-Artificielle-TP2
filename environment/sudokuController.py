from random import randint, shuffle

class SudokuController:

    def __init__(self, cli_sudoku):
        self.cli_sudoku = cli_sudoku

    # this function get the cases with 0 as number
    def getZeros(self):
            listVar = []
            for x in range(9):
                for y in range(9):
                    if self.cli_sudoku.grid[x][y].number == 0:
                        listVar.append((x, y))
            return listVar
    
    # this function fill the grid with the values in assignment
    def fillGrid(self, assignement):
        for key in assignement:
            x = int(key[1])
            y = int(key[4])
            self.cli_sudoku.grid[x][y].number = assignement[key]
    
    # this function get the constraint from the cases in the column x
    def getConstraintX(self, x):
        L=[]
        for y in range(9):
            if self.cli_sudoku.grid[x][y].number != 0:
                L.append(self.cli_sudoku.grid[x][y].number)
        return L
    
    # this function get the constraint from the cases in the lign y
    def getConstraintY(self, y):
        L=[]
        for x in range(9):
            if self.cli_sudoku.grid[x][y].number != 0:
                L.append(self.cli_sudoku.grid[x][y].number)
        return L
    
    # this function get all the possible variables that can take the corresponding case
    def getDomain(self, var, assignement):
        x = var[0]
        y = var[1]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        Constraint = self.Merge(self.getConstraintX(x), self.getConstraintY(y))
        Constraint = self.Merge(Constraint, self.getConstraint(assignement, x, y))
        for value in Constraint:
            if value in numbers:
                numbers.remove(value)
        return numbers

    # a function that get all the values that are in L1 and in L2 without repeting them
    def Merge(self, L1, L2):
        L=L1[:]
        for val in L2:
            if val not in L1:
                L.append(val)
        return L

    # get the constraint from assignement
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

    # get the constraint from the 3x3 square containing the corresponding case
    def getSquareConstraint(self, assignement, x, y):
        Constraint = []
        xSquare = x//3
        ySquare = y//3
        for i in range(xSquare*3, xSquare*3+3):
            for j in range(ySquare*3, ySquare*3+3):
                if self.cli_sudoku.grid[i][j] != 0:
                    Constraint.append(self.cli_sudoku.grid[i][j].number)
        for key in assignement:
            if int(key[1])//3 == xSquare:
                if int(key[4])//3 == ySquare and assignement[key] not in Constraint:
                    Constraint.append(assignement[key])
        return Constraint

    # this function is used to remove values from a full sudoku (when it is created randomly)
    # the level is from 1 to 6 and the higher the level is, the more values are removed
    def withdrawSudoku(self, level):
        listValues = self.getNonZeros()
        if level < 1:
            level = 1
        elif level > 6:
            level = 6
        num = 40 + 5*level
        for k in range(num):
            i = randint(0, len(listValues) - 1)
            x = listValues[i][0]
            y = listValues[i][1]
            self.cli_sudoku.grid[x][y].number = 0
            listValues.pop(i)
    
    # get all the cases that has a number (different than 0)
    def getNonZeros(self):
        listVar = []
        for x in range(9):
            for y in range(9):
                if self.cli_sudoku.grid[x][y].number != 0:
                    listVar.append((x, y))
        return listVar

    # get the numbers of apparitions of all the numbers from 1 to 9
    def getWeightNumbers(self):
        dict = {}
        for i in range(9):
            dict[str(i+1)] = 0
        for var in self.getNonZeros():
            case = self.cli_sudoku.grid[var[0]][var[1]]
            dict[str(case.number)] += 1
        return dict

    # this function reset all the values of the sudoku to 0
    def setZeros(self):
        for x in range(9):
            for y in range(9):
                if self.cli_sudoku.grid[x][y].number != 0:
                    self.cli_sudoku.grid[x][y].number = 0

    # call the recursive function to get a random sudoku
    def FullSudokuRandom(self):
        return self.recursive_random_backtracking({})
    
    # this function is a recursive backtracking that assign random values to generate a random sudoku
    def recursive_random_backtracking(self, assignment):
        if self.isComplete(assignment):
            return assignment
        else:
            listVar = self.getZerosAssignment(assignment)
            var = listVar[0]
            domain = self.getDomain(var, assignment)
            shuffle(domain)
            #value = une valeur possible pour case
            for value in domain:
                assignment[str(var)] = value
                result = self.recursive_random_backtracking(assignment)
                if result != {}:
                    return result
                else:
                    del assignment[str(var)]
            return {}
    
    # get the cases that are not yet in assignement
    def getZerosAssignment(self, assignment):
            listVar = []
            for x in range(9):
                for y in range(9):
                    if str((x, y)) not in assignment:
                        listVar.append((x, y))
            return listVar

    # check if all the cases are in assignement 
    def isComplete(self, assignement):
        if len(assignement) < 81:
            return False
        else:
            return True 
