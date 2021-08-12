# Import
from sudoku import Sudoku

# Backtrack solver class
class BacktrackSolver:
  # Constructor
  def __init__(self, matrix):
    self.sudoku = Sudoku(matrix)

  # Find next empty position in board
  def nextEmpty(self):
    for k in range(81):
      if self.sudoku.board[k] == 0:
        return k

    return 81

  # Solve sudoku
  def solve(self):
    k = self.nextEmpty()
    if k == 81:
      print(f'Solved? {self.sudoku.isSolved()}\n')
      return self.sudoku.display()

    for v in range(1, 10):
      self.sudoku.add(k // 9, k % 9, v)
      if self.sudoku.isValid():
        self.solve()
      self.sudoku.remove(k // 9, k % 9)

# Testing
if __name__ == '__main__':
  sample = [
    0, 9, 0, 0, 0, 6, 0, 4, 0,
    0, 0, 5, 3, 0, 0, 0, 0, 8,
    0, 0, 0, 0, 7, 0, 2, 0, 0,
    0, 0, 1, 0, 5, 0, 0, 0, 3,
    0, 6, 0, 0, 0, 9, 0, 7, 0,
    2, 0, 0, 0, 8, 4, 1, 0, 0,
    0, 0, 3, 0, 1, 0, 0, 0, 0,
    8, 0, 0, 0, 0, 2, 5, 0, 0,
    0, 5, 0, 4, 0, 0, 0, 8, 0
  ]
  solver = BacktrackSolver(sample)
  solver.solve()
