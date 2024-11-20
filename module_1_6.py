my_dict = {"Sasha": 4.7, "Max": 4.0, "Olya": 3.7}
my_dict["Max"] = 4.0
my_dict["Renata"] = 4.75
my_dict.update({"Artem": 3.9, "Kira": 2.8})
del my_dict["Max"]
print(my_dict)

my_set = {707, 1, False, "True", 707,1,6}
my_set.update({8,"pop", 96})
my_set.discard(707)
print(my_set)