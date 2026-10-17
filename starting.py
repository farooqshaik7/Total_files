string1 = """sum
and mltiplication"""
print(string1)

string2 = 'It\'s raining today' # use back slash if you use same quotes
print(string2)

string3 = 'python programming'
print('python' in string3)

string4 = " Hello world "
print(len(string4))
print(string4[3])
print(string4[-4])

greetings = "Hi"
greetings = "Hi Babe"
print(greetings)

str1 = "Hello"     #String concatination
str2 = "Farooq"
Adding = str1 + " " + str2
print(Adding)

str3 = "Hello"
int4 = 5
sum = str3 + str(int4)
print(sum)
# or
sum = str3
sum += str(int4)
print(sum)  # += is using for adding both

stri1 = "python"          # string interpolation
stri2 = "Language"
stri1_and_stri2 = f'welcome to {stri1} pogramming {stri2}'
print(stri1_and_stri2)

str_slice = " Hello world "
print(str_slice[0:8])
print(str_slice[1:9:2])
print(str_slice[::-1])


my_str = "hello world"       #converts lower case to upper
upper_str = my_str.upper()
print(upper_str)

my_str1 = " HELLO WORLD "
lower_str1 = my_str1.lower()  #converts upper case to lower
print(lower_str1)


my_str2 = '    hello world    '
my = my_str2.strip()         
print(my)


my_str3 = " Hello world "
replace_str = my_str3.replace("Hello", "Hi")   #replace(old, new)
print(replace_str)

my_str4 = " Hi farooq"
my_split = my_str4.split()     
print(my_split)

my_str5 = ["Hello", "world"]
my_join = " ".join(my_str5)
print(my_join)

string1 = " Hello world "
my_stri = string1.startswith(" Hello")
print(my_stri)

string2 = " Hello world "
my_stri = string2.endswith(" Hello ")
print(my_stri)

string3 = " Hello world "
my_str = string3.find("world")
print(my_str)

string4 = " Hello world "
my_str = string4.count("l")
print(my_str)

string1 = "hello world"
my__str = string1.capitalize()
print(my__str)

string2 = "Hello world"
my__str1 = string2.isupper()
print(my__str1)

string3 = "hello world"
my__str2 = string3.islower()
print(my__str2)

string4 = "hello world"
my__str3 = string4.title()
print(my__str3)

