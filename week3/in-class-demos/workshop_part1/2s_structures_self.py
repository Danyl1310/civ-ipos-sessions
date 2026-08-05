#Exercise 1a manually create 2d structure

my_2d_list = [[1,2,3],[4,5,6],[7,8,9]]

#Random Access

#Whole list of lists
print(my_2d_list)
#One list in list
print(my_2d_list[0])
#One item from list within list
print(my_2d_list[1][2])

print('#'*20)

# Exercise 1b

row = [0, 1, 2]
my_2d_list = [row] * 3

print("Before:", my_2d_list)

#Update one element in first row
my_2d_list[0][0] = 99
print("After:", my_2d_list)

print('#'*20)

# Exercise 2
for row in my_2d_list:
    for grid_square in row:
        print(grid_square)

print('#'*20)
