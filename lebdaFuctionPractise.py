
# 01  write a lembda function to find quare of  a number 

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11)) 
# print(mytripler(11))


# lambda num: num**2
# result = lambda num: num**2
# result(20)

num = 5
square = num ** 2
print(square)

# numbers = [4]
lambda num: num ** 2
squares = lambda num: num ** 2
squares(20)
# print(squares)


# 02 Write a lambda function that takes a number as input and returns true if it is even otherwise false
lambda num: num ** 2
squares = lambda num: num ** 2
squares(20)


result = lambda x : f"{x} is true" if x %2==0 and   x % 0 == 0 else f"{x} is false"
print(result(0))

even_odd = lambda num: num % 2 == 0
even_odd(int(input("enter a number: ")))



# 03 write  a lambda that takes two number as a input and returns the maximum of the two

maximum1 = lambda x,y : min(x,y)
maximum1(12,45)

maximum2 = lambda x,y : max(x,y)
maximum2(12,450)

# maximum2 = lambda x,y : x if x > y you can not use if without else in lambda
maximum2 = lambda x,y : x if x > y else y
maximum2(1200,45000)


# 04 write a lambda function that takes a string as input and returns it reverse
# 05 write a lambda function that takes a string as input and returns count vovels in a string 
# 06 write a lambda function that generate fabonacii sequence up to am terms
# 07 write a lambda function that check prime number