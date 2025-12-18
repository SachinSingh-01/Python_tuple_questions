# Write a program to check whether an element exists in a tuple without using in keyword.
name=("Sachin","Moni","kakali","Doggy","Crimsy","Pippo")
found=False
n=input("Enter the name to check present or not:").upper()
for i in name:
    if i==n:
        found=True
        break
if found:
    print("Yes present")
else:
    print("No not present")