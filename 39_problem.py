'''Write a program that prints all indexes where value 3 occurs:
t = (1, 3, 5, 3, 7, 3, 9)'''
t = (1, 3, 5, 3, 7, 3, 9)
lst=list(t)
for value in t:
    if value==3:
        print(value)
