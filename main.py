list46 = []
checked46 = []

def getuseritems():
    print("Please enter the numbers you want to check if 4 AND 6 are factors. Type 'done' to run the program with the numbers you have given")
    exit = False
    while exit == False:
        tmpvar1 = input("Please enter number: ")
        if tmpvar1 == "done".lower():
            exit = True
            print("Checking")
        elif tmpvar1.isdigit():
            list46.append(tmpvar1)
        else:
            print("Please enter a vaild number!")
    
def checkitems(inputlist, outputlist):
    for item in inputlist:
        is4 = False
        is6 = False
        if (float(item[-1]) / 2).is_integer():
            #print(2)
            if (float(item[-1]) / 4).is_integer():
                #print(4)
                is4 = True
            if (float(item) / 3).is_integer():
                #print(6)
                is6 = True
            if is4 == True and is6 == True:
                outputlist.append(True)
            else:
                outputlist.append(False)
        else:
            outputlist.append(False)
    return(outputlist)

def outputfunction(inputlist, outputlist):
    i = 0
    while i != len(inputlist):
        if outputlist[i] == True:
            print("{} is divisible by 4 and 6!".format(inputlist[i]))
        else:
            print("{} is not divisible by 4 and 6!".format(inputlist[i]))
        i += 1


getuseritems()
checked46 = checkitems(list46, checked46)
#print(checked46)
outputfunction(list46, checked46)
