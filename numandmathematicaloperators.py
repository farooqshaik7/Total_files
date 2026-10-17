num1 = 50
num2 = -7
print(type(num1))
print(type(num2))
sum = num1 + num2
subtraction = num1 - num2
multi = num1 * num2
division = num1 / num2
modular = num1 % num2
floor_division = num1 // num2
Exponentiation = num1 ** num2
print("integer addition:", sum)
print("integer subtraction:", subtraction)
print("integer multiplication:", multi)
print("integer division:", division)        # same for floating values
print("modular remainder:", modular)
print("integer floor dividion:", floor_division)
print("Integer exponentiation:", Exponentiation)


num3 = -4.51
num4 = 35.8
num5 = 34
rounded = round(num3)
rounding = round(num4)
absolute = abs(num3)
power = pow(num3, num3)
print(rounded)
print(rounding)
print(absolute)
print(power)



my_var = 10
my_var += 5        #with augumented assignment
print(my_var)      #same for subtraction,multiplication,division,modulus,floor dividion and exponentiation

my_vari = 12
my_vari = my_vari + 4   #without augumented assignment
print(my_vari)

variable = " Hello "

variable += " world "
print(variable)

variable1 = " Hello "
variable1 *= 3        #other augumented assignment operators throw typeerror
print(variable1)

my__var = 5
my__var += 1 
print(my__var)

#conditional statements

age = 19

if age >= 19:
    print("You are eligible for driving licence")
#########
Age1 = 15

if  Age1 >= 19:
    print("You are an adult")
else:
    print("You are not an adult yet")
#########

Age = 10

if Age >= 20:
    print("You are eligible for driving")
elif Age >= 15:
    print("You are a teenager")
else:
    print("You are a child")

print(bool(0))
print(bool(""))
print(bool(False))

print(bool(1))
print(bool("Hello"))
print(bool(True))


is_citizen = True                     #Usage of "and" operand 
age = 23

if is_citizen and age >= 18:
    print("You are elizible to vote")
else:
    print("you need to grow")
    

Is_citizen = True                    #Usage of "or" operand
age = 18

if Is_citizen or age >= 19:
    print("Ypu are elizible for student discount")
else:
    print("you are not")


is_citizens = False                 

if not is_citizens:
    print("Access denied for non-administrators")
else:
    print("Welcome, Administrators")

