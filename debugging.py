# for i in range(5)    # red line as colon ':' is not at the end
# print("pies")

# if 5 > 10:
#     print("5 is less than 10")
# else:
#     print("5 is greater than 10") # this is a logic error as 5 is actually less than 10 but prints "5 is greater than 10"

#static analysis is looking through your code manually for errors without executing it

#dynamic analysis is the testing and evaluation of a program by executing data in real-time

# import pdb

# pdb.set_trace()

# a="aaa"
# b="bbb"
# c="ccc"

# final = a + b + c
# print(final)

#ex1
# user_funds = 10.31
# item_price = 12 #price not defined

# if item_price < user_funds:
#     print("You have enough money!") # print with capital P
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price > user_funds: # Logic error, used < instead of >
#     print("Sorry you don't have enough money")  #added quotes around string

#ex2
# total = 0 # defined total
# def product(n):
#     total = 1 #removed equals
#     for i in n: # for i in n, not for n in n
#         total *= i
#     return total # moved return to inside the function (indented)

# print(product([4,4,5]))

#ex3
# import pdb

# pdb.set_trace()

# def is_prime(x):
#     if x <= 2:
#         return True
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return False
#             else:
#                 return True
# print(is_prime(12))

#ex4
# import pdb
# pdb.set_trace()

# item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
# n = 0

# while n < 5:
#     for i in item_list:
#         print(i)
#     n += 1

# print (item_list[n-1])


