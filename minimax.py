from jogo_da_velha import empty, token, verificaGanhador

def movimentoIA(board, player):
  possibilidades = getPosicoes(board)
  melhorValor = None
  melhorMovimento = None
  for possibilidade in possibilidades:
    board[possibilidade[0]][possibilidade[1]] = token[player]
    valor = minimax(board, player)
    board[possibilidade[0]][possibilidade[1]] = empty

    if melhorValor is None:
      melhorValor = valor
      melhorMovimento = possibilidade
    elif player == 0 and valor > melhorValor:
      melhorValor = valor
      melhorMovimento = possibilidade
    elif player == 1 and valor < melhorValor:
      melhorValor = valor
      melhorMovimento = possibilidade

  return melhorMovimento[0], melhorMovimento[1]

def getPosicoes(board):
  posicoes = []
  for i in range(3):
    for j in range(3):
      if(board[i][j] == empty):
        posicoes.append([i, j])
  return posicoes

score = {
  ' X ': 1,
  ' O ': -1,
  'Empate': 0
}

def minimax(board, player):
  ganhador = verificaGanhador(board)
  if ganhador:
    return score[ganhador]

  player = (player + 1) % 2

  possibilidades = getPosicoes(board)
  melhorValor = None
  for possibilidade in possibilidades:
    board[possibilidade[0]][possibilidade[1]] = token[player]
    valor = minimax(board, player)
    board[possibilidade[0]][possibilidade[1]] = empty

    if melhorValor is None:
      melhorValor = valor
    elif player == 0 and valor > melhorValor:
      melhorValor = valor
    elif player == 1 and valor < melhorValor:
      melhorValor = valor


  return melhorValor