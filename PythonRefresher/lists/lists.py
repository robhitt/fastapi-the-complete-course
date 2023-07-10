my_list = [80, 96, 72, 100, 8]
print(my_list[2])

people_list = ["Eric", "Adil", "Jeff"]

# SLICING
print(people_list[0:2])  # does not include the last index stated

# APPEND
my_list.append(1000)
print(my_list)

# INSERT
my_list.insert(2, 1000)
print(my_list)

# REMOVE
my_list.remove(8)  # only removes the value 8, not the 8th index
print(my_list)

# POP
my_list.pop(0)  # removes the specific index from the list
print(my_list)

# SORT
my_list.sort()
print(my_list)


# EXERCISE
zoo = ["gorilla", "snake", "giraffe", "lion", "capybara"]
zoo.pop(3)
zoo.append("cheetah")
zoo.remove("gorilla")
print(zoo)
print(zoo[0:3])