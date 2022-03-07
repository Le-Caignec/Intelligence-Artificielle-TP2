from environment.cli_sudoku import CLI_Sudoku
from agent.agent import Agent
from environment.sudokuController import SudokuController
import os

def getInitialSudoku(cli_sudoku, sudoku_controller, title):
    filesize = os.path.getsize("{}.txt".format(title))
    if filesize == 0:
        sudoku_controller.setZeros()
        assignment = sudoku_controller.FullSudokuRandom()
        sudoku_controller.fillGrid(assignment)
    else : cli_sudoku.getSudokuFromFile(title)



if __name__ == '__main__':
    cli_sudoku = CLI_Sudoku()
    sudoku_controller = SudokuController(cli_sudoku)
    getInitialSudoku(cli_sudoku, sudoku_controller, "empty")
    print("---------FULL--------")
    cli_sudoku.DisplayGrid()
    sudoku_controller.withdrawSudoku(99)
    agent = Agent(sudoku_controller)
    print("---------AVANT---------")
    cli_sudoku.DisplayGrid()
    assignment = agent.backtracking_search()
    sudoku_controller.fillGrid(assignment)
    print("---------APRES---------")
    cli_sudoku.DisplayGrid()