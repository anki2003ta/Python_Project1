def binarySearch(numbers,low,high,x):
	if(high >= low):
		mid=low+(high-low)//2
		if(numbers[mid] ==x):
			return mid
		elif(numbers[mid] > x):
			return binarySearch(numbers,low,mid-1,x)
		else:
			return binarySearch(numbers,mid+1,high,x)
	else:
		return -1
numbers = []
while True:
	y=input("Enter the number of list to be searched (number only):")
	if not y:
		break
	num= int(y)
	numbers.append(num)
print(numbers)
numbers.sort()
print(numbers)
while True:
	x=input("Enter the number to search:")
	if not x:
		break
	num=int(x)
	result=binarySearch(numbers,0,len(numbers)-1,num)
	if(result !=-1):
		print("Search successfully,element found at position",result)
	else:
		print("The given number is not present in the list")