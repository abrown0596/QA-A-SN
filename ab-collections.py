
listvar1 = ["meat","veg","cake","beer for the weekend"]
# indexes:    0      1      2              3
#            -4     -3     -2             -1
#[] square brackets
#() parentheses
#{} curly brackets
#<> angle brackets/greek brackets
# < = bra     > = ket

print(listvar1)

#indexing

print(listvar1[1]) # would print 'veg'
print(listvar1[-1]) # would print 'beer for the weekend'

print("")

print("updated list")
listvar1 = ["meat","veg","cake","beer for the weekend",20]
print(listvar1)

#lists containing lists:
cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_animals[1][0]) # prints 'baaaarnaby' from cool_sheep list

#appending items into list
listvar1.append('pies')
print(listvar1)


#inserting into list


#length
print(f"Length of list1 is {len(listvar1)}")



#TUPLES

#tuples use parentheses (not square brackets like lists)
listvar2 = (1,2,3,4)
print(listvar2)

print(listvar2[3])


print("")

#Dictionaries
dictvar1 = {"cow":"moo", "sheep":"baa", "dog":"bark"}
print(dictvar1)

print(dictvar1["sheep"]) # prints the item associated to the 'sheep' key
print(dictvar1.items()) # prints all items in doictionary (key/value pairs)
print(dictvar1.keys()) # just prints the keys
print(dictvar1.values()) #just prints values


#TUTORIAL

books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])






