num=int(input('Enter the number: \n'))
if(num==0):
	print('Enter the positive value')
else:
	count=0
	while(num>0):
		num=num//10
		count=count+1
	print(count)