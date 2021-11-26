def is_empty(board):
    #checks every square on the board and returns true if it's blank
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    #find the x and y positions of the two ends of the sequence
    x_first = x_end - (length)*d_x
    y_first = y_end - (length)*d_y
    x_last = x_end + d_x
    y_last = y_end + d_y

    if y_first in [-1, len(board)] or x_first in [-1, len(board[0])]:
        first = "NOT EMPTY"
    else:
        first = board[y_first][x_first]

    if y_last in [-1, len(board)] or x_last in [-1, len(board[0])] :
        last = "NOT EMPTY"
    else:
        last = board[y_last][x_last]

    if last == " " and first == " ":
        return "OPEN"
    elif last == " " or first == " ":
        return "SEMIOPEN"
    else:
        return "CLOSED"


def isbounded(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count, semi_open_seq_count = 0, 0
    i = -1

    while True:
      seq_exists = True
      i += 1
      starting_x = x_start + d_x*i
      end_x = starting_x + d_x*(length - 1)
      starting_y = y_start + d_y*i
      end_y = starting_y + d_y*(length - 1)
      if isbounded(starting_x, end_x) and isbounded(starting_y, end_y): #checks if a seq of that length from starting pos is in the bounds of the board

        # find existing seq
        for j in range (length):
          if board [starting_y+d_y*j][starting_x+d_x*j] != col: #if seq exists within that length
            seq_exists = False
            break

        #check if the seq is bounded by any of its own colour-------
        if (isbounded(starting_x - d_x, starting_y - d_y) and board [starting_y - d_y][starting_x - d_x] == col) or (isbounded(end_x + d_x, end_y + d_y) and board [end_y + d_y][end_x + d_x] == col):
          seq_exists = False

        #-----------------------------

        if seq_exists == False: #skips over this value of i if the seq is not valid
            continue

        #-----------------------------

        #this is all checked if seq is valid
        res = is_bounded(board, end_y, end_x, length, d_y, d_x)
        if res == "OPEN":
          open_seq_count += 1
        elif res == "SEMIOPEN":
          semi_open_seq_count += 1

      else:
        break #if not in bounds, then row is finished

    return open_seq_count, semi_open_seq_count


#CLOSED ROW HELPER FUNCTIONS-----------------------------------------------------------------
def detect_closed_row(board, col, y_start, x_start, length, d_y, d_x):
    closed_seq_count = 0
    i = -1

    while True:
      seq_exists = True
      i += 1
      starting_x = x_start + d_x*i
      end_x = starting_x + d_x*(length - 1)
      starting_y = y_start + d_y*i
      end_y = starting_y + d_y*(length - 1)
      if isbounded(starting_x, end_x) and isbounded(starting_y, end_y): #checks if a seq of that length from starting pos is in the bounds of the board

        # find existing seq
        for j in range (length):
          if board [starting_y+d_y*j][starting_x+d_x*j] != col: #if seq exists within that length
            seq_exists = False
            break

        #check if the seq is bounded by any of its own colour-------
        if (isbounded(starting_x - d_x, starting_y - d_y) and board [starting_y - d_y][starting_x - d_x] == col) or (isbounded(end_x + d_x, end_y + d_y) and board [end_y + d_y][end_x + d_x] == col):
          seq_exists = False

        #-----------------------------

        if seq_exists == False: #skips over this value of i if the seq is not valid
            continue

        #-----------------------------

        #this is all checked if seq is valid
        res = is_bounded(board, end_y, end_x, length, d_y, d_x)
        if res == "CLOSED":
          closed_seq_count += 1

      else:
        break #if not in bounds, then row is finished

    return closed_seq_count

def detect_closed_rows(board, col, length):
    closed_seq_count = 0

    for i in range (8):
        #seq counting for all horizontal rows
        closed_seq_count += detect_closed_row(board, col, i, 0, length, 0, 1)

        #seq counting for all vertical rows
        closed_seq_count += detect_closed_row(board, col, 0, i, length, 1, 0)

        #seq counting for all diagonal rows-----------------

        #top left to bottom right:
        closed_seq_count += detect_closed_row(board, col, i, 0, length, 1, 1)

        if i != 0:
            closed_seq_count += detect_closed_row(board, col, 0, i, length, 1, 1)

        #top right to bottom left:
        closed_seq_count += detect_closed_row(board, col, 0, i, length, 1, -1)

        if i != 7:
            closed_seq_count += detect_closed_row(board, col, i, 7, length, 1, -1)

    return closed_seq_count

#-----------------------------------------------------------------------------------------------

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    for i in range (8):
        #seq counting for all horizontal rows
        open_seq_count += detect_row(board, col, i, 0, length, 0, 1) [0]
        semi_open_seq_count += detect_row(board, col, i, 0, length, 0, 1) [1]

        #seq counting for all vertical rows
        open_seq_count += detect_row(board, col, 0, i, length, 1, 0) [0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, 0) [1]

        #seq counting for all diagonal rows-----------------

        #top left to bottom right:
        open_seq_count += detect_row(board, col, i, 0, length, 1, 1) [0]
        semi_open_seq_count += detect_row(board, col, i, 0, length, 1, 1) [1]

        if i != 0:
            open_seq_count += detect_row(board, col, 0, i, length, 1, 1) [0]
            semi_open_seq_count += detect_row(board, col, 0, i, length, 1, 1) [1]

        #top right to bottom left:
        open_seq_count += detect_row(board, col, 0, i, length, 1, -1) [0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, -1) [1]

        if i != 0:
            open_seq_count += detect_row(board, col, i, 7, length, 1, -1) [0]
            semi_open_seq_count += detect_row(board, col, i, 7, length, 1, -1) [1]

    return open_seq_count, semi_open_seq_count

def search_max(board):
    move_y, move_x = 0,0
    max_score = -100000

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = "b"
                if score(board) > max_score:
                    max_score = score(board)
                    move_y = i
                    move_x = j
                board[i][j] = " "

    found = False
    if move_y == 0 and move_x == 0 and board[0][0] != " ":
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    move_y = i
                    move_x = j
                    found = True
                    break

            if found == True:
                break

    return move_y, move_x


#DONT TOUCH THIS
def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    full_board = True
    status = ["White won", "Black won", "Draw", "Continue playing"]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                full_board = False
                break

    if detect_closed_rows(board, "b", 5)!=0 or detect_rows(board, "b", 5)[0] != 0 or detect_rows(board, "b", 5)[1] != 0:
        return(status[1])
    elif detect_closed_rows(board, "w", 5)!=0 or detect_rows(board, "w", 5)[0] != 0 or detect_rows(board, "w", 5)[1] != 0:
        return(status[0])
    elif full_board == True:
        return (status[2])
    else:
        return status[3]



#DONT TOUCH ANYTHING UNDER THIS -----------------------------------------------------------------
def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    #play_gomoku(8)
    some_tests()