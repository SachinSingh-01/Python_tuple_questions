'''Change the first element of this tuple to "Python":
langs = ("Java", "C", "C++")'''
langs = ("Java", "C", "C++")
lst_langs=list(langs)
lst_langs.pop(0)
lst_langs.insert(0,"python")
print(lst_langs)
