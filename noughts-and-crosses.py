

import collections

def clearBoard():

	coordinates = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

	board = collections.OrderedDict()
	for p in coordinates:
		board[p] = " "
	return board

def display(board):

	print (
		"    A   B   C \n" 
		"1 | %s | %s | %s | \n"
		"2 | %s | %s | %s | \n"
		"3 | %s | %s | %s |" % tuple(board.values())
			)

def possibleMoves(board):

	remaining = []
	for space in board:
		if board[space] == " ":
			remaining.append(space)
	return remaining

def validMove(board, move):

	if move not in possibleMoves(board): 
		print("You must select an open space. Please try again.")
		return False
	return True


def updateBoard(board, move, turn):

	boardUpdated = board
	boardUpdated[move] = "X" if turn%2==0 else "O"
	return boardUpdated

def checkBoard(board):

	winner = None

	winLines = [
	(board["A1"]+board["A2"]+board["A3"]),
	(board["B1"]+board["B2"]+board["B3"]),
	(board["C1"]+board["C2"]+board["C3"]),
	(board["A1"]+board["B1"]+board["C1"]),
	(board["A2"]+board["B2"]+board["C2"]),
	(board["A3"]+board["B3"]+board["C3"]),
	(board["A1"]+board["B2"]+board["C3"]),
	(board["A3"]+board["B2"]+board["C1"])
	]

	if 'XXX' in winLines:
		print ("Woohooooo!! Player 1 wins! \n")
		winner = 1
	elif 'OOO' in winLines:
		print ("Yahoooooo!! Player 2 wins! \n")
		winner = 2
	elif " " not in board.values():
		print ("Ohhoo!! This is a draw! \n")
		winner = 0
	else:
		print ("Seems there is still no champion. \n")
	return winner

def playTheGame():

	print ("\n Welcome to Noughts & Crosses! \n Player 1, you'll be X. \n Player 2, you'll be O. \n")

	board = clearBoard()
	turn = 0

	while True:
		# show the board
		display(board)

		if checkBoard(board) != None:
			break

		print ("Lets start a game. Player %s, it's your turn!" % (turn%2 + 1))
		while True:
			move = input("Please select a space.(for example A1 or just any of your favourite or lucky spots)").upper()
			if validMove(board, move):
				board = updateBoard(board, move, turn)
				turn += 1
				break

playTheGame()
