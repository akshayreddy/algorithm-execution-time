
from random import randint

N=input("Enter the value\n")
ItemsList=[]
for i in range(0,N):
	ItemsList.append(randint(-100,100))


f=open("input1.txt","w")
for i in reversed(ItemsList):
	f.write("%d"%i)
	f.write("\n")
