'''I think keeping 2**X outside the loop will improve the code performance because in this case for each iteration of a loop the value of 2**X will not be computed.
The code can be written as follows.
using while-else construction and using for loop to form L and keeping 2**X outside the loop
creator : Krishnendu Maji  '''
L=[]
for m in range(7):
    L.append(2**m)
X=5
G=2**X
j=0
while j<len(L):
    if G==L[j]:
        print('at index',j)
        break
    j+=1
else:
    print(X,'not found')
#the same task can be done by other method keeping 2**X outside the loop by using same type of code as shown above #
