import math
import time

def nCr(n, r):
	n = float(n)
	r = float(r)
	function_output_var = (math.factorial(n))/(math.factorial(n-r) * math.factorial(r))
	return function_output_var

while True:
	choice_alpha = input("\nAction? 1 for doing the nCr thing, anything else for exiting. ")
	if choice_alpha == "1":
		function_input_var_n = input("Please input n, or the total number of things. ")
		function_input_var_r = input("Please input r, or the number of things you deal with at a time. ")
		print ("Your answer is %s.\n" % nCr(function_input_var_n, function_input_var_r))
	else: 
		print ("Thanks for using the service!")
		time.sleep ("500")
		break