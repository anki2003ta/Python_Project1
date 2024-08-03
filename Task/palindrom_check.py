def palindrom_number(number):
	temp=number
	r=0
	while(number>0):
		d=number%10
		r=r*10+d
		number=number//10
	if(temp==r):
		return 1
	else:
		return 0
def removeSpaces(sentence):
	count=0
	list=[]
	for i in range(len(sentence)):
		if(sentence[i] != ' '):
			list.append(sentence[i])
	string=''.join(list)
	return string
def palindrom_sentence(sentence):
	
	string1=sentence.lower()
	string=reversed(string1)
	if(list(string) == list(string1)):
		return 1
	else:
		return 0	
while True:
	x=input("Enter the number:")
	if not x:
		break
	num=int(x)
	result=palindrom_number(num)
	if(result==1):
		print("Palindrom Number")
	else:
		print("Not a Palindrom Number")
while True:
	x=input("Enter the sentence:")
	if not x:
		break
	sentence=removeSpaces(x)
	result=palindrom_sentence(sentence)
	if(result==1):
		print("Palindrom Sentence")
	else:
		print("Not a Palindrom Sentence")