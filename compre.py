

nums = [1,2,3,4,5,6,7,8,9,10]

###For basics

#for x in nums:

#   print(x)

### Append

#my_list = []


#for n in nums:



#    my_list.append(n)

#print(my_list)
#####

#my_list = [n for n in nums]

#print(my_list)

###################

# for n*n for each n times

#my_list = []

#for n in nums:
#    my_list.append(n*n)

#print(my_list)

## use this

#my_list = [n*n for n in nums]


#print(my_list)

##### Print even numbers form List

#my_list = [n for n in nums if n % 2 == 0]

#print(my_list)

my_list = []

for letter in 'abcd':

    for num in range(4):

        my_list.append((letter,num))

#print(my_list)

# In one line

my_list1 = [(let,n) for let in 'dsaf' for n in range(4)]

#print(my_list1)



# Dictionary Comprehension


names = ['bruce', 'stark', 'cap', 'thor']

heros = ['batman', 'ironman', 'superhuman', 'alien']

my_dict = {name : hero for name, hero in zip(names, heros)}

#print(my_dict)

### Decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

say_whee()


### try Decorators

def smart_sub(func):
    def inner(a, b):

        if a < b:
            a, b = b, a
        else:
            pass



        return func(a,b)
    return inner

def sub(a,b):

    print(a - b)

sub = smart_sub(sub)

num1 = int(input("Enter First Number : "))

num2 = int(input("Enter Second Number : "))

sub(num1, num2)


