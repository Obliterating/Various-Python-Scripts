def MolecularGeometry(EG, LP):
    EG = int(EG)
    LP = int(LP)
    if EG == 4:
        if LP == 1:
            print ("Trigonal Pyramidal")
        elif LP ==2:
            print ("Bent")
        else:
            print ("Tetrahedral")
    elif EG == 2:
        print ("Linear")
    elif EG == 3:
        print ("Trigonal Planar")

while True:
    x = input("How many Electron Groups/Electron Domains? ")
    if x == "stop":
        break
    y = input("How many Lone Pairs? ")
    MolecularGeometry(x, y)
    
