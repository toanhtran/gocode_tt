'''
Golf Score Calculator App

The goal of this app is for you to be able to enter scores for different players and print a leaderboard.  You are given a file with the base scores for a default course that you will need to read in (ask an instructor if you don't understand golf!).

# Example UI in the Terminal:
# How many players are in the golf tournament? 2
# How many holes are in the golf course? 18
# What is the name for player 1? Jonathan Lau
# What is the name for player 2? Jeremy Schwartz
# What are the scores for player 1? [3,3,3,3,3...]
# What are the scores for player 2? [3,3,3,3,3]
# Type p to print the leaderboard: p
# LeaderBoard
# 1 - Jonathan Lau, Overall Score: 73, +1
# 2 - Jeremy Schwartz, Overall Score: 76, +5

You will implement this idea and create a golf score calculator using classes.  

You are free to adjust the gameplaym, how the app works, and to extend it as you wish.

Here are some basic recommendations for how to design your classes:

1) A CourseLayout class:

In charge of reading in the file with the base scores for the golf course.

You will use the file given to you as the default.  

Optionally, you can allow the user to enter a filename for a different golf course.

2) A PlayerScore class:

In charge of handling player information and scores

3) A AppInterface Class:

This has a simple method that runs the game and talks to the terminal I/O.

It also has a method that uses information from the CourseLayout and PlayerScore and prints a leaderboard.

Ex:

LeaderBoard
1 - Jonathan Lau, Overall Score: 73, +1
2 - Jeremy Schwartz, Overall Score: 76, +4

Note: The last number is simply the overall score minus 72 (it's how golf works...)

'''

# class CourseLayout:
#     def __init__(self):
#         pass

# class Player:
#     def __init__(self):
#         pass

# class AppInterface:
#     def __init__(self):
#         pass

def add_score(array_item):
	new_score = raw_input("Enter score: ")
	array_item.append(new_score)
	return array_item


def num_of_players():
	num_of_players = raw_input("How many players today? ")
	return "You have " + num_of_players + " players golfing today."

# def holes():
# 	print "You are playing 18 holes today"
# 	with open ('CourseLayout.txt') as f:
# 		f.readlines()
	
def create_player(new_dict_pair):
	player = raw_input("Please enter player name: ")
	array_item = []
	new_dict_pair[player] = array_item
	return new_dict_pair
	



def ai_loop():
	all_scores = {}
	while True:
		ui_input = raw_input("**********        Welcome to the golf tournment tracker!      **********\nEnter:\n't' track number of players \n'n' number of holes play\n'a' add player names\n's' see player score\n'l' view leaderboard:\n")
		if ui_input == 't':
			print "You have players, player!"
			print num_of_players()
		elif ui_input == 'n':
			holes = raw_input("How many holes do you want to play today? ")
			# print holes()
		elif ui_input == 'a':
			all_scores = create_player(all_scores)
			print all_scores
		elif ui_input =='s':
			# player_search = raw_input("What player do you want to add a score? ")
			# # if all_scores.has_key(all_scores['player_search']):
			# 	all_scores[player_search] = add_score(all_scores[player_search])
		else:
			ui_input == 'q'
			break





ai_loop()



