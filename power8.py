'''using in opertor membership operation and for loop to construct L
creator : Krishnendu Maji  '''
L=[]
for m in range(7):
    L.append(2**m)

X=5
if(2**X in L ):
        print('at index', L.index(2**X))
else:
    print(X, 'not found')
