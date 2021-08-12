# Sudoku class
class Sudoku:
  # Constructor
  def __init__(self, matrix):
    self.board = self.load(matrix)

  # Load board with matrix
  def load(self, matrix):
    if (self.isMatrixValid(matrix)):
      return matrix
    else:
      return [
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0
      ]

  # Display board
  def display(self):
    for j in range(9):
      str = ''
      for i in range(9):
        if self.board[j * 9 + i] > 0:
          str += f'{self.board[j * 9 + i]} '
        else:
          str += '- '
      print(str)
    print('\n')

  # Add value to position in board
  def add(self, row, col, value):
    if row not in range(9) or col not in range(9) or value not in range(1, 10):
      return

    self.board[row * 9 + col] = value

  # Remove value from position in board
  def remove(self, row, col):
    if row not in range(9) or col not in range(9):
      return

    self.board[row * 9 + col] = 0

  # Check matrix validity
  def isMatrixValid(self, matrix):
    if len(matrix) != 81:
      return False

    for v in matrix:
      if v not in range(10):
        return False

    return True

  # Check board validity
  def isValid(self):
    rv = self.isRowValid()
    cv = self.isColumnValid()
    sv = self.isSquareValid()

    if rv and cv and sv:
      return True
    
    return False

  # Check board completion
  def isSolved(self):
    if not self.isValid():
      return False

    for k in range(81):
      if self.board[k] == 0:
        return False

    return True


  # Check row validity
  def isRowValid(self):
    for j in range(9):
      row = []
      for i in range(9):
        row.append(self.board[j * 9 + i])

      for v in range(1, 10):
        if row.count(v) > 1:
          return False

    return True

  # Check column validity
  def isColumnValid(self):
    for i in range(9):
      col = []
      for j in range(9):
        col.append(self.board[j * 9 + i])

      for v in range(1, 10):
        if col.count(v) > 1:
          return False

    return True

  # Check square validity
  def isSquareValid(self):
    for c in range(9):
      sq = []
      for k in range(9):
        sq.append(self.board[((c // 3) * 3 + (k // 3)) * 9 + ((c % 3) * 3 + (k % 3))])

      for v in range(1, 10):
        if sq.count(v) > 1:
          return False

    return True

# Testing
if __name__ == '__main__':
  sample = [
    1, 4, 5, 6, 2, 7, 8, 9, 3,
    2, 9, 3, 4, 1, 8, 6, 7, 5,
    6, 7, 8, 3, 9, 5, 1, 2, 4,
    5, 2, 7, 1, 6, 3, 9, 4, 8,
    4, 1, 9, 8, 5, 2, 7, 3, 6,
    3, 8, 6, 7, 4, 9, 2, 5, 1,
    9, 6, 2, 5, 3, 1, 4, 0, 7,
    8, 3, 4, 9, 7, 6, 5, 1, 2,
    7, 5, 1, 2, 8, 4, 3, 6, 9
  ]
  sudoku = Sudoku(sample)
  sudoku.display()
  print(sudoku.isSolved())
  sudoku.add(6, 7, 8)
  sudoku.display()
  print(sudoku.isSolved())
  sudoku.remove(4, 5)
  sudoku.display()
  print(sudoku.isSolved())
