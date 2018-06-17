num1=raw_input()

num2=raw_input()

list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if num1 in list:
	
    print('enter the number')

if num2 in list:
	
    print('Enter the number')

else:
	
    num3=int(num1)*int(num2)
	
    if(num3%2==0):
		
        print('even')
	
    else:
		
        print('odd')