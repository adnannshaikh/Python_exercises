# Ask the user for a string and print out whether this string is a palindrome or not.
word = input("Enter a word: ")
rvs = word[::-1]

if word == rvs:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
