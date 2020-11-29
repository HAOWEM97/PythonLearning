Least_so_far = None
print('Before', Least_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if Least_so_far is None:
        Least_so_far = the_num
    elif the_num < Least_so_far:
        Least_so_far = the_num
    print(Least_so_far, the_num)
print('After',Least_so_far)
