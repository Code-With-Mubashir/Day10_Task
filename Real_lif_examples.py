# Some real life Examples
# 1.Convert celsius to fahrenheit
# Example No.01
tempreature_in_celsius = float(input("Enter the tempreature in celsius: "))
    tempreature_in_fahrenheit = (tempreature_in_celsius * 9/5) + 32
    print(f"The tempreature in fahrenheit is: {tempreature_in_fahrenheit}°F")
    
    
# 2. Calculate area of Rectangle
# Example No.02
length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
area_of_rectangle = length * breadth
print(f"The area of rectangle is: {area_of_rectangle} square units")
    
# 3. Calculate area of Circle
# Example No.03
radius = float(input("Enter the radius of circle: "))
area_of_circle = 3.14 * radius * radius
print(f"The area of circle is: {area_of_circle} square units")
    
# 4. Calculate Simple Interest
# Example No.04
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time_period = float(input("Enter the time period in years: "))
simple_interest = (principal * rate_of_interest * time_period) / 100
print(f"The simple interest is: {simple_interest}")

# 5. Eligible for vote
# Example No.05
Enter_your_age = int(input("Enter your age"))
if Enter_your_age <= 18:
    print("You are not eligible for vote")
else:
    print("You are eligible for vote")
    
    
# 6. Check even or odd
# Example No.06
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
    
# 7. Check prime number
# Example No.07
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
        
else:
    print(f"{num} is not a prime number")
    
# 8. Find largest number among three numbers
# Example No.08
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c
    
# 9. Calculate factorial of a number
# Example No.09
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")

