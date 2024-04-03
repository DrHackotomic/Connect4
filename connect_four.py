import random

# Initialize the board
board = [[' ' for _ in range(7)] for _ in range(6)]


# Function to print the board
def print_board(board):
  for row in board:
    print('|'.join(row))
  print('-' * 13)


# Function to check if a move is valid
def is_valid(board, col):
  return board[0][col] == ' '


# Function to insert a piece into the board
def insert_piece(board, row, col, piece):
  board[row][col] = piece


# Function to get the next open row in a column
def get_next_open_row(board, col):
  for r in range(5, -1, -1):
    if board[r][col] == ' ':
      return r


# Function to check for a win
def check_win(board, piece):
  # Check horizontal locations for win
  for row in range(6):
    for col in range(4):
      if board[row][col] == piece and board[row][col + 1] == piece and board[
          row][col + 2] == piece and board[row][col + 3] == piece:
        return True

  # Check vertical locations for win
  for col in range(7):
    for row in range(3):
      if board[row][col] == piece and board[row + 1][col] == piece and board[
          row + 2][col] == piece and board[row + 3][col] == piece:
        return True

  # Check diagonals for win
  for row in range(3):
    for col in range(4):
      if board[row][col] == piece and board[row + 1][
          col + 1] == piece and board[row + 2][col + 2] == piece and board[
              row + 3][col + 3] == piece:
        return True

  for row in range(3, 6):
    for col in range(4):
      if board[row][col] == piece and board[row - 1][
          col + 1] == piece and board[row - 2][col + 2] == piece and board[
              row - 3][col + 3] == piece:
        return True

  return False


# Minimax function with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizingPlayer):
  if depth == 0 or check_win(board, 'X') or check_win(board, 'O'):
    return (None, -1) if check_win(
        board, 'O') else (None, 1) if check_win(board, 'X') else (None, 0)

  if maximizingPlayer:
    maxEval = float('-inf')
    bestMove = None
    for col in range(7):
      if is_valid(board, col):
        row = get_next_open_row(board, col)
        insert_piece(board, row, col, 'X')
        eval = minimax(board, depth - 1, alpha, beta, False)[1]
        board[row][col] = ' '
        alpha = max(alpha, eval)
        if eval > maxEval:
          maxEval = eval
          bestMove = col
        if beta <= alpha:
          break
    return (bestMove, maxEval)

  else:
    minEval = float('inf')
    bestMove = None
    for col in range(7):
      if is_valid(board, col):
        row = get_next_open_row(board, col)
        insert_piece(board, row, col, 'O')
        eval = minimax(board, depth - 1, alpha, beta, True)[1]
        board[row][col] = ' '
        beta = min(beta, eval)
        if eval < minEval:
          minEval = eval
          bestMove = col
        if beta <= alpha:
          break
    return (bestMove, minEval)


# Main game loop
def startGame():
  turn = 'X' if random.randint(0, 1) == 0 else 'O'
  print("Player 1 is X and Player 2 is O.")
  print("Player", turn, "goes first.")
  while True:
    print_board(board)
    if turn == 'X':
      col = int(input("Enter the column number to drop your piece (0-6): "))
      if is_valid(board, col):
        row = get_next_open_row(board, col)
        insert_piece(board, row, col, 'X')
        if check_win(board, 'X'):
          print_board(board)
          print("Player X wins!")
          break
        turn = 'O'
      else:
        print("Invalid move, try again.")
    else:
      col, _ = minimax(board, 4, float('-inf'), float('inf'), False)
      if col is not None:
        row = get_next_open_row(board, col)
        insert_piece(board, row, col, 'O')
        if check_win(board, 'O'):
          print_board(board)
          print("Player O wins!")
          break
        turn = 'X'


# Start the game
startGame()
