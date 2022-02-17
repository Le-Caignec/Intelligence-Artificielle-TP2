from Sudoku import Sudoku


if __name__ == '__main__':
    env = Sudoku()
    env.Random_sudoku(5)
    env.getSudokuFromText()
    env.DisplayGrid()