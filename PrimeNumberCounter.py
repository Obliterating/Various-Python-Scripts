print ('''Welcome to the Prime Number finder! Give us a range of integers and we'll find all the prime numbers in it!''')
minimum = int(input("Gives us the minimum of your range! "))
maximum = int(input("Gives us the maximum of your range! "))
while minimum == 0 or maximum == 0:
	print ("Sorry, please do not enter 0!")
	minimum = int(input("Gives us the minimum of your range! "))
	maximum = int(input("Gives us the maximum of your range! "))
maximum = abs(maximum)
minimum = abs(minimum)
print ("")
print("Would you like to be notified whenever a number is found to not be prime? Please type Y or N")
message_me = input("Y or N : ")
while (message_me != "Y") and (message_me != "N"):
        print ("Please type 'Y' or 'N' !")
        message_me = input("Type it here: ")
if message_me == "Y":
        message_me = True
else:
        message_me = False
print ("")
print ("Would you like the final string of prime numbers to be copied to the clipboard?")
copy_to_clipboard = input("Type Y or N: ")
while (copy_to_clipboard != "Y") and (copy_to_clipboard != "N"):
	copy_to_clipboard = input("Type Y or N: ")
if copy_to_clipboard == "Y":
        copy_to_clipboard = True
else:
        copy_to_clipboard = False

print (
'''
-------------------------------------------------------------------------------------------------
''')
current_number = minimum
stop = False
prime_number_list = []
#------------------------------------------------------------
'''

while stop == False:

	prime = True # Logic


	square_of_current_number = (current_number ** (0.5)) # Squaring that number
	cap =  round(square_of_current_number + 0.5) # Finding that square... rounded up
	n1 = (current_number/cap) # Using that rounded square to check for divisibility

	print ("Checking to see if %s is a prime #" % current_number)


	while cap > 2: # Repeating Logic
		if (n1 - round(n1)) == 0:
			prime = False
		cap = cap - 1 # Repeating Logic

	if cap < 2:
		prime = False

	if prime == True:
		prime_number_list.append(current_number)
	if current_number == 10:
		stop = True

# Iteration...
	current_number = current_number + 1

'''
#------------------------------------------------------------
while stop == False:
	prime = 1
	y = int(current_number ** 0.5) + 1
	for i in range(2, y): # Riddle: When you count from 2 to the rounded up square root of the current_number, why doesn't it work?
		if current_number % i == 0:
			prime = 0
			if message_me:
				print ("%s Prime!" % current_number)
	if current_number  % 2 ==  0 and current_number != 2:
		prime = 0
	if (prime == 1) and (current_number != 1): 
		prime_number_list.append(str(current_number))
	if round(maximum / current_number) == maximum / 2:
		print(">49% there!")
	if round(maximum / current_number) == (3 * maximum) / 4:
		print(">74% there!")
	if current_number == maximum:
		stop = True
	current_number = current_number + 1











#------------------------------------------------------------

print ("")
print ("----- These are the prime numbers!!! -----")
print ("")

MyString = ", ".join(prime_number_list) 
print (MyString)
if copy_to_clipboard:
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(MyString)
	r.update() 
	r.destroy()

print ("")
print (
'''
Thank you for using this system! 
Please go back to the file and press RUN (located on the top bar) to use this program again!''')
		

# Credit to Programiz, Stackoverflow accounts Mark Beik, David Anderton, Robert, Hannes Karppila, atomizer, and vauhochzett for helping me with some syntax
