import math
def find_percent_composition (listofelements, molarmasses):
    listtoreturn = []
    totalmolarmass = 1
    for index in range(len(molarmasses)):
        totalmolarmass += molarmasses[index]
    for index in range(len(listofelements)):
        value = (molarmasses[index])/(totalmolarmass) * 100
        listtoreturn.append("%s has a percent composition of %s percent." % (str(listofelements[index]), str(value)))
    for index in range(len(listtoreturn)):
        print (listtoreturn[index])


listofelements = []
while True:
    value = input("What is the element name? ")
    if value == "exit":
        break
    listofelements.append(value)
    print ('''Got it, type "exit" to exit.''')


scaledmolarmasses = []
while True:
    value = input("What is the molar mass of the element? ")
    if value == "exit":
        break
    YorN = input("Are there multiple of this element present? (Y/N) ")
    if YorN.lower() == "y":
        multiplier = input("How many atoms of this element are present? ")
        value = (float(value) * int(multiplier))
    scaledmolarmasses.append(float(value))
    print ('''Got it, type "exit" to exit.''')

find_percent_composition(listofelements, scaledmolarmasses)
