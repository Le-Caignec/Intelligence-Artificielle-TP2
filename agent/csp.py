<<<<<<< Updated upstream
=======

from asyncio import constants
from sqlalchemy import Constraint


>>>>>>> Stashed changes
class Agent:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.listVar = self.sudoku.getZeros()

    def backtracking_search(self):
        return self.recursive_backtracking({})
    
    def recursive_backtracking(self, assignment):
        if self.isComplete(assignment):
            return assignment
        else:
            var = self.Select_variables(assignment)
            for value in self.getDomain(var, assignment):
                    assignment[str(var)] = value
                    result = self.recursive_backtracking(assignment)
                    if result != {}:
                        return result
                    else:
                        assignment.remove[str(var)]
            return {}
    
    def isComplete(self, assignement):
        for var in self.listVar:
            if str(var) not in assignement:
                return False
        return True
    
    def Select_variables(self, assignement):
        for var in self.listVar:
            if str(var) not in assignement:
                return var

    def getDomain(self, var, assignement):
        ## la fct intéréssante
        Constraint = []
        x = var[0]
        y = var[1]
        numbers = [1,2,3,4,5,6,7,8,9]
        Constraint = self.Merge(Constraint,self.sudoku.getConstraintX(x))
        Constraint = self.Merge(Constraint,self.sudoku.getConstraintY(y))
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
            elif int(key[3]) == y:
                Constraint.append(assignement[key])
        return Constraint
