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
            #value = une valeur possible pour case
            for value in self.sudoku.getDomain(var, assignment):
                assignment[str(var)] = value
                result = self.recursive_backtracking(assignment)
                if result != {}:
                    return result
                else:
                    del assignment[str(var)]
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

