''' Ask the user to enter two numbers, and output the sum, product, difference, 
and the GCD '''

#i am not going to use any pre defined functions

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f'The sum of {num1} and {num2} is {num1 + num2}')
print(f'The difference between {num1} and {num2} is {num1 - num2}')
print(f'The product between {num1} and {num2} is {num1 * num2}')
print(f'The division between {num1} and {num2} is {num1 / num2}')

#GCD

while num2:
    num1, num2 = num2, num1 % num2
print(f'The GCD is {num1}')