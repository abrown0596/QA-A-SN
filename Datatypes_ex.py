# Exercise in QA community


#Tutorial

word1 = "Good"
word2 = "Day"
word3 = "Adam"

sentence = word1 + " " + word2 + " " + word3

print(sentence)

#Exercises

#Q1: What will be the output of this code?
number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)
#Answer: It will ask for a whole number and a decimal number from the user (as input) and then print the int, 
# with the float and the float rounded.

print("")

#Q2: What is this piece of code doing?
# Pet
name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)
#Answer: this code is returning the variables within the sentence (where variable is boolean it will print 'True/False')