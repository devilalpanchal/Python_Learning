# 1. Print Hello World.
print('hello world')


# 2. Write a Program to add two numbers.
a = 10
b = 20
c = a+b
print(c)

# 3. Find and Calculate Squatre root. Using Input.
import math
a = int (input('Enter a number'))
input(print(math.sqrt(10)))
print (math.sqrt(9))

# 4. How to calculate area of triangle. Using Input. solution - (0.5 * base * height) 

base = float(input("base length of the triangle: "))
height = float(input("height of the triangle: "))

area = 0.5 * base * height
print("area of triangle is:", area)

# 5. Swap two variables. Change the places.
x = 5
y = 10


temp = x
x = y
y = temp
print(x)
print(y)

# 6. Convert Kilometers to Miles.

# First you read this line and after you can go belove code

# 1 kilometre equals 0.62137 miles.  
# Miles = kilometre * 0.62137  
# And,  
# Kilometre = Miles / 0.62137  

def kilometre(km):  
    milesInOneKM= 0.621371  
    miles = km * milesInOneKM  
    print ("The speed Miles: ", miles)  
km = float (input ("Please enter the speed Kilometre as a unit: "))  
kilometre(km)  

# 7. Is a number positive, negative or Zero?


def check(number):
     
    # if the number is positive
    if number > 0:
        print("Positive")
         
    # if the number is negative
    elif number < 0:
        print("Negative")
         
    # if the number is equal to
    # zero
    else:
        print("Equal to zero")
         
check(5)
check(-458)
check(-5)
check(00)
       
# 8. Is a number Odd or Even?

def check(number1):
     
    if number1 % 2:
        print("Even")
    else:
        print("odd")
         
check(5)
check(458)
check(22)
check(00)

# 9. Check Leap Year.  

year =int(input('Enter Your Year')) 
if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
    print ( f"{year} is a leap year .") 
else :
    print(f"{year} is not a leap year.")

# 10. Find Largest among three numbers.
    num1 = 10
    num2 = 30
    num3 = 20
# max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)
    
# 11. Write a program to check Prime Numbers.
  
#   Prime numbers are numbers that have only 2 factors: 1 and themselves. For example, the first 5 prime numbers are 2, 3, 5, 7, and 11. By contrast, numbers with more than 2 factors are call composite numbers
  def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
# Test the function
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# 12. Write a program a genrate a random number.
    
    # Importing the random module  
import random  
  
# Using randint function from the random module  
num = random.randint(100, 200)  
  
print("Random Integer between 100 to 200:", num)  
print("Random Integer between 100 to 200:", random.randint(100, 200))  
print("Random Integer between 100 to 200:", random.randint(100, 200))  


# 13. Write a program to print all Prime numbers in an Interval.

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
# 14. Convert Celsius to Farenheit.
# 15. Find factorial on a number.
# 16. Display the multiplication table.
