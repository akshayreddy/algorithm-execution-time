
# Insertion sort, Quick Sort and Randomise Quick Sort
#Akshay Reddy


from random import randint
from decimal import Decimal
import timeit
import sys
sys.setrecursionlimit(100000000)                             #to avoid stack overflow because to the recusrion



def InsertinSort(ItemsList):                                  #insertion sort 
	N=len(ItemsList)
	for j in range(1,N):
		CurrentItem=ItemsList[j]
		i=j
		while i>0 and ItemsList[i-1]>CurrentItem:
			ItemsList[i]=ItemsList[i-1]
			i=i-1
		ItemsList[i]=CurrentItem

	return ItemsList


def Partition(arr,low,high):
	pivot=arr[high]                                           #choosing the last item as the pivot
	i=low-1
	for j in range(low , high):
		if arr[j]<=pivot:
			i=i+1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return (i+1)

def QuickSort(ItemsList,low,high):                             #Quick sort
	if low < high:  
		p = Partition(ItemsList,low,high)
		QuickSort(ItemsList, low, p-1)
		QuickSort(ItemsList, p+1, high)
	return ItemsList



def RandomisedPartition(arr,low,high):
	RandomPivot=randint(low,high)

	temp=ItemsList[high]
	ItemsList[high]=ItemsList[RandomPivot]
	ItemsList[RandomPivot]=temp
	
	pivot=arr[high]
	i=low-1
	for j in range(low , high):
		if arr[j]<=pivot:
			i=i+1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return (i+1)


def RandomisedQuickSort(ItemsList,low,high):                     #randomised Quick sort
	if low < high:
		RandomPivot=randint(low,high)

		temp=ItemsList[high]
		ItemsList[high]=ItemsList[RandomPivot]
		ItemsList[RandomPivot]=temp                              #choosing a random pivot and swaping with the last item

		p = RandomisedPartition(ItemsList,low,high)
		RandomisedQuickSort(ItemsList, low, p-1)
		RandomisedQuickSort(ItemsList, p+1, high)
	return ItemsList



FileName=sys.argv[1]
N=int(sys.argv[2])
ItemsList=[]
f=open(FileName,"r+")
for i in f:
	ItemsList.append(i.replace("\n",""))

ItemsListIV=[]
ItemsList=map(int,ItemsList)                         #To convert input file contaings items of string type to int

X=input("Make a choice\n1.)InsertionSort\n2.)QuickSort\n3.)RandomisedQuickSort\n")

if X == 1:
	start=Decimal(timeit.default_timer(),5)
	print InsertinSort(ItemsList)
	end=Decimal(timeit.default_timer(),5)
	print "\n"
	print "Size of lsit="+str(N)
	print "Excution time="+str(end-start)
elif X==2:
	start=Decimal(timeit.default_timer(),5)
	print QuickSort(ItemsList,0,N-1)
	end=Decimal(timeit.default_timer(),5)
	print "\n"
	print "Size of lsit="+str(N)
	print "Excution time="+str(end-start)
elif X==3:
	start=Decimal(timeit.default_timer(),5)
	print RandomisedQuickSort(ItemsList,0,N-1)
	end=Decimal(timeit.default_timer(),5)
	print "\n"
	print "Size of lsit="+str(N)
	print "Excution time="+str(end-start)