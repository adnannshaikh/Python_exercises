# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
li = []
div = int(input("Enter a number: "))
for x in range(1,div+1):
    if div % x == 0:
        li.append(x)

print(li)