'''programme to compute the sum of the unicode code points
creator : Krishnendu Maji '''
S='mumbai'
sum=0
for i in S:
    sum+=ord(i)
print("the sum of the Unicode code points of the characters in S : ",sum)  # printing the sum #
