'''code for making a list that contains all the Unicode code points of the string S  '''
S='mumbai'
Unicodes=[]
for i in S:
    Unicodes.append(ord(i))    #appending the values of the Unicode code points in the list #
print(Unicodes)                 # printing the list #
#by list comprehension method #
UNICODES=[ord(i) for i in S]    #making the list #
print(UNICODES)                  # printing the list #
#by map class method#
def unicode(a):
    return(ord(a))
b=map(unicode,S)
print('list of the unicodes by map class=',list(b))