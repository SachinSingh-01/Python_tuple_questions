# Write a program to print all elements of a nested tuple using loops:
# t = (1, (2, 3), (4, 5, 6))
t = (1, (2, 3), (4, 5, 6))

for item in t:
    if isinstance(item, tuple):
        for value in item:
            print(value)
    else:
        print(item)
