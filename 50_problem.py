'''Given the tuple:
data = ("Sachin", (90, 85, 88), "Pass")
Write a program to:
Unpack the tuple into variables
name
marks (nested tuple)
result
Calculate the average marks using the unpacked values'''
data = ("Sachin", (90, 85, 88), "Pass")
(name,marks,result)=data
average=(marks[0]+marks[1]+marks[2])/len(marks)
print("name:",name)
print("marks:",average)
print("result:",result)
