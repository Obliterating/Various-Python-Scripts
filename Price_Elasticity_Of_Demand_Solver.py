undefined_variable = True
while undefined_variable:
	Quantity_Demanded_1 = float(input("Old Quantity Demanded? "))
	Quantity_Demanded_2 = float(input("New Quantity Demanded? "))
	Price_1 = float(input("Old Price? "))
	Price_2 = float(input("New Price? "))
	percent_change_in_quantity_demanded = (Quantity_Demanded_2 - Quantity_Demanded_1)/(Quantity_Demanded_1)
	percent_change_in_price = (Price_2 - Price_1)/(Price_1)
	elasticity_of_demand = (percent_change_in_quantity_demanded)/(percent_change_in_price)
	if elasticity_of_demand == -1:
		is_elastic = "Unit Elastic"
	elif elasticity_of_demand < -1:
		is_elastic = "Elastic"
	else:
		is_elastic = "Inelastic"
	print ("%s is the percent change in quantity demanded,\n%s is the percent change in price,\n%s is the elasticity of demand.\nIt is %s." % (percent_change_in_quantity_demanded, percent_change_in_price, elasticity_of_demand, is_elastic))
	undefined_variable = bool(input('''Continue? Answer anything to continue, press enter to quit. '''))

