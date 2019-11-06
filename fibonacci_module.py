'''it is a module to print first n fibonacci numbers
creator : Krishnendu Maji    '''
def fibonacci(n):        # defining the function to print 1st n fibonacci numbers#
    a = 0                 #the value of 1st number#
    b = 1                 #the value of second number#
    i = 0
    print('first '+str(n)+' fibonacci numbers are :\n',a,'\n',b)   #printing the 1st two values#
    count = 2
    while (i >= 0 and count < n):
        c = a + b
        print(c)                     #printing the next values#
        a = b
        b = c
        count +=1

