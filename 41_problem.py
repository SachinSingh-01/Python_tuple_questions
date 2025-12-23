'''Unpack the tuple so that:
first value → start
last value → end
remaining values → middle
t = (1, 2, 3, 4, 5, 6)'''
t = (1, 2, 3, 4, 5, 6)
(a,*b,c)=t
print(a)
print(*b)
print(c)
