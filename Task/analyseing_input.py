def sum_numbers(numbers):
	s=0
	for i in numbers:
		s=s+i
	print("Sum of all Numbers:", s) 
def sum_odd_numbers(numbers):
	s=0
	for i in numbers:
		if(i%2 != 0):
			s=s+i
	print("Sum of all Odd Numbers:",s)
def sum_even_numbers(numbers):
	s=0
	for i in numbers:
		if(i%2 == 0):
			s=s+i
	print("Sum of all Even Numbers:",s) 
def count_odd_numbers(numbers):
	c=0
	for i in numbers:
		if(i%2 != 0):
			c=c+1
	print("Count all Odd Numbers:",c)
def count_even_numbers(numbers):
	c=0
	for i in numbers:
		if(i%2 == 0):
			c=c+1
	print("Count all Even Numbers:",c)
def odd_numbers(numbers):
	list=[]
	for i in numbers:
		if(i%2 != 0):
			list.append(i)
	print("List of Odd Numbers:")
	for i in list:
		print(i)
def even_numbers(numbers):
	list=[]
	for i in numbers:
		if(i%2 == 0):
			list.append(i)
	print("List of Even Numbers:")
	for i in list:
		print(i)
numbers = []
while True:
	y=input("Enter the list of numbers:")
	if not y:
		break
	num= int(y)
	numbers.append(num)
def main():
	sum_numbers(numbers)
	sum_odd_numbers(numbers)
	sum_even_numbers(numbers)
	count_odd_numbers(numbers)
	count_even_numbers(numbers)
	odd_numbers(numbers)
	even_numbers(numbers)
main()