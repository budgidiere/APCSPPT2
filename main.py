list46 = []
checked46 = []

def getuseritems():
    print("Please enter the numbers you want to check if 4 AND 6 are factors. Type 'done' to run the program with the numbers you have given")
    exit = False
    while exit == False:
        tmpvar1 = input("Please enter number: ")
        if tmpvar1 == "done".lower():
            exit = False
            print("Checking")
        elif tmpvar1.isdigit():
            list46.append(tmpvar1)
        else:
            print("Please enter a vaild number!")
    
def checkitems(inputlist, outputlist):
    for item in inputlist:
        is4 = False
        is6 = False
        if item[-1] == "0" or item[-1] == "2" or item[-1] == "4" or item[-1] == "6" or item[-1] == "8"
         last2 = (item[-1] + item[-2]
