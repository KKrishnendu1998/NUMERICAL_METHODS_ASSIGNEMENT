'''using for-else construction and using for loop to construct L
creator : Krishnendu Maji  '''
L=[]
for m in range(7):
    L.append(2**m)

X=5
for k in L:
    if 2 ** X == k:
        print('at index', L.index(k))
        break
else:
    print(X, 'not found')
