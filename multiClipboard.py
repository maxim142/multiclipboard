import shelve, pyperclip
x=1
names = []

mcbShelf = shelve.open("mcb")

def NotExistingName(a, b):
	if a not in b:
		b.append(a)
		return True



print ("""Welcome. This is the multiclipboard app.\n
	Just enter a name, hit enter and this will copy your clipboard.\n 
	Need the text back? type the name again and you can paste it.\n
	Type "help" to view your copies.\n
	Type "exit" to exit the app.
	""")

while x == 1:
	title = input("Enter name here: ")

	if title == "exit":
		x=0

	elif title == "help":
		print (names)
	else:

		if NotExistingName(title, names):
			text = str(pyperclip.paste())
			mcbShelf[title] = text
			print ("saved")

		else:

			text = mcbShelf[title]
			pyperclip.copy(text)
			print (title + " copied to clipboard")



mcbShelf.close()