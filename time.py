Time=int(input('Ente the time in miniute:\n'))

h=0

m=0

if (Time>0):
	
    h=Time/60
	
    m=Time%60
	
    print(h,m)

else:
	
    print('Enter the valid number')
	