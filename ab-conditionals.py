var1 = False


if var1:
    print("My boolean is outputting true")
else:
    print("My boolean is outputting False")


var1 = input("Please type in a number: ")
var2 = input("Please type in another number: ")
var3 = input("Please type in yet another number: ")

#comparators
# ==  equals
# != not equal
# < less than
# > more than
# <= lessthan OR equal to
# >= greater than OR equal to

#Boolean Logic AND, OR, NOT.
if var1 == var2 and var1 == var3:
    print("My boolean is outputting True")
else:
    print("My boolean is outputting False")


if var1 == var2 or var1 == var3:
    print("My OR boolean is outputting True")
else:
    print("My OR boolean is outputting False")

# Using lists:
treevar1 = input("Type in a tree: ")
trees = ["Larch", "Oak", "Pine","Willow"]
if treevar1 in trees:
    print("You have typed a valid tree")
else:
    print("FAIL")

numvar1 = int(input("Type in a number: "))
if numvar1 < 10:
    print("Your number is a single digit integer")
elif numvar1 < 100:
    print("Your number is a two-digit number")
elif numvar1 < 1000:
    print("Your number is a three digit number")
elif numvar1 < 10000:
    print("Your number is a four digit number")
else:
    print("That is a BIG number!")


