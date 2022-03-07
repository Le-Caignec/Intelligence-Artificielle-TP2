
class Agent:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        # listVar is the list of coordinates that are not in the sudoku nor in assignment
        self.listVar = self.sudoku.getZeros()
        # numbersWeighted is a dictionnary with numbers from 1 to 9
        # it contains the numbers of apparitions of those numbers
        self.numbersWeighted = self.sudoku.getWeightNumbers()

    # this fucction start the recursive backtracking
    def backtracking_search(self):
        return self.recursive_backtracking({})
    
    # this function is a CSP backtracking with LCV and MRV
    def recursive_backtracking(self, assignment):
        # if the sudoku is complete, it returns assignement
        if self.isComplete():
            return assignment
        else:
            # we get the most appropriate case with the domain of value it can take
            var, domain = self.Select_variables(assignment)
            # we sort the domain so that the most appropriate values are at the beggining of the list 
            domain = self.sortDomain(domain)
            for value in domain:
                assignment[str(var)] = value
                self.numbersWeighted[str(value)]+=1
                self.listVar.remove(var)
                result = self.recursive_backtracking(assignment)
                # if result is not empty, the sudoku is complete
                if result != {}:
                    return result
                # otherwise, the value is not correct and we select the next one
                # we update variables that depends on the value selected.
                else:
                    del assignment[str(var)]
                    self.numbersWeighted[str(value)]-=1
                    self.listVar.append(var)
            return {}
    
    # this function check if listVar has variables
    # if not the sudoku is complete
    def isComplete(self):
        if self.listVar != []:
            return False
        else:
            return True
    
    # 
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

    def sortDomain(self, domain):
        if domain == []:
            return domain
        new_domain = [domain[0]]
        n = len(domain)
        for i in range(1,n):
            bool = True
            for j in range(len(new_domain)):
                if self.numbersWeighted[str(domain[i])]>self.numbersWeighted[str(new_domain[j])] and bool:
                    new_domain=new_domain[:j]+[domain[i]]+new_domain[j:]
                    bool = False
            if bool:
                new_domain.append(domain[i])
                
        return new_domain
