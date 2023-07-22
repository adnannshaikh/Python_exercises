# write a program that prints out all the elements of the list that are less than 5.
# Instead of printing the elements one by one,
# make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.

some_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num1 = int(input("Enter a number to check the list: "))
dup = []
for item in some_list:
    if item < num1:
        dup.append(item)


print(dup)