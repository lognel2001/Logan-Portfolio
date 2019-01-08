#Logan Nelson
#12/18
#Tic_Tac_Toe against computer

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#functions
def display_instructions():
    """Display game instructions."""
    print(
        """
            Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
            This will be a showdown between your human brain and my silicon processor.

            You will make your move known by entering a number,0-8. The number
            will correspond to the board position as illustrated:

    
       0  |  1   | 2
   -------|------|-----
       3  |   4  | 5
   -------|------|-----
      6   |   7  | 8

          Prepare yourself""")

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question+" y or n").lower()
    return response
    
    answer = input()
    while answer.lower() != "y" or "n":
        if answer== "n":
            return "No"
        elif answer== "y":
            return "Yes"
        else:
            print(answer)

####display_instructions()
####x=ask_yes_no("do you wanna fight?")
####print (x)
##################################################
def ask_num(question, low, high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)
##################################################
###x=ask_num("enter a number between 1 and 10 ",1,11)
###print (x)

def go_first():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you want to go first?")
    if go_first == ("y"):
        print("\nThen you shall go first")
        human=X
        computer=O
        
    else:
        print("\nThen I shall go first")
        human=O
        computer=X
    return human, computer
       
###human, computer = go_first()
###print(human)
###print(computer)
##################################################
def new_board():
    """Create new game board."""
    board=[]
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
###board = new_board()
###print(board)
##################################################
def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
##board = [X,EMPTY,EMPTY,EMPTY,X,EMPTY,EMPTY,EMPTY,X]
##display_board(board)
##################################################
def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for i in range(len(board)):
        if board[i] == EMPTY:
            moves.append(i)
    return moves
##board = new_board()
##moves = legal_moves(board)
##print(moves)
##################################################
def winner (board):
        """Determine the game winner."""
        WAYS_TO_WIN = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 8))
        for row in WAYS_TO_WIN:
            if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                winner = board[row[0]]
                return winner

        if EMPTY not in board:
            return TIE

        return None

##board =[X,X,X,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
##win = winner(board)
##print(win)
##################################################
def human_move(board, human):
    """Get human move."""
    legal=legal_moves(board)
    move = None
    
    while move not in legal:
        move = ask_num("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already chose. Choose another.\n")
        print("Okay")
        return move

##board = new_board()
##move = human_move(board)
##################################################
def next_turn(turn):
    """Swithc turns."""
    if turn == X:
        return O
    else:
        return X
##turn = X
##turn = next_turn(turn)
##print(turn)
##################################################
def congrat_winner(the_winner,computer , human):
    """Congratulate the winner."""
    if the_winner !=TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")
        
    if the_winner == TIE:
        print("Oh wow, it's a tie, how dissapointing. \n")
    elif the_winner == human:
        print("You got lucky this time peasant")
    elif the_winner == computer:
        print("Hahahahahahahaha")

##w=X
##c=O
##h=X
##congrat_winner(w,c,h)
##################################################
def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    #the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end= " ")

    #if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
##board = new_board()
##board[4] = X
##board[0] = X
##h=X
##c=O
##move = computer_move(board, c,h)
##print(move)
##################################################
def main():
    display_instructions()
    human, computer = go_first()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

##start the program
main()
input("\n\nPress the enter key to quit.")
