numbers = [1, 232, 43, 54, 76, 4, 5, 12]

x_max = max(numbers)
x_min = min(numbers)

h = []

for el in numbers:
    if el % 2 == 0:
        h.append(el * x_min)
    else:
        h.append(el * x_max)

numbers = h

print(numbers)
