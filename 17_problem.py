'''Count how many times 3 appears in:
nums = (1, 3, 4, 3, 2, 3, 9)'''
nums = (1, 3, 4, 3, 2, 3, 9)
count=0
for n in nums:
    if n==3:
        count+=1
print("No. of time 3 appear:",count)