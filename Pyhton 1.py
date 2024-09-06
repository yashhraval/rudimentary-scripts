    # #type conversion

# a = 6  
# b = 7.56
# sum = a + b #python will automatically consider a as float instead of int.
# print(type(a))
# print(sum) #13.56

    # #type casting

# a= int(6.7)  #manually defined the datatype as float instead of int.
# b= 7.56
# sum = a+b
# print(type(a))
# print(sum) #13.56

    # #input

# a = int(input("enter value for a:"))    #entered value will be saved as int a=7
# b = int(input("enter value for b:"))    #entered value will be saved as int b=7
# print(a+b) #14 #sum

# a = input("enter value for a:")     #entered value will be saved as str a=7
# b = input("enter value for b:")     #entered value will be saved as str b=7
# print(a+b) #77 #concatenated

    # #practice = area of square

# side = float(input("Enter value of side:"))
# print("area =",side*side) #can use side**2 instead of side*side

    # #practice = average of 2 numbers

# a = float(input("enter value for a:"))
# b = float(input("enter value of b:"))

# print("average is:", (a+b)/2)

    # #practice = true / false

# a = input("enter a:")
# b = input("enter b:")
# print(a>=b)