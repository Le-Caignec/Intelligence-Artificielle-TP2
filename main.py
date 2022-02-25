from environment.cli_sudoku import CLI_Sudoku
from agent.agent import Agent
from environment.sudokuController import SudokuController
import os

def getInitialSudoku(cli_sudoku, sudoku_controller, title):
    filesize = os.path.getsize("{}.txt".format(title))
    if filesize == 0:
        sudoku_controller.FullSudokuRandom_2()
    cli_sudoku.getSudokuFromFile()



if __name__ == '__main__':
    cli_sudoku = CLI_Sudoku()
    sudoku_controller = SudokuController(cli_sudoku)
    getInitialSudoku(cli_sudoku, sudoku_controller, "grille")    
    sudoku_controller.withdrawSudoku(2)
    agent = Agent(sudoku_controller)
    print("---------AVANT---------")
    cli_sudoku.DisplayGrid()
    assignment = agent.backtracking_search()
    cli_sudoku.fillGrid(assignment)
    print("---------APRES---------")
    cli_sudoku.DisplayGrid()