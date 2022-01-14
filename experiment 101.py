import random

def Randy(num,begin = 1, end = 100):
    #get a random number
    array = []
    number = random.randint(begin, end)
    print('This code will print a random number between 1 and 100')
    
    for count in range(num):
        #while loop  
        while number in array:
            number = random.randint(begin, end)
        #append  random number to array      
        array.append(number)
          
    #return array  
    return array
#print 5 random numbers
print(Randy(5))
