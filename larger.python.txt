a=int(input('Enter the num1: \t'))
b=int(input('Enter the num2: \t'))
c=int(input('Enter the num3: \t'))
if(a > b) and (a > c):
	print('a is larger')
elif(b > a) and (b > c):
	print('b is larger')
else:
	print('c is larger')