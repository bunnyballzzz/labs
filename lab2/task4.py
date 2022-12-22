while True:
    lst_numbers = list(map(int, input().split()))
    if len(lst_numbers) >= 4:
        break
    print('error')

lst_no_extremum = []
for i in lst_numbers:
    lst_no_extremum.append(i)

lst_no_extremum.remove(min(lst_no_extremum))
lst_no_extremum.remove(max(lst_no_extremum))

print(lst_no_extremum)
print(lst_numbers)
