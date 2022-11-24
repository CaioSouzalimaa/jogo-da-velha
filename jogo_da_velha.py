empty = "  "
token = [" X ", " O "]

def criarBoard():
  board = [
    [empty, empty, empty],
    [empty, empty, empty],
    [empty, empty, empty]
  ]
  return board

def printBoard(board):
  for i in range(3):
      print("|".join(board[i]))
      if(i < 2):
        print("-----------")

def getInputValido(mensagem):
  try:
    n = int(input(mensagem))
    if(n >= 1 and n <=3):
      return n - 1
    else:
      print("Número precisa ser entre 1 e 3")
      return getInputValido(mensagem)
  except:
    print("Valor inválido")
    return getInputValido(mensagem)

def verificaMovimento(board, linha, coluna):
  if(board[linha][coluna] == empty):
    return True

def fazMovimento(board , linha, coluna, jogador):
  board[linha][coluna] = token[jogador]

def verificaGanhador(board):
  for i in range(3):
    if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != empty):
      return board[i][0]

  for i in range(3):
    if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != empty):
      return board[0][i]
  
  if(board[0][0] != empty and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
    return board[0][0]
  
  if(board[0][2] != empty and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
    return board[0][2]

  for i in range(3):
    for j in range(3):
      if(board[i][j] == empty):
        return False

  return 'Empate'