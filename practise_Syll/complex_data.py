import cmath
#creating complex numbers

complex1 = complex(2,4)
print(complex1)

complex2 = 2+ 5j
print(complex2)

#Basic operations
print(f'The sum of {complex1} and {complex2} is {complex1 + complex2}') 
print(f'The difference of {complex1} and {complex2} is {complex1 - complex2}')
print(f'The product of {complex1} and {complex2} is {complex1 * complex2}')
print(f'The quotient of {complex1} and {complex2} is {complex1 / complex2}')

#modulus and phase angle 
print(f'The modulus of {complex1} is {abs(complex1)}')

print(f'The phase angle of {complex1} is {cmath.phase(complex1)}')