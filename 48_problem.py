# Convert this tuple into a list, sort it, and convert it back to tuple:
# t = (5, 2, 9, 1, 7)
t = (5, 2, 9, 1, 7)
lst=list(t)
lst.sort()
t=tuple(lst)
print(t)