
#function to add arbitrary number of arguments#
def arb_adder(*d):
    sum = d[0]
    for i in range(1,len(d)):
       sum+=d[i]
    return sum
print(arb_adder(1,2,3))