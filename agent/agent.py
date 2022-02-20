from xml import dom


class Agent:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        # listVar est la liste des coordonées qui ne sont pas remplis
        self.listVar = self.sudoku.getZeros()
        # numbersWeighted est un dictionnaire avec les nombres de 1 à 9.
        # il permet de connaitre de fois un numéro est présent dans le sudoku
        self.numbersWeighted = self.sudoku.getWeightNumbers()

    def backtracking_search(self):
        return self.recursive_backtracking({})
    
    def recursive_backtracking(self, assignment):
        if self.isComplete(assignment):
            return assignment
        else:
            var, domain = self.Select_variables(assignment)
            #value = une valeur possible pour case
            for value in domain:
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
        domain_min = self.sudoku.getDomain(self.listVar[0], assignement)
        min = len(domain_min)
        min_var = self.listVar[0]
        for var in self.listVar:
            domain = self.sudoku.getDomain(var, assignement)
            n= len(domain)
            if  n<min and str(var) not in assignement:
                domain_min = domain
                min = n
                min_var = var
        return min_var, domain_min

