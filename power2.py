'''using while-else construction
creator : Krishnendu Maji  '''
L=[1,2,4,8,16,32,64]
X=5
j=0
while j<len(L):
    if 2**X==L[j]:
        print('at index',j)
        break
    j+=1
else:
    print(X,'not found')
