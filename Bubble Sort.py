my_array = [2, 3, 7, 5, 6, 17, 8, 99, 0]
j = int(len(my_array))
for n in range(j-1):
    for i in range(j-n-1):
        if my_array[i] > my_array[i+1]:
            my_array[i], my_array[i+1] = my_array[i+1], my_array[i]
print(my_array)

