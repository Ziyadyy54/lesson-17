inputfromuser=int(input("enter a number"))
for i in range(1, inputfromuser + 1):
    if inputfromuser % 20==0 :
        print("shake")
    elif inputfromuser % 15==0 :
        pass
    elif inputfromuser % 5==0 :
        print("move")
    elif inputfromuser % 3==0:
        print("bye")
    else:
        print("the number you entered was",inputfromuser)