from environment.cli_sudoku import Sudoku
from agent.agent import Agent


if __name__ == '__main__':
    env = Sudoku()
    agent = Agent(env)
    env.getSudokuFromText()
    print("---------AVANT---------")
    env.DisplayGrid()
    assignment = agent.backtracking_search()
    print(assignment)
    env.fillGrid(assignment)
    print("---------APRES---------")
    env.DisplayGrid()