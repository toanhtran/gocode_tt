'''

Part 1: Make a program that keeps track of your budget.  The user can type in commands via the terminal to make changes/add/show the budget.

- Create a program with a simple ui loop (a function that has a while loop which keeps the program running).  THe loop will repeatedly display a list of commands and ask the user for input. (Commands are listed below)
- Once the input action is complete, display the list of command options again until the user quits (enters "q").
- Each command has an associated function that gets called when the user enters the right letter.  You will write these functions.


Commands:

"a" Add an item to the budget - should ask the user for each field name, amount, monthly
"s" Show items in the budget - calculates the total amount of expenses
"r" Remove an item from the budget
"q" Quit Program


'''



'''
**** Finish part one before moving on to Part 2 ****


A csv file is a very simple file that is used quite often. Usually a csv file will look something like this:

(a simple expenses csv file)

---
name,amount,monthly
food,1000.00,y
rent,2000.00,y
braces,2000.00,n
---


A csv usually starts with a header line that lists the names of the fields so someone reading or importing it into a spreadsheet app knows what each column is for.

Your goal is to write a simple budget app. This application will have a simple interface that shows the list of commands to the user, and allows the user to enter a command and keep doing various commands until they say
quit. 

It will store the data it gets from the user in a csv file. 

Add the following commands

1. "s" - Save file -> this converts your internal data structure to a csv and rights it out
2. "r" - Read File -> reads from a csv and converts the data into your internal data structure.

To test your output, you should be able to open the file in a spreadsheet application (e.g. Excel) after closing.

'''
def add_items():#creates function to store items in 
	my_budget = {}#stores user input in an empty hash
	name = raw_input("Enter the name of your item: ")
	amount = raw_input("Enter amount:$ ")
	monthly = raw_input("Enter 'Y' for reoccuring or 'N' : ").upper()
	return {"name": name, "amount": amount, "monthly": monthly}

def show_items(all_budget_items):
	# print all_budget_items
	total = 0# start counter at 0

	for item in all_budget_items:#loop thru hash
		print "Item: ", item['name'] 
		print "Amount: ",item['amount']
		print "Monthly: ",item['monthly']	
		total += float(item['amount'])
		print total

def remove_items(all_budget_items):
	for item in all_budget_items:
		print item['name']
	remove_input = raw_input("Enter item name to remove.: ")
	for key, item in enumerate(all_budget_items):
		for name in item:
			if item[name] == remove_input: 
				all_budget_items.pop(key)


def save_file(all_data):#passing all_data pass it in save_file to loop thru array
	filename = raw_input("Enter filename with csv. ext.: ")
	with open (filename, "w") as f:
		f.write("Name,Amount,Monthly\n")#created header with name, amount, monthly
		for i in all_data:# loops through all_data 
			f.write(i["name"] + "," + i["amount"] + "," + i["monthly"] + "\n")#prints dict = i + ,(comma) to separate each item

	print filename

def read_file():
	file_a = raw_input("Enter filename.csv to read: ")#prompt user to enter file name to view
	final_budget = []#creates an empty array to store new_budget dict array
	with open(file_a,"r") as f:
		lines = f.readlines()#stores readlines output into lines variable
		for line in lines[1:]:# use slice to skip first line, which is the header and start reading data below
			print line
			fields = line.strip('\n').split(",")# takes out the \n and separates items with a comma
			name = fields[0] 
			amount = fields[1]
			monthly = fields[2]
			new_budget_item = {"name": name, "amount": amount, "monthly": monthly}#new_budget_item takes the dict to store data
			final_budget.append(new_budget_item)#appends new dict to final_budget
		return final_budget

	


def ui_loop():#creates loop function
	all_data  = []#creates empty array to store items
	while True:
		name = raw_input("Enter 'a' to add ,'s' to show, 'r' to remove\n'w' to write to file, 'l' load file to read, 'q' to quit:  ")#prompts user to 'a' = add_item(), 's' = show_item , 'q'
		if name == 'a':
			all_data.append(add_items())#add new add_time to all_data hash
		elif name == 's':
			show_items(all_data)
			print "Your items have been saved. "
		elif name == 'w':
			print save_file(all_data)
		elif name =='l':
			all_data = read_file()# swapping out empty array for data that is called and built from read_file
		elif name == 'r':
			print remove_items(all_budget_items)
		else:
			name == 'q'
			break
	return all_data
ui_loop()



