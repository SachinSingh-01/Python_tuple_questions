'''Convert this tuple into a list, add "Russia", then convert back to tuple:
c = ("Spain", "Italy", "India")'''
c = ("Spain", "Italy", "India")
convert_list=list(c)
convert_list.append("Russia")
print(convert_list)
convert_tuple=tuple(convert_list)
print(convert_tuple)