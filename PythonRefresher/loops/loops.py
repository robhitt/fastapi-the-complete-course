my_list = [1, 2, 3, 4, 5]

# FOR IN
for num in my_list:
    print(num)

sum_of_for_loop = 0
for num in my_list:
    sum_of_for_loop += num
print(sum_of_for_loop)

# RANGE
for num in range(3, 6):
    print(num)

# WHILE
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # continue will exit the current iteration and move to the next iteration
    print(i)
    if i == 4:
        break  # break exits the loop completely
else:
    print("i is now larger or equal to 5")

# ASSIGNMENT
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
i = 0
while i < 3:
    for day in my_list:
        if day == "Monday":
            continue
        else:
            print(day)
    i += 1

