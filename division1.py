'''programme to divide 1 by 0,1,2,3,4
creator : Krishnendu Maji'''
#when we divide something by 0 it showa zero division error#
#The programme to divide 1 by 0,1,2,3,4 is shown below : #
for i in range(5):
    if i==0:
        print('1 divided by ', i, ' is  : indeterminate')

    else:
        print('1 divided by ', i, ' is  :', 1 / i)

