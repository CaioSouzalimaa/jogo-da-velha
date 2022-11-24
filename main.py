from jogo_da_velha import criarBoard, fazMovimento, getInputValido, printBoard, verificaGanhador, verificaMovimento, token
from minimax import movimentoIA

player = 0
board = criarBoard()
ganhador = verificaGanhador(board)

modo = ''
while modo != '1' and modo != '2':
  modo = input("\nVocê quer jogar contra a IA digite 1, se quiser ver IA vs IA digite 2: ")

while(not ganhador):
  print('Jogador: ' + token[player] +'\n')

  printBoard(board)
  print("\n")

  if(player == 0):
    movimentoLinha, movimentoColuna = movimentoIA(board, player)
  else:
    if modo == '2':
      movimentoLinha, movimentoColuna = movimentoIA(board, player)
    else:
      movimentoLinha = getInputValido("Digite a linha do movimento: ")
      movimentoColuna = getInputValido("Digite a coluna do movimento: ")

  if(verificaMovimento(board, movimentoLinha, movimentoColuna)):
    fazMovimento(board, movimentoLinha, movimentoColuna, player)
    player = (player + 1) % 2
  else:
    print("A posição já está ocupada")

  ganhador = verificaGanhador(board)

print('\n______________Situação final_______________\n')
printBoard(board)

if ganhador == 'Empate':
  print('\nDeu Velhaa!')
else:
  print("\nO ganhador é o jogador", ganhador)