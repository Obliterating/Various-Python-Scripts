mole_num = 6.02214076 * 10 ** 23
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
special_list = ["A", "B", "C"]

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
					if scam_check_string[(i - 1)] not in special_list:
						alphanumeric = False
	return alphanumeric

def grams_to_moles (grams, molar_mass):
	grams = float(grams)
	molar_mass = float(molar_mass)
	function_output = grams/molar_mass
	return function_output

def moles_to_grams (moles, molar_mass):
	moles = float(moles)
	molar_mass = float(molar_mass)
	function_output = moles * molar_mass
	return function_output

def particles_to_moles (particles):
	particles = float(particles)
	function_output = particles/mole_num
	return function_output

def moles_to_particles (moles):
	moles = float(moles)
	function_output = moles * mole_num
	return function_output

while True:
	#check if it's bad
	while True:
		what_we_do = input('''Enter "A" for "grams to molecules", "B" for "molecules to grams", "C" to quit. ''')
		if scam_check_beta(what_we_do):
			break
		else:
			print ("Please try again.")
	if (what_we_do == "A"):
		#check if it's bad
		while True:
			user_input1 = input("Please enter the number of grams. ")
			user_input2 = input("Please enter the molar mass. ")
			try:
				user_input1 = float(user_input1)
				user_input2 = float (user_input2)
				break
			except ValueError:
				print ("Please try again! (Numbers and decimals only)")
		print ("%s particles."% moles_to_particles(grams_to_moles(user_input1, user_input2)))
	elif (what_we_do == "B"):
		#check if it's bad
		while True:
			user_input1 = input("Please enter the number of molecules. (Decimal part, scientific notation later) ")
			user_input2 = input ("What power of ten is that multipled by? ")
			user_input3 = input("Please enter the molar mass. ")
			try:
				user_input1 = float (user_input1)
				user_input2 = float (user_input2)
				user_input3 = float (user_input3)
				num_molecules = user_input1 * 10 ** user_input2
				break
			except ValueError:
				print ("Please try again! (Numbers and decimals only)")
		print ("%s grams." % moles_to_grams(particles_to_moles(num_molecules), user_input3))
	else:
		break
