from environment.Sudoku import Sudoku


if __name__ == '__main__':
    env = Sudoku()
    env.getSudokuFromText()
    env.DisplayGrid()