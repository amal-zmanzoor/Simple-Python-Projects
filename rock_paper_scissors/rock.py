# Simple Rock, Paper, Scissors Game

import random

def play():
	user = input("What's your choice? 'r' for rock, 'p' for scissors, 's' for scissors\n")
	computer = random.choice(['r','p','s'])

	if user == computer:
		print("It\'s a tie.") 
	elif is_win(user, computer):
		print("You won!")
	else:
		print("You lost :/ ")

def is_win(player, opponent):
	if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') \
		or (player == 'p' and opponent == 'r'):
		return True
play()