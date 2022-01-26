from itertools import count

#Without Iteration
countdown = 5

# print(countdown)
# countdown = countdown - 1
# print(countdown)
# countdown = countdown - 1
# print(countdown)
# countdown = countdown - 1
# print(countdown)
# countdown = countdown - 1
# print(countdown)
# countdown = countdown - 1
# print(countdown)


#With Iteration
# while countdown > -1:
#     print(countdown)
#     countdown = countdown - 1


# for i in ["cat", "dog", "lemur", "brazilian river snake", "llama"]:
#     print(i)


# cool_animals = ["Winnie the Moo","Moolan","Milkshake", "Mooana","Chris P Bacon"]
# for i in cool_animals:
#     print(i)
#     if i == "Mooana":
#         break
#     #runs code until Mooana is met

# cool_animals = ["Winnie the Moo","Moolan","Milkshake", "Mooana","Chris P Bacon"]
# for i in cool_animals:
#     if i == "Mooana":
#         continue
#     print(i)
    #runs code until it meets Mooana, when it does it skips it and runs the rest of the items in cool animals

#Tutorial
# count = 0
# name = str(input("What is your name?"))

# while count < 5:
#     print(name, "is awesome!")
#     count += 1

#Exercise1
# names = [input("What is name 1? "), input("What is name 2? "), input("What is name 3? "), input("What is name 4? "), input("What is name 5? ")]
# count = 0

# while count <5:
#     print(names[count], "is awesome!")
#     count += 1

#Exercise2
# for i in range (10,21,2):
#     print(i)

#W3 resource exercises (Conditional Statements and Loops)
# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

#1
# nl = []
# for x in range(1500,2701):
#     if x%7 == 0 and x%5 ==0:
#         nl.append(str(x))
# for i in nl:
#     print (i)
        

#5
# word = str(input("Please enter a word: "))

# firstletter = word[0]
# lastletter = word[-1]

# print (firstletter)
# print(lastletter)

# print(word(range(lastletter,firstletter)))


#4 
#Decomposition:
#Need 9 lines to be printed
#use a 'for' loop
#nested for loop
#line of up to 5 *'s
#increment and decrement by one


# printvar = []
# asterix = "* "

# for i in range(9):
#     for printvar in range(i):
#         if len(printvar) > 0 and len(printvar) <5:
#             printvar.append(asterix)
#             print(printvar)
#         else:
#             break
#         if len(printvar) > 1:
#             printvar.pop()
#             print(printvar)

#SOLUTION Q4:

# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

