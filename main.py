from environment.cli_sudoku import CLI_Sudoku
from agent.agent import Agent
from environment.sudokuController import SudokuController

def Generate_Random_sudoku(sudoku_controller):
    sudoku_controller.setZeros()
    assignment = sudoku_controller.FullSudokuRandom()
    sudoku_controller.fillGrid(assignment)
    sudoku_controller.withdrawSudoku(2)

def Take_Sudoku_From_File(title):
    cli_sudoku.getSudokuFromFile(title)

if __name__ == '__main__':
    cli_sudoku = CLI_Sudoku()
    sudoku_controller = SudokuController(cli_sudoku)
    print("-----------------------------GAME RULES-----------------------------")
    print("   * To generate a random grid press 1")
    print("   * To generate your own grid put it in the grid.txt file then press 2 (Warning: an empty box is represented by a 0)")
    print('')
    choice = input('Enter your choice: ')
    if choice == '1':
        Generate_Random_sudoku(sudoku_controller)
    else :
        Take_Sudoku_From_File("grid")
    agent = Agent(sudoku_controller)
    print(" ")
    print("---------BEFORE---------")
    print(" ")
    cli_sudoku.DisplayGrid()
    assignment = agent.backtracking_search()
    if assignment == {}:
        print(" ")
        print("The Sudoku is impossible, please try with another grid")
    else: 
        sudoku_controller.fillGrid(assignment)
        print(" ")
        print("---------AFTER---------")
        print(" ")
        cli_sudoku.DisplayGrid()
