#A SIMPLE MATHEMATIC TABLE CALCULATOR

#asking for a number to calculate the tables of
number = int(input("What do you want to calculate the tables of: "))

amount = int(input("What is the extend: "))
for i in range(1,amount):
    #print every table
    print(i,"*",number + 1,"=",i*number)
input("press enter to exit")