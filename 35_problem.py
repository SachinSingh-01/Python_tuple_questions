'''Write a program to:
Change 20 to 200
Without directly modifying the tuple
t = (10, 20, 30)'''
t = (10, 20, 30)
lst=list(t)
lst[1]=200
t=tuple(lst)
print(t)