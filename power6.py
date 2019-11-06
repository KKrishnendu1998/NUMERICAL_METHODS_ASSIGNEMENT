'''using while-else construction and using for loop to form L
creator : Krishnendu Maji  '''
L=[]
for m in range(7):
    L.append(2**m)
X=5
j=0
while j<len(L):
    if 2**X==L[j]:
        print('at index',j)
        break
    j+=1
else:
    print(X,'not found')
