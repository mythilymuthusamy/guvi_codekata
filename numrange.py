num=raw_input()

list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if num in list:
	
    print('Enter the valid number')

else:
	
    if int(num) in range(1,10):
		
        print('yes')
	
    else:
		
        print('no')
	