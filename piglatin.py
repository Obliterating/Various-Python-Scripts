var1 = 0
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number_list_1 = ["0", "1", "2"]
a = 0
inputted_string_4 = "!"
continue_variable = "!"
inputted_string_3 = "!"
the_action = 4


def scam_check_alpha (scam_check_string):
	alphanumeric = True
	scam_check_string = str(scam_check_string)
	for i in range(0, len(scam_check_string)):
					if scam_check_string[(i - 1)] not in alphabet_list:
						alphanumeric = False
	return alphanumeric
def scam_check_beta (scam_check_string):
	alphanumeric = True
	scam_check_string = str(scam_check_string)
	for i in range(0, len(scam_check_string)):
					if scam_check_string[(i - 1)] not in number_list_1:
						alphanumeric = False
	return alphanumeric	
def PigLatin(inputted_string):
	length_of_string = len(inputted_string)
	length_minus_one = length_of_string - 1
	length_minus_two = length_of_string - 2
	new_string = inputted_string[length_minus_one] + inputted_string[0:(length_minus_one)] + "ay"
	return new_string
def translate_to_pig_Latin(inputted_string_2):
	length_of_string_2_2 = int(len(inputted_string_2) - 2)
	new_string = inputted_string_2[1: length_of_string_2_2] + inputted_string_2[0]
	return new_string
while True:
	var2 = 0
	the_action = 4
	while not scam_check_beta(the_action):
		the_action = input('''Enter "0" for translating a word from English to PigLatin, "1" for translating a word from PigLatin to English, and "2" to quit the program. ''')
		if not scam_check_beta(the_action):
			print ("Sorry, only enter valid numbers. ")
	the_action = int(the_action)
	if the_action == 0:
		continue_variable = 0
		i = 0
		while continue_variable == 0:
			inputted_string_4 = "!"
			while not scam_check_alpha(inputted_string_4):
				inputted_string_4 = input("Please carefully write the word (no spaces) that you want to translate to PigLatin. ")
				if not scam_check_alpha(inputted_string_4):
					print("Sorry, only enter characters in the English Alphabet. ")
			print ("Your translated word is: " + PigLatin(inputted_string_4))
			while not scam_check_alpha(continue_variable):
					continue_variable = input("Do you want to continue? Enter Yes if you want to continue. ")
					if not scam_check_alpha(continue_variable):
						print("Sorry, only enter characters in the English Alphabet. ")
			if continue_variable.lower() == "yes":
				continue_variable = 0
			else:
				continue_variable = 1
		continue_variable = 0
		print ("Exiting back to the main menu")
		print ("")
	elif the_action == 1:
		continue_variable_2 = 0
		while continue_variable_2 == 0:
			inputted_string_3 = "!"
			while not scam_check_alpha(inputted_string_3):
				inputted_string_3 = input("What string would you like to translate from PigLatin to English? ")
				if not scam_check_alpha(inputted_string_3):
					print("Sorry, only enter characters in the English Alphabet. ")
			print ("Your translated word is: " + translate_to_pig_Latin(inputted_string_3))
			while not scam_check_alpha(continue_variable_2):
					continue_variable_2 = input("Do you want to continue? Enter Yes if you want to continue. ")
					if not scam_check_alpha(continue_variable_2):
						print("Sorry, only enter characters in the English Alphabet. ")
			if continue_variable_2.lower() == "yes":
				continue_variable_2 = 0
			else:
				continue_variable_2 = 1
		continue_variable_2 = 0
		print ("Exiting back to the main menu")
		print ("")
	elif the_action	== 2:
		print ("Come again soon!")
		break
	else:
		pass

