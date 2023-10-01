for j in range(int(input())):
    n=int(input("Enter the number"))
    for number in range (1,n):  
        if number > 1:  
            for i in range (2, number):   
                if (number % i) == 0:  
                    break  
            else:  
                print (number) 