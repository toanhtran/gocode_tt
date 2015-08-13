'''You will create a Menu/Bill App for a waitress to keep track of her bills

- you will display a built in set menu (it does not change) 
	Appetizers:
	Mozarella Sticks: $2.50
	Garden Salad: $3.25
	French Fries: $3.75

	Main:
	Burger: $5.50
	BLT: $4.75
	Steak and Cheese: $5.25
	Chiken Parm sandwich: $6.25
	Italian Sandwich: $6.00

	Drinks:
	soda: $2.00
	juices: $2.50
	iced tea: $1.75
	water(Bottled): $1.25

- When the waitress starts a bill, she can give it a name
- The waitress will enter the item name and it will be added to a bill
- Every time the bill displays, it will show the item, cost, and total for the bill
- The waitress can remove an item from the bill

Commands:
n - creates a new bill, asks user for the name of the bill
l - lists ALL the bills
d - deletes a bill


a - User enters "Garden Salad" - this gets added to the bill:
	Two ways to do this:
		* when the total is populated, it goes back to look up all the prices and adds them together
		* when the item is stored, the price is stored as well and you keep a running total

r- removes item from bill
s- shows items in bill

tips:
- Write this down and plan it out on paper and in english
- Use functions
- Think about what data structures you want to use to store the menu and bills

	'''

def create_bill(new_dict):#creates a bill
	ask_user = raw_input("Enter new bill name: ")
	array_item = []
	new_dict[ask_user] = array_item
	return new_dict


def list_bills(listOfBill):
	for name in listOfBill:
		print name

def add_item(array_item):
	new_item = raw_input("What food item do you want to add? ")
	array_item.append(new_item)
	return array_item
	print array_item

def remove_item(array_item):
	delete_item = raw_input("What item do you want to remove? ")
	array_item.remove(delete_item)
	return array_item
	print array_item

def total_bill(array_item,menu):
	Menu = {"Mozarella sticks": 2.50, "Garden salad": 3.25, "French Fries": 3.75, "Burger": 5.50, "BLT": 4.75, "Steak&Cheese": 5.25, "ChickenParm": 6.25, "ItalianSand": 6.00, "Soda": 2.00, "Juice": 2.50, "IceTea": 1.75, "Water": 1.25}
	total = 0
	
	for item in all_bills[bill_total]:
		total +=1float(menu[add_item])
		print "Your total is " + str(total)

		print item
		



def display_menu():
	
	Menu = {"Mozarella sticks": 2.50, "Garden salad": 3.25, "French Fries": 3.75, "Burger": 5.50, "BLT": 4.75, "Steak&Cheese": 5.25, "ChickenParm": 6.25, "ItalianSand": 6.00, "Soda": 2.00, "Juice": 2.50, "IceTea": 1.75, "Water": 1.25}
	total = 0
	for i in Menu:
		print i, ":", Menu[i]
	


def ui_loop():
	all_bills = {}
	cost = []
	while True:
		name = raw_input("Enter \n'm' to see menu items\n'n' to create and name new bill \n'l' list all bills \n'd' deletes a bill \n'a' add items in bill \n'r' remove item from bill\n't' to total and finalize\n'q' to quit: ")
		if name == 'm':
			display_menu()
		elif name == 'n':
			all_bills = create_bill(all_bills)
		elif name == 'l':
			list_bills(all_bills)
			print all_bills
		elif name == 'a':
			display_menu()
			bill_search = raw_input("What bill do you want to add items? ")
			if all_bills.has_key(bill_search):
				all_bills[bill_search] = add_item(all_bills[bill_search])
				print all_bills
			else:
				print"No bill exist with that name."

		elif name == 'r':
			bill_remove = raw_input("What bill do you want to remove items? ")
			if all_bills.has_key(bill_remove):
				all_bills[bill_remove] = remove_item(all_bills[bill_remove])
				print all_bills	

		elif name == 'd':
			bill_cancel = raw_input("What bill do you want to cancel? ")
			all_bills.pop(bill_cancel)
			print all_bills
			print "You have deleted a bill."

		elif name == 't':
			bill_total = raw_input("What bill do you want to total and finalize? ")
			total_bill(all_bills,menu)

		else:
			name == 'q'# user will quit program
			break

#print list_bills(all_bills)
ui_loop()
