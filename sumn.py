n=int(input('Enter the number: \n'))
k=int(input('Enter the k value: \n'))
sum=0
i=1
while(sum<n):
	sum=sum+1
	print(sum)
if(k>n):
	print('enter the k value within the range of n')
else:
	while(i<k):
		sum=sum+i
		i=i+1
print('sum is',sum)
 