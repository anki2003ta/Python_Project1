def fibbo(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)
while True:
	x=input("Enter the number:")
	if not x:
		break
	num=int(x)
	result=fibbo(num)
	print('The {0}th term in a Fibonancci series is:{1}'.format(x,result)) 