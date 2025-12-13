'''Using asterisk unpacking:
nums = (1, 2, 3, 4, 5)
Store the first element in a, remaining elements in b.'''
nums = (1, 2, 3, 4, 5)
(a,*b)=nums
print(a)
print(b)