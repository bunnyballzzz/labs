n = int(input())
list_of_names = []
for i in range(n):
    info = list(input().split(' '))
    name = info[0]
    old = int(info[1])
    list_of_names.append([name, old])

t1 = []
t2 = []

for el in list_of_names:
    if el[1] < 20 or el[1] > 40:
        t1.append(el[0])
    else:
        t2.append(el[0])

print(sorted(t1))
print(sorted(t2))
