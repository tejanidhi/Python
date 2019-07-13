length_of_string=int(input())
string_value=input()
no_of_cases=int(input())
input_list=[]

for _ in range(no_of_cases):
  p=int(input())
  input_list.append(p)

count_list=[]
for ele in input_list:
    val=ele-1
    value=string_value[val]
    count=0
    for i in range(val):
        if (string_value[i]==value):
            count=count+1
    count_list.append(count)
for i in count_list:
    print(i)




