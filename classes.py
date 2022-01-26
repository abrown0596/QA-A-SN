# class Dog:
#     energy = "high"

#     def speak(self):
#         print("woof")

# bilbo_waggins = Dog()

# scooby_doo = Dog()

# print(bilbo_waggins.energy)
# bilbo_waggins.speak()

# class Dog:
#     #energy = "high"

#     def __init__(self,energy = "high", food = "dogmeat"):
#         self.energy=energy
#         self.food = food
    
#     def speak(self):
#         print("woof")

# bilbo_waggins = Dog("superhigh","shiremeat")

# scooby_doo = Dog("Lax","ScoobySnax")

# print(bilbo_waggins.energy)
# print("Scooby's energy is",scooby_doo.energy, ". And his favourite food is",scooby_doo.food, ".")
# bilbo_waggins.speak()


#Tutorial
# class Student:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# John = Student("John","21")
# Adam = Student("Adam","25")

# print(getattr(Adam , "age")) #getattr finds age attribute for this object

#Exercise
class Student:
    
    def __init__(self, name, age, _class_):
        self.name = name 
        self.age = age
        self._class_ = _class_

    def avgtest(self,list):
        self.list = list
        list = [(float(input("Enter first test score: "))),
        (float(input("Enter second test score: "))),
        (float(input("Enter third test score: ")))]
        print(f"{self.name}'s average test score = {sum(list)/len(list)}")

adam = Student("Adam", 25, "Maths")

print("Student:",adam.name, 
"\nAge:",adam.age,
"\nClass:",adam._class_,
adam.avgtest)

print("")
# print("Happy birthday!")
# print("")
# adam.age = 26
# print("Student:",adam.name, "\nAge:",adam.age,"\nClass:",adam._class_,"\nTest 1 Score:",adam.score1,"\nTest 2 Score:",adam.score2,"\nTest 3 Score:",adam.score3)

