'''
Create an app that acts like a phonebook:

A user can:
Add a name and phone number 
List all of the names and phone numbers in the phonebook
Look up a phone number by the person's name
Remove a person from the phonebook

tips:
Plan out how to write/structure this code in english
Think of what data structure to use for storing the name and phone number of the phonebook
use functions to break up the tasks, does the function take a parameter? Does the function return something? 
If so,What does the function return?
'''

def add_contact():
	name = raw_input("Please enter the name: ")
	phone = raw_input("Please enter the phone number: ")
	return {"name": name, "phone": phone}

# print add_contact()

def list_contacts(list_contact):
	for item in list_contact:
		print "Name:", item['name'],
		print "Phone:", item['phone']

def find_contact(list_contact):
	for item in list_contact:
		lookup_name = raw_input("Enter name to lookup: ")
		for key, item in enumerate(list_contact):
			for name in item:
				if item[name] == lookup_name: 
					print "Name:",item['name'], "Phone:",item['phone']
# print find_contact(all_contacts)

def remove_contact(list_contact):
	remove_name = raw_input("Enter name to remove: ")
	for item in list_contact:#item is the a hash in list_contacts
		if item['name'] == remove_name: 
			list_contact.remove(item)
			return list_contact		

			

def loop():
	all_contacts = []
	while True:
		name = raw_input("Enter\n 'a' to add name and number\n 'l' to list all names \n 'f' find name\n 'r' to remove name,\n 'q' to quit: ")
		if name == 'a':
			all_contacts.append(add_contact())
		elif name == 'l':
			list_contacts(all_contacts)
		elif name == 'f':
			find_contact(all_contacts)
		elif name == 'r':
			remove_contact(all_contacts)
			print all_contacts	
		else:
			name == 'q'
			break
	return all_contacts
loop()





