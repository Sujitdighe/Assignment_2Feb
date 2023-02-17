''' Q1.  Explain with an example each when to use a for loop and a while loop.

Q2.  Write a python program to print the sum and product of the first 10 natural numbers using for
and while loop.

Q3. Create a python program to compute the electricity bill for a household.

Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
that list.
The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.


You are required to take the units of electricity consumed in a month from the user as input.


Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250.

Q5.  Write a program to filter count vowels in the below-given string.

string = "I want to become a data scientist'''


#Q1 Answer------>>>
'''A for loop is typically used when you want to 
iterate over a sequence of values such as a list, tuple, or range of numbers. A while loop is used when you want to continue executing a 
block of code as long as a certain condition is met.'''
# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# while loop
i=0
while i < 5:
    print(i)
    i=i+1

# Q2 Ans------------------------->>>>>>>>>>>>

# Sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum:", sum)

# Product of first 10 natural numbers
product = 1
for i in range(1, 11):
    product *= i
print("Product:", product)

#Using while loop:


# Sum of first 10 natural numbers
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print("Sum:", sum)

# Product of first 10 natural numbers
product = 1
i = 1
while i <= 10:
    product *= i
    i += 1
print("Product:", product)

#Q3 ans----------------------->>>>>>>>
units = int(input("Enter the units consumed: "))
total_cost = 0

if units <= 100:
    total_cost = units * 4.5
elif units <= 200:
    total_cost = 100 * 4.5 + (units - 100) * 6
elif units <= 300:
    total_cost = 100 * 4.5 + 100 * 6 + (units - 200) * 10
else:
    total_cost = 100 * 4.5 + 100 * 6 + 100 * 10 + (units - 300) * 20

print("Total electricity bill: Rs.", total_cost)


# using for loop

cubes = []
for i in range(1, 101):
    cube = i**3
    if cube % 4 == 0 or cube % 5 == 0:
        cubes.append(i)
print(cubes)

# using while loop

cubes = []
i = 1
while i <= 100:
    cube = i**3
    if cube % 4 == 0 or cube % 5 == 0:
        cubes.append(i)
    i += 1
print(cubes)


#Q5 ans---------->>>>





