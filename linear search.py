my_array = [
    [0, 9, 8, 5, 3, 6, 4, 2, 7, 4, 3],
    [2, 4, 6, 7, 2, 1, 2, 3, 8, 7, 8]
]
found = False
rows = len(my_array)
col = len(my_array[0])
num = int(input("Please enter a number :"))
for i in range(rows):
    for x in range(col):
        if my_array[i][x] == num:
            found = True
if found == True:
    print("Number Found")
else:
    print("Not Found")
