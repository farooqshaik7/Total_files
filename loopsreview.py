###### LISTS ##### List data type is a ordered sequence of elements that can composed of strings, numbers and even lists.
                     # List is a mutable and zero based index.

developer = ['jessica', 'charan', 'mega', 12]
del developer[3]
print(developer)
dev = 'jessica' in developer
print(dev)
##############

devel = ['Alice', 19, 'Rust developer']
name, age, job = devel
print(age)
#######
devel1 = ['Alice', 19, 'Rust developer','Google']
name, *remaining = devel1
print(*remaining)
##########

numbers = [1,2,3,4,5,6]
numbers.pop(3)
print(numbers)
##########
numbers1 = [1,2,7,9,0]
numbers.pop()
print(numbers)
#######
numbers2 = [1,2,3,4,5]
numbers2.clear()
print(numbers2)
##########

numbers4 = [1,2,3,4,5]
numbers4.insert(2,2.5)
print(numbers4)
#####
numbers5 = [1,2,4,6,8]
numbers5.reverse()
print(numbers5)


###### TUPLES #####   Tuple data type is a ordered sequence of values. tuple can obtain different type of data types and tuples are immutable

coder = ('Squad', 19, 'developer')
ind = coder[1]
print(ind)
cod1 = 'Squad' in coder
print(cod1)
######
coder1 = 'Jessica'
print(tuple(coder1))
####### 

developer12 = ('Alice', 34, 'Rust Developer')
name, age, job = developer12
print(name)
#########

coder2 = ('Rust', 'Python', 'C++', 'Python', 'Java', 'Python')
cod3 = coder2.count('Python')
print(cod3) 
#############

programming_languages = ('Rust', 'Python', 'C++', 'golang', 'Java', 'C#')
programming_languages1 = sorted(programming_languages, key = len)
print(programming_languages1)
#######

for code in 'char':
    print(code)
#######

# secret_number = 4
# guess = 0

# while guess != secret_number:
#     guess = int(input('Guess a number (1-5):'))
#     if guess != secret_number:
#         print("Wrong! Try again")
# print("Your guess is right")
#########

#### Break Statement ###
developers = ['Jessica', 'Alice', 'Farooq']
for developer in developers:
    if developer == 'Alice':
        break
    print(developer)
#######
print("Hello Farooq")

developer_names = ['Jessica', 'Alice', 'Farooq']
for developer in developer_names:
    if developer == 'Alice':
        continue
    print(developer)
########

words = ['name', 'aeroplane', 'sky', 'fly', 'orange', 'rhythm']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}'  contains the vowel '{letter}'")   
            break
    else:
        print(f"'{word}' has no vowels")
########

for num in range(2,11,2):
    print(num)
#######

numbers = list(range(2,11,2))
print(numbers)
#######

##### Enumerate ###

languages = ['java', 'c++', 'python', 'golang', 'rust']

for index, language in enumerate(languages):
    print(f"index '{index}, and language '{language}'")
########

print(list(enumerate(languages)))
######

##### Zip #####
developers6 = ['java', 'c++', 'python', 'golang', 'rust']
ids = [1,2,3,4,5]

for name , id in zip(developers6, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
######

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_words(word):
    return len(word) > 4
len_word = list(filter(is_long_words, words))
print(len_word)
#######

celsius = [0, 10, 20, 30, 40, 50]

def is_fahrenheit(temp):
    return (temp * 9/5) + 32
fahrenheit = list(map(is_fahrenheit, celsius))
print(fahrenheit)
#####

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
pro = programming_languages.index('Python', 3)
print(pro)
#######

list0 = [6,7,3,4,1,0,23,21,90,600]
list0.sort()
print(list0)
###########

list000 = [1,2,3,4,5,7,9]
list000.insert(2,2.5)
print(list000)
########

