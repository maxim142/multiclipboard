import shelve, pyperclip
x=1
names = []

mcbShelf = shelve.open("mcb")

def NotExistingName(a, b):
	if a not in b:
		b.append(a)
		return True

def existingName(a, b):
	if a in b:
		return True


def copToBoard(a):
	text = mcbShelf[a]
	pyperclip.copy(text)
	print (title + " copied to clipboard")

def saveToFile(a):
	text = str(pyperclip.paste())
	mcbShelf[a] = text
	print ("saved")



print ("""Welcome. This is the multiclipboard app.\n
	Just enter a name, hit enter and this will copy your clipboard.\n 
	Need the text back? type the name again and you can paste it.\n
	Type "copies" to view your copies.\n
	Type "OW" (OverWrite) to overwrite one of your copies.\n
	Type "exit" to exit the app.
	""")

while x == 1:
	title = input("Enter name here: ")

	if title == "exit":
		x=0

	elif title == "copies":
		print (names)
	elif title == "OW":
		overWrite = input("what do you want to overwrite: ")
		if existingName(overWrite, names):
			saveToFile(overWrite)

	elif NotExistingName(title, names):
		saveToFile(title)
	elif existingName(title, names):
		copToBoard(title)




mcbShelf.close()