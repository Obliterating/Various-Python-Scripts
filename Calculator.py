def zeCalculater(x):
	x = int(x)
	if x >= 0:
		z = 1
		total_pegs = 16
		while (x+1) != z:
			#print (z)
			#print (x)
			#print (str((4+(z*2))*(4+(z*2))))
			total_pegs += ((4+z)*(4+z))
			#print (total_pegs)
			z += 1
		return ("This is the total amount of pegs: " + str(total_pegs))


	else:
		return ("Please enter a whole number, which is a positive number that is not a decimal, but could be zero.")


y = int(input("How many more square brick layers are behind the first 4x4 layer? "))
print (zeCalculater(y))
