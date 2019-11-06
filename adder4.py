'''generalize the function so that it can take arbitrary number of keyword arguments'''
def arb_key_adder(**b):
    sum=0
    for value in b.values():
        sum+=value

    return sum
print(arb_key_adder(good=2,ugly=2))
