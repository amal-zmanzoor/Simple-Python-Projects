#GLOBAL VARIABLES
#------------------------------------------------------------
#game board
board = ["-","-","-",
		 "-","-","-",
		 "-","-","-"]

#if game is still going
game_still_going = True

#won?lost?tie?
winner = None

#who's turn is it?
current_player = "X"

#-----------------------------------------------------------

def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

	#display the intial board
	display_board()

	while game_still_going:
		handle_turn(current_player)
		check_if_game_over()
		#other player's turn now
		flip_player()

	#game ends
	if winner == "X" or winner == "O":
		print(winner + " won!")
	elif winner == None:
		print("It's a tie...")


def check_if_game_over():
	check_for_winner()
	check_if_tie()


def check_for_winner():

	global winner 
	#check rows
	row_winner = check_rows()
	#check columns
	column_winner = check_columns()
	#check diagonals
	diagonal_winner = check_diagonals()
	#deiding winner
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None
	return


def check_rows():

	global game_still_going

	#check if any of the rows consist of all 'X's or all 'O's
	#these 3 varaiables will be used as booleans
	row1 = board[0] == board[1] == board[2] != "-"
	row2 = board[3] == board[4] == board[5] != "-"
	row3 = board[6] == board[7] == board[8] != "-"

	#to return winner as X or O
	if row1 or row2 or row3:
		game_still_going = False
	if row1:
		return board[2]
	elif row2:
		return board[5]
	elif row3:
		return board[8]
	return


def check_columns():

	global game_still_going

	#check if any of the columns consist of all 'X's or all 'O's
	#these 3 varaiables will be used as booleans
	column1 = board[0] == board[3] == board[6] != "-"
	column2 = board[1] == board[4] == board[7] != "-"
	column3 = board[2] == board[5] == board[8] != "-"

	#to return winner as X or O
	if column1 or column2 or column3:
		game_still_going = False
	if column1:
		return board[0]
	elif column2:
		return board[1]
	elif column3:
		return board[2]
	return


def check_diagonals():

	global game_still_going

	#check if any of the diagonals consist of all 'X's or all 'O's
	#these 2 varaiables will be used as booleans
	diagonal1 = board[0] == board[4] == board[8] != "-"
	diagonal2 = board[2] == board[4] == board[6] != "-"

	#to return winner as X or O
	if diagonal1 or diagonal2:
		game_still_going = False
	if diagonal1:
		return board[0]
	elif diagonal2:
		return board[2]
	return


def check_if_tie():

	global game_still_going

	if "-" not in board:
		game_still_going = False
	return

#change current player
def flip_player():

	global current_player

	#checking if current player is X. 
	#If yes, ASSIGN current player to be O
	if current_player == "X":
		current_player = "O"
	elif current_player == "O":
		current_player = "X"
	return

#handles the turn of the player who's turn it is
def handle_turn(player):

	print(player + "'s turn.")
	#asking user to decide where thet want to place their X or O
	position = input("Choose a position from 1-9 to choose your position: ")
	#can use integer value as index for board list

	#input validation

	valid = False 

	while not valid:
		while position not in ["1","2","3","4","5","6","7","8","9"]:
			position = input("Invalid input. Choose a position from 1-9.")

		position = int(position)-1

		if board[position] == "-":
			valid = True
		else:
			print("This position is already taken. Please choose another one.")
	board[position] = player
	display_board()


play_game()


