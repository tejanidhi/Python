#reading n value
n=int(input())
#reading a matrix
matrix = []
for i in range(n):
    a=[int(x) for x in input().split(" ")]
    matrix.append(a)
#counting sum of each row and adding sum to list
v=0
sum_values_of_rows=[]
while(v<n):
    for i in range(n):
        sum=0
        if(i==v):
            for j in range(n):
                sum=sum+matrix[i][j]
            sum_values_of_rows.append(sum)
            v=v+1
#counting sum of each column and adding sum to list
u=0
while(u<n):
    for i in range(n):
        sum1=0
        if(i==u):
            for j in range(n):
                sum1=sum1+matrix[j][i]
            sum_values_of_rows.append(sum1)
            u=u+1

#counting sum of  forwad diagnol
d=0
sum_d=0
for i in range(n):
    for j in range(n):
        if(i==j):
            sum_d=sum_d+matrix[i][j]
sum_values_of_rows.append(sum_d)
#counting sum of backward diagnol
b=0
sum_b=0
for i in range(n):
    for j in range(n):
        if(i+j+1==n):
            sum_b=sum_b+matrix[i][j]
sum_values_of_rows.append(sum_b)
#storing first element
first_value=sum_values_of_rows[0]
m=n+n+2
count=0
#checking all list elements are same or not
for x in sum_values_of_rows:
    if x==first_value:
        count=count+1
if(count==m):
    print("yes")
else:
    print("no")

