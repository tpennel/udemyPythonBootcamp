# # Problem 1
# # Create a generator that generates the squares of numbers up to some number N.
# def gensquares(N):
#     for num in range(N):
#         yield num**2
#
# for x in gensquares(10):
#     print(x)

# # Problem 2
# # Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# # Note: Use the random library. For example:
# import random
# # random.randint(1,10)
# def rand_num(low, high, n):
#     for num in range(n):
#         yield random.randint(1, 10)
#
# for num in rand_num(1, 10, 12):
#     print(num)

# # Problem 3
# # Use the iter() function to convert the string below into an iterator:
# s = 'hello'
# iter_s = iter(s)
# print(next(iter_s))
# print(next(iter_s))
# print(next(iter_s))
# print(next(iter_s))
# print(next(iter_s))

# Problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
# When you, either don't know the input amount or will be using a large input amount as it will save memory space

# Extra Credit!
# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
# it is a compression of a function creating a list from another list with if statement then iterating through it
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
