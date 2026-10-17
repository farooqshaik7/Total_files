def calculate(a,b):
    print(a+b)
calculate(3,4)
#--------------------------------------
def calculate_sum(a, b):      #Usage of return
    return a + b
my_sum = calculate_sum(3, 1)
print(my_sum)
#---------------------------------------
def my_fun():             #Local scope
    my_var = 10
    print(my_var)
my_fun()
#--------------------------------------

def outer_fun():          #Enclosing scope
    msg = "Hello mister"

    def inner_fun():
        print(msg)
        
    inner_fun()

outer_fun()
#---------------------------------------

def outer_fun():           #This is also for enclosing scope sand to modify
    msg = "Hello Farooq"
    say = ""

    def inner_fun():
        nonlocal say
        say = "How are you?"
        print(msg)
    
    inner_fun()
    print(say)

outer_fun()
#--------------------------------------

my_var = 100              #Global scope

def show_var():
    print(my_var)

show_var()
print(my_var)
#---------------------------------------

my_var_1 = 7              #This is also a global scope and to make it global variable

def show_vars():
    global my_var_2
    my_var_2 = 13
    print(my_var_1)
    print(my_var_2)

show_vars()
print(my_var_2)
#---------------------------------------

my_var = 20

def change_var():
    global my_var
    my_var = 35

change_var()

print(my_var)
#--------------------------------------

#Built-in scope refers to all of python buit-in functions,modules and keywords and are avialable any where in your program.
print(str(40))
print(type(3.4))
print(isinstance(4,str))
#
greetings = "Hello \"Farooq.shaik\""
print(greetings)

Greetings = "Hello"
Greetings += " World"
print(Greetings)

name = "Farooq.shaik"             #f-string
age = 19
messeage = f"My name is {name} and my age is {age}"
print(messeage)

name = "Arief"
initial = "Shaik"
translate = str.maketrans(name, initial)
print(translate)
############

t = str.maketrans('lr', 'br')
sentence =  'The tent gave in to the leaks'

print(sentence.translate(t))
str6 = "Hello world"
str_replace = str6.replace("world", "Farooq")
print(str_replace)

spl = "Hello farooq, how are you?"
print(spl.split)

joi = ["Hello", "Farooq", "shaik"]
print(" ".join(joi))

develop = "Farooq shaik"
print(develop.startswith("F"))
print(develop.endswith("o"))
print(develop.find('o'))
print(develop.count("a"))
print(develop.capitalize())
print(develop.isupper())
print(develop.islower())
print(develop.title())


translate1 = str.maketrans("abc", "123")
print(translate1)

result = "abcabc".translate(translate1)
print(result)

num1 = -4
print(abs(num1))  #used to return the absolute value of a number
print(bin(num1))  #used to convert an integer to its binary representation as a string
print(oct(num1))  #used to convert an integer to its octal representation as a string
print(hex(num1))  #used to convert an integer to its hexadecimal representation as a string

num2 = pow(2, 3)
print(num2)

def sum(num1, num2= 3):
    return num1 + num2
result = sum(2)
print(result)

# type = input("what is your name?")
# print("Hello", type)

import keyword
print(keyword.kwlist)


# def greet():
#     pass
# print(greet())

# name = "Farooq"
# print(list(name))

# programming_languages = ['python', 'java', 'c++']
# programming_languages[-2] = 'javascript'
# print(programming_languages)
# del programming_languages[2]
# print(programming_languages)
# 'python' in programming_languages

# developer = ['Alice', 23, ['python', 'java', 'Rust']]
# print(developer[2])
# print(developer[2][1])  #to access the element in the nested list

developer = ['Alice', '19', 'agentic AI']
name, age, job = developer
print(name)

list = [1,2,3,4,5,6,7,8]
print(list[1:9:2])

list1 = [1,2,3,4]
list1.append(5)           #
even_numbers = [6,8,9,0]
list1.append(even_numbers)
print(list1)

list2 = [10,12,13,14,15]
add_numbers = [20,22,24,26]
list2.extend(add_numbers)  #
print(list2)

list3 = [13,1,4,54,54,22]
list3.insert(3,25)         #
print(list3)
list3.remove(54)           #
print(list3)


list4 = [1,2,3,5,6]
list4.pop(2)              #
print(list4)
list4.clear()             #
print(list4)

list5 = [12,10,15,20,19]
list5.sort()              #
print(list5)

list6 = [13,12,25,19,22]
num0 = sorted(list6)     #
print(list6)
print(num0)
list6.reverse()          #
print(list6)

programming__languages = ['java', 'python', 'rust', 'go lang']
ind = programming__languages.index('python')
print(ind)

################

developer1 = 'jack'
tup = tuple(developer1)  ##
print(tup)

developer2 = ('name', 'age', 'job') ##
tup1 = 'age' in developer2
print(tup1)

developer3 = ('Apple', 'mango', 'banana')  
fruit1, fruit2, fruit3 = developer3       ##or  fruit1, *fruits = developer3# *fruit is assigned for raming values
print(fruit1)

developer4 = ('Rust','c++','Rust','c','java')
dev = developer4.count('Rust')
print(dev)     #if no argument is passed in the count() it will give typeerror
dev1 = developer4.index('c++')
print(dev1)
dev2 = developer4.index('Rust', 0, 2)
print(dev2)
dev4 = sorted(developer4, key=len)
print(dev4)
print(sorted(developer4, reverse=True))

num5 = (1,4,9,3,7,23,111,169)
sorted_1 = sorted(num5)
print(sorted_1)
