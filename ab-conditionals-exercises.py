#Tutorial

devs_money = 100
dev_can_play_smash = False

if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament!")
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")


#Exercise

# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"

mark = int(input("Enter mark here: "))

if mark > 85:
    print("Distinction")
elif mark >= 65:
    print("Pass")
else:
    print("Fail")

if mark >85:
    print("Distinction")
    if mark >=65 and mark <85:
        print("Pass")
else:
    print("Fail")   # needs extra work as does not work

#Integer Test
num = input("Enter number here: ")

if int(num)%2 == 0:
    print("Number is even")
else:
    print("Number is odd")


#Letter Test

char = input("Type letter here: ")
vowels = ['a','e','i','o','u']
if char in vowels:
    print("Letter entered is a vowel!")
elif char =='y':
    print("Letter 'Y' is sometimes a vowel and sometimes it isn't!")
else:
    print("Letter entered is a consonant!")

#Sides test

sides = int(input("Enter number of sides here: "))

if sides < 3:
    print("Your shape has less than 3 sides!")
elif sides < 4:
    print("Your shape is a Triangle!")
elif sides < 5:
    print("Your shape is a Square!")
elif sides < 6:
    print("Your shape is a Pentagon!")
elif sides < 7:
    print("Your shape is a Hexagon!")
elif sides < 8:
    print("Your shape is a Heptagon!")
elif sides < 9:
    print("Your shape is a Octagon!")
elif sides < 10:
    print("Your shape is a Nonagon!")
elif sides < 11:
    print("Your shape is a Decagon!")
elif sides >= 11:
    print("Your shape has more than 10 sides!")


year = int(input("Please enter a year: "))
if year%400 == 0:
    print("This year is a leap year!")
elif year%100 == 0:
    print("This year is NOT a leap year!")
elif year%4 == 0:
    print("This year is a leap year!")
else:
    print("This year is NOT a leap year!")


