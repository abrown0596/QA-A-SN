#QA Community Tutorial:

# file = open("filename.txt","r")

# outfile = ""

# for line in range(1,10):
#     if line % 2 ==0:
#         outfile += file.readline()
#     else:
#             file.readline()

# file = open("filename.txt","w")
# file.write(outfile)
# file.close()


#QA Community Exercise:



file = open("teams.txt","w")

for n in range(1,6):
    newline = "Team" + str(n) + "\n"
    file.write(newline)

file.close()

file = open("teams.txt","r")
lines = file.readlines()
print(lines [0])
print(lines [3])

file.close()