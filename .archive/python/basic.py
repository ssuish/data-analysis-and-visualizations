from code import interact

# Python Basics
print("Numeric Data Types") # print function
num1 = 5; print(num1, " ", type(num1)) # integer
num2 = 6.0; print(num2, " ", type(num2)) # float
num3 = 3j; print(num3, " ", type(num3)) # complex

x = 20; y = 15  # basic syntax
print("\nBasics Arithmetic Operations")
print(f"Addition: {x + y}") # f-string (string interpolation)
print("Substraction: %s" %(x - y)) # %-formatting (string interpolation)
print("Multiply: {}" .format(x * y)) # Str.format() (string formating and interpolation)
print("Division: {result}" .format(result = x / y)) # Str.format() (string formating and interpolation)
print("Modulus: " + str(x % y)) # can't concatenate different data types, str() formats data-type -> string
print("Floor Division: %s" %(x // y)) # returns int value discarding fractional result
print("Exponent: %s" %(x ** 2)) # returns x^2, REMINDER: ** has higher precedence than -

print(f"{'name': > 20}")

