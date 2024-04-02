my_list = [1,2,3,4]

my_list.append(10)
my_list.append(9)
my_list.append(31)
print("List after appending elements:", my_list)

my_list.remove(2)
print("List after removing element 2:", my_list)

new_list = [4, 5, 6]

my_list.extend(new_list)
print("List after extending with new_list:", my_list)


