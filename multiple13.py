num1=raw_input()

list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if num1 in list:
	
    print('enter the number')

else:
	
	
    if int(num1)%13==0:
		
        print('multiple of 13')
	
    else:
		
        print('not multiple of 13')