# Ask the user for his name, and then print a greeting message test
print("Enter your name:")
x = input()
print("Hello, " + x)

# Ask two users for their names, and then tell them who got the longest name.
print("Enter your name 1:")
x = input()
print("Enter your name 2:")
y = input()
if len(x) > len(y):
    print(f"The user {x} have longest name")
else:
    print(f"The user {y} have longest name")

# Ask a user for his name, and if it starts with a vowel, greet him
vowel_letters = ["a","e","i","o","u"]
print("Enter your name:")
x = input()
if x[0].lower() in vowel_letters:
    print(f"Hello {x}")

# Ask the user for his name, and tell him if the last letter is a vowel or a consonant
vowel_letters = ["a","e","i","o","u"]
print("Enter your name:")
x = input()
length = len(x)
if x[length - 1].lower() in vowel_letters:
    print("Last letter is vowel")
else:
    print("Last letter is consonant")

# Ask the user for two numbers (one after the other) and then print their sum
print("Enter first number:")
x = int(input())
print("Enter second number:")
y = int(input())
print("The sum is",x+y)

# Challenge the user to print the longest sentence without any “A”, if he achieves it,
# tell him how many letters he wrote, else, print a fail message.

# TO-DO

# Ask the user for his full name (example: “John Doe”), and check the validity of his answer:
#
# The name should contain only letters.
# The name should contain only one space.
# The first letter of each name should be upper cased.

# TO-DO

# Ask the user for a sentence, and then tell him how many words are in it.
print("Enter sentence:")
x = input()
res = len(x.split())
print ("The number of words in string : " +  str(res))

# Write a python program to get a string made of the first 2 and the last 2 chars from a given string,
# if the string length is less than 2, return instead the empty string.
# For example: "Helloworld" output "Held", while "Sik" returns ""

# TO-DO

# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY)
# and then tell him how old he turnt/will turn this year.
# TO-DO

# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY)
# and then tell him how old he is today.
# TO-DO

# ************************* For loops *************************************
# Write a program that counts the number of element for a list, without the len function.
name=['Alex','Mike','Dylan','Yossi']
counter = 0
for name1 in name:
    counter += 1
print('The count of element:', counter)

# Write a program that print every name that starts by ‘a’
name=['Alex','Mike','Dylan','yossi','Alan']
for name1 in name:
    if (name1[0] == "A"):
        print(name1)
# Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.
for x in range(10):
  if (x != 3 and x != 6):
  	print(x)
# Use a for loop to print the numbers from 1 to 20, inclusive.
for i in range(1, 21):
    print(i)
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
list1 = list(range(1, 1000001))
for i in list1:
    print(i)
# Make a list of the numbers from one to one million, and then use min() and max() to
# make sure your list actually starts at one and ends at one million.
list1 = list(range(1, 1000001))
for i in list1:
    print(i)

print("min value element : ", min(list1))
print("min value element : ", max(list1))

# Write a program that returns the index of the first occurrence of an item in a list.
list1 = list(range(1, 100))
index = list1.index(5)
print('The index of 5:', index)

# Write a little program that concatenate two lists together without using the + sign.
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]

for i in list2:
    list1.append(i)
print(list1)
# Create a board as following by using for loops:
#X
#XX
#XXX
#XXXX
#XXXXX
#XXXXXX
#XXXXX
#XXXX
#XXX
#XX
#X

for i in range (0, 6):
    for j in range(0, i + 1):
        print("x ", end='')
    print("\r")
for i in range (6, 0, -1):
    for j in range(0, i -1):
        print("x ", end='')
    print("\r")

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
threes = list(range(3, 31, 3))

for number in threes:
    print(number)

#  Write a program that insert an item at a defined index.
# to do

# cars question
# to do

# You have two lists, current_players and new_players, use a while loop to
# transfer every player from new_players to current_players.
current_players = ['Mario', 'Luigi', 'Peach']
new_players = ['Blue Toad', 'Red Toad', 'Green Toad']

current_players = current_players + new_players
print(current_players)

# there are missing excerises

# Write a program that put each word of a string in a list without using the split function.
sentence = 'This is a sentence to split without split'
split_value = []
tmp = ''
for c in sentence:
    if c == ' ':
        split_value.append(tmp)
        tmp = ''
    else:
        tmp += c
if tmp:
    split_value.append(tmp)

print(split_value)

# Write a program that prints the longest word in a list.
words=["alpha","omega","up","down","over","under","purple","red","blue","green"]
sortedwords = sorted(words, key=len)
print ("The longest word in the list is: " + sortedwords[-1])
