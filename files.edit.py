file = open("teams.txt","r")

lines = file.readlines()

line1 = "This is a new line \n"
line2 = lines[1]
line3 = lines[2]
line4 = lines[3]
line5 = lines[4]

file.close()

file = open("teams.txt","w")

file.write(line1)
file.write(line2)
file.write(line3)
file.write(line4)
file.write(line5)

file.close()

file = open("teams.txt","r")
print(file.readlines())
file.close()