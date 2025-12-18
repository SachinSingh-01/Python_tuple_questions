# Use count() to check if an element appears more than once in a tuple.
t=(3,4,6,3,2,1,8,4,6,4,7,6,8)
num=int(input("Enter the numeber: "))
count=t.count(num)
if count>1:
    print("Yes it appear more than once")
else:
    print("No it's not appear more than once")