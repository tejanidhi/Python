n=int(input("Enter n value:"))
z=0

def calc(size,no_of):
    even_list=[]
    odd_list=[]

    for i in range(0,no_of):
        if(size[i]%2==0):
            even_list.append(size[i])
        else:
            odd_list.append(size[i])

    even_list.sort()
    odd_list.sort()
    new_odd_list=[]

    n=len(odd_list)
    while n>0:
        new_odd_list.append(odd_list[n-1])
        n=n-1

    for ele in even_list:
        new_odd_list.append(ele)
    return new_odd_list


values=[]
while(z<n):
    no_of=int(input("enter size of list:"))
    size=list(map(int,input().split()))
    result=calc(size,no_of)
    values.append(result)
    z=z+1
for i in range(len(values)):
    for j in range(len(values[i])):
        print(values[i][j],end=" ")
    print()
