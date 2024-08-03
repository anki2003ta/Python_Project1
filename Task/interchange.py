def swapList_approach1(newList):
	size = len(newList)
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	print("Approach 1:",newList)
def swapList_approach2(newList):
	newList[0], newList[-1] = newList[-1], newList[0]
	print("Approach 2:",newList)
def swapList_approach3(newList):
	get=(newList[-1],newList[0])#packing
	newList[0],newList[-1]=get #unpacking
	print("Approach 3:",newList)
def swapList_approach4(newList):
	start,*middle,end=newList
	newList=[end,*middle,start]
	print("Approach 4:",newList)
numbers1=[]
numbers2=[]
numbers3=[]
numbers4=[]
while True:
	y=input("Enter the list of numbers:")
	if not y:
		break
	num= int(y)
	numbers1.append(num)
	numbers2.append(num)
	numbers3.append(num)
	numbers4.append(num)
def main():
	print("List for Approach1:",numbers1)
	print("List for Approach2:",numbers2)
	print("List for Approach3:",numbers3)
	print("List for Approach4:",numbers4)
	swapList_approach1(numbers1)
	swapList_approach2(numbers2)
	swapList_approach3(numbers3)
	swapList_approach4(numbers4)
main()