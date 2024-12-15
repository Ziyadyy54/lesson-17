inputfromuser=input("enter a Word ")
a=0
for i in inputfromuser:
    if (i=="a"):
        print("a is found after",a,"times")
        break
    else:
        a=a+1