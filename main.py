from environment.Sudoku import Sudoku
from agent.csp import Agent


if __name__ == '__main__':
    env = Sudoku()
    agent = Agent(env)
    env.getSudokuFromText()
    print("---------AVANT---------")
    env.DisplayGrid()
    assignment = agent.backtracking_search()
    env.fillGrid(assignment)
    print("---------APRES---------")
    env.DisplayGrid()