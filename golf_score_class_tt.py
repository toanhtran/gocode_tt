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

class CourseLayout:
    def __init__(self,course_layoutfilename_string):
     	self.course_layoutfilename = course_layoutfilename
        with open(self.course_layoutfilename_string, "r") as gt:
        	print gt.readlines()
    def read(self):
    	with open(self.filename) as gt:
    		print gt.readlines()

class Player:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    # def __str__(self):
    # 	return '{0} has been added with a score of {1} making {2} their total score.'.format(self.name,self.score,self.total_score)

   

    def total_score(self):
    	# all_score = sum(self.score)
    	# return all_score
    	
    	par = 72
    	all_score = sum(self.score)
    	above_par = all_score - par
    	below_par = par - all_score
    	return all_score, above_par

    	# for num_player in all_score:
    	# 	if all_score > par:
    	# 		above_par = all_score - par
    	# 		print "Player:" num_player, "scored", sum(all_score[num_player]) "," above_par, "above par."

        
class AppInterface:
	def __init__(self):
		pass
	
	leaderboard = []	

	while True:
		
		ui_input = raw_input("**********        Welcome to the Golf Tournment Tracker!      **********\nEnter:\n't' track number of players \n'n' number of holes play\n'a' add player names and scores\n'l' view leaderboard:\n")
		if ui_input == 'n':
			holes = raw_input("How many hole are you playing today? ")
			print "You are playing %s holes." %holes

		elif ui_input =='t':
			t = raw_input("How many players are playing today? ")
			print "You have %s players in your game." %t

		elif ui_input =='a':
			player_name = raw_input("What is your name? ")
			add_score = raw_input("What is your score? ")

	 		array = add_score.split(',')#arrary of score is a string
	 		for idx, num in enumerate(array):#loop thru  array and get element and change str to int
	 			array[idx] = int(num)

			p1 = Player(player_name,array)#create an instance(copy) of Player stored in p1 instance
			print p1.score, p1.name#call score method for p1 instance and name method on p1
			leaderboard.append(p1)# append object to leaderboard 
			
		elif ui_input == 'l':
			par = 72
			for player in leaderboard:
				
		else:
			if ui_input == 'q':
				break

hello = AppInterface()
#gt = CourseLayout(raw_input("Which .txt file do you want to read? "))
#course = CourseLayout(filename)

#AppInterface
#gt = AppInterface("course_layout.txt")
