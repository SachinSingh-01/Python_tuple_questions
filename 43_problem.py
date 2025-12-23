# Count how many odd numbers are present in this tuple:
# t = (11, 22, 33, 44, 55, 66)
t = (11, 22, 33, 44, 55, 66)
odd_count=0
for i in t:
    if i%2!=0:
        print(i)
        odd_count+=1
print("No of odd number present:",odd_count)
