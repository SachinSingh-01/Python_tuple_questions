# Given a tuple of marks, find the highest and lowest marks:
# marks = (45, 67, 89, 23, 90, 56)
# (Do not use max() or min())
marks = (45, 67, 89, 23, 90, 56)
largest=marks[0]
smallest=marks[0]
for i in marks:
    if i>largest:
        largest=i
    elif i<smallest:
        smallest=i
print("Largest marks:",largest)
print("smallest marks:",smallest)
        