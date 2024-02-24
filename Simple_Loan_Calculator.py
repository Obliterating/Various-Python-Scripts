import math

purchase_price = float(input("What's the purchase price? "))
down_payment = float(input("What's the down payment? "))
months = float(input("How many months? "))
APR = float(input("What's the APR? "))
principal_loan = purchase_price - down_payment
interest = principal_loan * APR * (months/12)
monthly_amount = (interest + principal_loan)/months
print ("Your interest paid is %s" % str(interest))
print ("Your monthly amount is %s for %s months." % (str(monthly_amount), str(months)))
print ("It will cost you a total of $%s." % str((principal_loan + down_payment + interest)))
    
