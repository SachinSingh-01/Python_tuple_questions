'''You are given a tuple of numbers:
t = (3, 6, 9, 12, 15, 18, 21)
Write a program to:
Create a new tuple that contains only the elements which are divisible by both 3 and 6
Do not convert the tuple into a list
Use loops and tuple concatenation only'''
t = (3, 6, 9, 12, 15, 18, 21)
new_tuple=()
for i in t:
    if i%3==0 and i%6==0:
        i.__add__(new_tuple)
        print(i)