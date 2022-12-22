from random import uniform

n = int(input())
n_min = float(input())
n_max = float(input())

list_random = []
count = 0

for i in range(n):
    list_random.append(uniform(-10, 10))

for el in list_random:
    if n_min < el < n_max:
        count += 1

print(list_random)
print(count)
