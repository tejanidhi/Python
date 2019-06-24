inputString='abDEg:1789,bcdFw:2679'
val=inputString.split(',')


def square(x):
  sum=0
  while x>0:
    rem=x%10
    sum=sum+rem*rem
    x=x//10
  return sum



first_value=val[0]
first_split=first_value.split(':')
first_string=first_split[0]
first_integer=first_split[1]
sum_one=square(int(first_integer))

second_value=val[1]
second_split=second_value.split(':')
second_string=second_split[0] #second_integer
second_integer=second_split[1]#second integer
sum_two=square(int(second_integer))

if sum_one%2==0:
	x=first_string[-1]+first_string[0:-1]
	print(x)
else:
	x=first_string[-1]+first_string[0:-1]
	y=x[-1]+x[0:-1]+','
	print(y)

if sum_two%2==0:
	x=second_string[-1]+second_string[0:-1]
	print(x)
else:
	x=second_string[-1]+second_string[0:-1]
	y=x[-1]+x[0:-1]+','
	print(y)





