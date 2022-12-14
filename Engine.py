class gameState():
  def __init__(self):
    self.board = [[0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0]]
    self.redTurn = True
    self.rowCounter = [5, 5, 5, 5, 5, 5, 5]
    self.moveLog = [] #move log used for the undoMove method
    self.win = False
    self.turns = len(self.board) * len(self.board[0])
    self.winningCoords = []
  
  def allMoves(self):
    moves = []
    if not self.win:
      for i in range(7):
        if self.rowCounter[i] >= 0:
          moves.append(i)
    return(moves)
  
  def move(self, column):
    if column <= 6 and column >= 0:
      if self.rowCounter[column] >= 0:
        if self.redTurn:
          self.board[self.rowCounter[column]][column] = 1
        else:
          self.board[self.rowCounter[column]][column] = 2
        self.rowCounter[column] -= 1
        self.redTurn = not self.redTurn
        self.moveLog.append(column)
        self.win = self.isWin(column)
        self.turns -= 1
        return True
    return False
    
        
  def undoMove(self):
    pop = self.moveLog.pop()
    self.board[self.rowCounter[pop] + 1][pop] = 0
    self.rowCounter[pop] += 1
    self.redTurn = not self.redTurn
    if self.win:
      self.win = False
    self.turns += 1

  def isWin(self, column):
    #done = False
    diagonalLefts, verticals, horizontals, diagonalRights = 0, 0, 0, 0
    piece = self.board[self.rowCounter[column] + 1][column]
    row = self.rowCounter[column] + 1

    winningCoords = [(row, column)]
    # Horizonals:
    positiveDir, negativeDir = False, False
    col = 1
    while (positiveDir == False or negativeDir == False) and horizontals < 3:       
      if negativeDir == False:
        if column - col >= 0:
          if piece == self.board[row][column - col]:
            winningCoords.append((row, column-col))
            horizontals += 1
          else:
            negativeDir = True
        else: 
          negativeDir = True
          
      if positiveDir == False:
        if column + col <= 6:
          if piece == self.board[row][column + col]:
            winningCoords.insert(0, (row, column+col))
            horizontals += 1
          else:
            positiveDir = True
        else:
          positiveDir = True
      col += 1
    if horizontals >= 3:
      self.winningCoords = winningCoords
      return True

    winningCoords = [(row,column)] 
    # Verticals:  
    negativeDir = False
    r = 1
    while negativeDir == False and verticals < 3:
      if negativeDir == False:
        if row + r <= 5:
          if piece == self.board[row + r][column]:
            winningCoords.append((row+r, column))
            verticals += 1
          else:
            negativeDir = True
        else:
          negativeDir = True
      r += 1
    if verticals >= 3:
      self.winningCoords = winningCoords
      return True

    winningCoords = [(row,column)]
    # diagonalLefts:
    positiveDir, negativeDir = False, False
    r = 1
    col = 1
    while (positiveDir == False or negativeDir == False) and diagonalLefts < 3:  
      if positiveDir == False:
        if column - col >= 0 and row - r >= 0:
          if piece == self.board[row - r][column - col]:
            winningCoords.insert(0, (row-r, column-col))
            diagonalLefts += 1
          else:
            positiveDir = True
        else:
            positiveDir = True

      if negativeDir == False:
        if row + r <= 5 and column + col <= 6:
          if piece == self.board[row + r][column + col]:
            winningCoords.append((row+r, column+col))
            diagonalLefts += 1
          else:
            negativeDir = True
        else:
            negativeDir = True
      r += 1
      col += 1
    if diagonalLefts >= 3:
      self.winningCoords = winningCoords
      return True

    winningCoords = [(row,column)]
    # diagonalRights:
    positiveDir, negativeDir = False, False
    r = 1
    col = 1
    while (positiveDir == False or negativeDir == False) and diagonalRights < 3:
      if negativeDir == False:
        if column - col >= 0 and row + r <= 5:
          if piece == self.board[row + r][column - col]:
            winningCoords.insert(0, (row+r, column-col))
            diagonalRights += 1
          else:
            negativeDir = True
        else:
            negativeDir = True
  
      if positiveDir == False:
        if row - r >= 0 and column + col <= 6:
          if piece == self.board[row - r][column + col]:
            winningCoords.append((row-r, column+col))
            diagonalRights += 1
          else:
            positiveDir = True
        else:
            positiveDir = True
      r += 1
      col += 1
    if diagonalRights >= 3:
      self.winningCoords = winningCoords
      return True
    return False
