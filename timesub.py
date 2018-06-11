a=int(input("enter the time1:\n"))

b=int(input("enter the miniute 1 :\n"))

c=int(input('enter the time2 :\n'))

d=int(input('Enter the miniute2 :\n'))

time1=0

time2=0

h=0

m=0

time1=(a*60)+b

time2=(c*60)+d

time=time1-time2

if(time==0):
	
    print('Enter the positive number')

else:
	
    h=time/60
	
    m=time%60
	
    print(h,m)