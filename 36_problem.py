'''Remove the value "banana" from the tuple:
fruits = ("apple", "banana", "cherry", "banana")
(Remove only the first occurrence)'''
fruits = ("apple", "banana", "cherry", "banana")
lst=list(fruits)
lst.remove("banana")
fruits=tuple(lst)
print(fruits)