found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value !=3:
        print(found, value)
    else:
        found = True
        print(found, value)
        break

print('After', found)
