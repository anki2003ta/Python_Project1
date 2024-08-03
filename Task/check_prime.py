def prime(number):
	count=0
	for i in range(2,number-1):
		if(number%i==0):
			count=count+1
	#print(count)
	return count
def sum_of_digits(number):
	s=0
	while(number>0):
		d=number%10
		s=s+d
		number=number//10
	if(s%2==0):
		return 1
	else:
		return 0
def main():
	for i in range(100,200):
		result1=prime(i)
		result2=sum_of_digits(i)
		if(result1 ==0 and result2 == 1):
			print(i,"is prime and sum of digits is even---")
		elif(result1 >0 and result2 == 1):
			print(i,"is not a prime and sum of digits is even")
		elif(result1 >0 and result2 == 0):
			print(i,"is not a prime and sum of digits is odd")
		elif(result1 ==0 and result2 == 0):
			print(i,"is prime and sum of digits is odd")
main()