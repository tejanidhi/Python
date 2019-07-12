values=list(map(int,input().split()))
n=values[0]
del values[0]


def smallest_element(ele):
    val=str(ele)
    a=val[0]
    b=val[1]
    c=val[2]
    numlist=[]
    numlist.append(int(a))
    numlist.append(int(b))
    numlist.append(int(c))
    numlist.sort()
    return numlist

sliced_values=[]
for ele in values:
    result=smallest_element(ele)
    smallest_ele=result[0]
    largest_ele=result[2]
    smallest_ele_int=int(smallest_ele)
    largest_ele_int=int(largest_ele)

    sum1=largest_ele_int*11+smallest_ele_int*7
    length_of_digits=len(str(sum1))
    if(length_of_digits==3):
        sliced_ele=int(str(sum1)[1:])
    else:
        sliced_ele=sum1

    sliced_values.append(sliced_ele)
print(sliced_values)

even_list=[]
i=0
while i<len(sliced_values):
    even_list.append(sliced_values[i])
    i=i+2
print(even_list)

odd_list=[]
i=1
while i<len(sliced_values):
    odd_list.append(sliced_values[i])
    i=i+2
print(odd_list)

sliced_even_list=[]
for i in even_list:
    ele=str(i)[0]
    sliced_even_list.append(ele)
print(sliced_even_list)

sliced_odd_list=[]
for i in odd_list:
    ele=str(i)[0]
    sliced_odd_list.append(ele)
print(sliced_odd_list)

count0=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
for i in sliced_odd_list:
    if(i=='1'):
        count1=count1+1
    if(i=='2'):
        count2=count2+1
    if(i=='3'):
        count3=count3+1
    if(i=='4'):
        count4=count4+1
    if(i=='5'):
        count5=count5+1
    if(i=='6'):
        count6=count6+1
    if(i=='7'):
        count7=count7+1
    if(i=='8'):
        count8=count8+1
    if(i=='9'):
        count9=count9+1
    if(i=='0'):
        count0=count0+1
count_list=[]
if(count0>1):
    count_list.append(count0)
if(count1>1):
    count_list.append(count1)
if(count2>1):
    count_list.append(count2)
if(count3>1):
    count_list.append(count3)
if(count4>1):
    count_list.append(count4)
if(count5>1):
    count_list.append(count5)
if(count6>1):
    count_list.append(count6)
if(count7>1):
    count_list.append(count7)
if(count8>1):
    count_list.append(count8)
if(count9>1):
    count_list.append(count9)

count0=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
for i in sliced_even_list:
    if(i=='1'):
        count1=count1+1
    if(i=='2'):
        count2=count2+1
    if(i=='3'):
        count3=count3+1
    if(i=='4'):
        count4=count4+1
    if(i=='5'):
        count5=count5+1
    if(i=='6'):
        count6=count6+1
    if(i=='7'):
        count7=count7+1
    if(i=='8'):
        count8=count8+1
    if(i=='9'):
        count9=count9+1
    if(i=='0'):
        count0=count0+1

if(count0>1):
    count_list.append(count0)
if(count1>1):
    count_list.append(count1)
if(count2>1):
    count_list.append(count2)
if(count3>1):
    count_list.append(count3)
if(count4>1):
    count_list.append(count4)
if(count5>1):
    count_list.append(count5)
if(count6>1):
    count_list.append(count6)
if(count7>1):
    count_list.append(count7)
if(count8>1):
    count_list.append(count8)
if(count9>1):
    count_list.append(count9)

print(count_list)
result=0
for i in count_list:
    result=result+i-1
print(result)




















