var1 = "adam" #sring
var2 = 50 #integer
var2a = 50.0 #float
var3 = True #boolean
var4 = int(var2a)
var5 = str(var2)


print(var1 + var1) #can print 2 of the same variable (concatenation)
print(var2 + var2a) #prints the sum of two variable types (have to be floats/ints)
print(var1 + str(var2)) #concat with data type change
print(var1,var2) #preformatted concat (adds space and allows different variable types)
#F string - allows for different data types
print(f"I like {var1}{var2}")

var6 = "Hello my name is \"Adam\"" # escape character is '\', this allows double quotes which usually confuses python
print(var6)

var7 = "I want text \n over two seperate lines" # includes line break where '\n' is typed
print(var7)




