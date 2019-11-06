'''
Programme name : programme to print first 10 fibonacci numbers
creator : Krishnendu Maji
'''
a=0                 #the value of 1st number#
b=1                 #the value of second number#
i=0
print('first ten fibonacci numbers are','\n', a,'\n',b)       #printing the 1st two values#
count=2
while(i>=0 and count<10):
    c=a+b
    print(c)             #printing the next values#
    a=b
    b=c
    count+=1

