'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

#Problem 1A
def give_coord(square_num):
    coord = [((square_num - 1) // 3), ((square_num-1) % 3)]
    return coord

#Problem 1B
def put_in_board(board, mark, square_num):
    coord1 = give_coord(square_num)
    board[coord1[0]][coord1[1]] = mark

#Problem 2A
def get_free_squares(board):
    free_squares = []
    for i in range (3):
        for j in range(3):
            if board[i][j]==" ":
                free_squares.append([i,j])
    return free_squares

#Problem 2B
def make_random_move(board, mark):
    free_squares = get_free_squares(board)
    move = free_squares[len(free_squares) * int(random.random())]
    board[move[0]][move[1]] = mark

#Problem 3A
def is_row_all_marks(board, row_i, mark):
  for i in range (0, 3):
    if board[row_i][i] != mark:
      return False
  return True

#Problem 3B
def is_col_all_marks(board, col_i, mark):
  for i in range (len(board)):
    if board[i][col_i] != mark:
      return False
  return True

#Problem 3C
def is_diag1_all_marks(board, mark):
  for i in range (0,3):
    if board[i][i] != mark:
      return False
  return True

def is_diag2_all_marks(board, mark):
  for i in range (0,3):
    if board[i][2-i] != mark:
      return False
  return True

#Problem 3D
def is_win(board, mark):
  win = False
  for i in range (0,3):
    if (is_row_all_marks(board, i, mark)==True or is_col_all_marks(board, i, mark)==True or is_diag1_all_marks(board, mark)==True or is_diag2_all_marks(board, mark)==True):
      win = True
      break
  return win

'''
#Problem 4B
def block (board):
  count_freesq = 0
  freesq = [0,0]
  count_player_mark = 0
  for i in range (0, 3):
    for k in range (0,3):
      if board[i][k] == " ":
        count_freesq+=1
        freesq = [i,k]
      elif board[i][k] == "X":
        count_player_mark +=1

    if count_freesq == 1 and count_player_mark ==2:
      board[freesq[0]][freesq[1]] == "O"'''

#Problem 4A
def comp_alg (board):
  free_squares = get_free_squares(board)

  for i in range (len(free_squares)):
    board[free_squares[i][0]][free_squares[i][1]] = "O"

    if (is_win(board, "O")):
      return True
    else:
      board[free_squares[i][0]][free_squares[i][1]] = " "

 #if (block(board)):
    #block(board)
 # else:

  make_random_move(board, "O")

if __name__ == '__main__':
    board = make_empty_board()

    print_board_and_legend(board)

    print (get_free_squares(board))

    #Problem 1C
    count = 0
    square_num = 0
    while count < 9:
        mark = ""
        if count%2 == 0:
            square_num = int(input("Please input coordinate for X: "))
            put_in_board(board,"X", square_num)
        else:
            comp_alg(board)

        print_board_and_legend(board)
        count += 1

        if is_win(board, "X") == True:
          print ("Player won :)")
          break
        elif is_win(board, "O") == True:
          print ("Computer won :)")
          break



