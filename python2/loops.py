programming_languages = ['rust','c++','java','python']
for languages in programming_languages:
    print(languages)
#######
for char in 'code':
    print(char)
#########
vegies = ['spinach','Bottle Guard']
fruits = ['Apple','Mango','Banana']
for veg in vegies:
    for fruit in fruits:
        print(veg,fruit)
########
# secret_number = 20
# guess = 19

# while guess != secret_number:
#     guess = int(input("Guess the number (1-20): "))
#     if guess != secret_number:
#         print("Wrong! Try again")
    
#     print("You got it!")
#######
names = ['Tom','Jerry','Naomi','Lucy']

for name in names:
    if name == 'Naomi':
        break
    print(name)

for name in names:
    if name == 'Naomi':
        continue
    print(name)
########

for i in range(8,1,-2):
    print(i)
########

languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1
#######

languages1 = ['spanish', 'Urdu', 'Arabic', 'Russian', 'Arabic']

lis1 = list(enumerate(languages1))
print(lis1)
#######

developers = ['Farooq', 'Farooq1', 'Farooq2', 'Farooq3']
ids = [1,2,3,4]

print(list(zip(developers,ids)))
#######

developers = ['Farooq', 'Farooq1', 'Farooq2', 'Farooq3']
ids = [1,2,3,4]

for name, id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"Id: {id}")
#######

even_numbers = []

for num in range(21):
    if num % i == 0:
        even_numbers.append(num)

print(even_numbers)
######3

even_numbers1 = [num for num in range(21) if num%i ==0]
print(even_numbers1)                                        #shortcut to print even_numbers in a list form
# #######

numbers = [1,2,3,4,5,6,7,8,9,10]
result = [(num,"even") if num % 2 == 0 else (num,"odd") for num in numbers]
print(result)
####
numbers2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in numbers2:
    if num % i ==0:
        print("Even",num)
    else:
        print("Odd",num)
########

words = ['Tree','mountain','mangos','bananas','jackfruit']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word,words))
print(long_words)   
#######

celsius = [0,10,20,30,40,50,60,70,80,90]

def to_fahrenheit(temp):
    return (temp*9/5)+32
fahrenheit = list(map(to_fahrenheit,celsius))
print(fahrenheit)
#########

numbers4 = [10,20,30,50]
total = sum(numbers4, 10)
print(total)
#########

def square(num):
    return num ** 2
print(square(4))
######

print(square(3))
#######
