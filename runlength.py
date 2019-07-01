from collections import OrderedDict
def runlength(x):
    #assigning every character of string with value 0
    dict=OrderedDict.fromkeys(x,0)
    #incrementing count characters if present in input string
    for ch in x:
        dict[ch]+=1
    #adding characters and counter in string format
    result=''
    for key,value in dict.items():
        result=result+str(key)+str(value)
    return result
s="aaaabbbbccccddaaa"
value=runlength(s)
print(value)

