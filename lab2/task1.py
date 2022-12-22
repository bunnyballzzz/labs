words = ['a', 'adasd', 'dasds', 'das']
my_list = []

for el in words:
    my_list.append(len(el))

result = (max(my_list) + min(my_list))

print(my_list)
print(result)
