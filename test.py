lst1 = [1, 2, 3]
lst2 = lst1

lst2.extend([5, 6])
lst1.append([-1, 0, 1])

lst3 = lst2[:]
lst3.insert(3, lst2.pop(3))

print(lst1 is lst2)

print(lst1)
print(lst2)
print(lst3)
