int1=int(input('Enter the intervel 1 :\n'))
int2=int(input('enter the intervel 2 :\n'))
if(int2==0):
	print('Enter the positive number')
else:
	for x in range(int1+1,int2):
		if (x%2!=0):
			print x