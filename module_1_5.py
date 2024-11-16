immutable_var = (1, 2, 5, "Sea", False) #Элементы кортежа нельзя изменить, тк кортежи не изменяемые, это неделимое целое
print(immutable_var)
mutable_list = [1, 6, 8, "cat", True]
mutable_list.remove(6)
mutable_list.extend(["milk"])
mutable_list [2] = "dog"
print(mutable_list)