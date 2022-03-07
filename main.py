from environment.cli_sudoku import CLI_Sudoku
from agent.agent import Agent
from environment.sudokuController import SudokuController
import os

def Generate_Random_sudoku(sudoku_controller):
    sudoku_controller.setZeros()
    assignment = sudoku_controller.FullSudokuRandom()
    sudoku_controller.fillGrid(assignment)
    sudoku_controller.withdrawSudoku(99)

def Take_Sudoku_From_File(title):
    cli_sudoku.getSudokuFromFile(title)

if __name__ == '__main__':
    cli_sudoku = CLI_Sudoku()
    sudoku_controller = SudokuController(cli_sudoku)
    print("---------GAME MODE--------")
    print("- To generate a random grid press 1")
    print("- To generate your own grid enter there in the grid.txt file then type 2 (Warning: an empty box is represented by a 0)")
    choice = input('Enter your choice: ')
    if choice == 1:
        Generate_Random_sudoku(sudoku_controller)
    else :
        Take_Sudoku_From_File("grid")
    agent = Agent(sudoku_controller)
    print("---------BEFORE---------")
    cli_sudoku.DisplayGrid()
    assignment = agent.backtracking_search()
    sudoku_controller.fillGrid(assignment)
    print("---------AFTER---------")
    cli_sudoku.DisplayGrid()
