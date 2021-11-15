number = int(input("What do you want to calculate the tables of: "))
amount = int(input("What is the extend: "))
for i in range(1,amount + 1): print(i,"*",number,"=",i*number)
input("press enter to exit")