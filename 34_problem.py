'''Why does this code give an error? Explain and then fix it.
t = (1, 2, 3)
t[1] = 99'''
t = (1, 2, 3)
# t[1] = 99 # it through an error as because tuple are immutable.
lst=list(t)
lst[1]=99
print(lst)
