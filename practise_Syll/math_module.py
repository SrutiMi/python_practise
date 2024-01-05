import math

# print(dir(math))

x=math.gcd(12,6)
print (x)

#Area of a circle
r = int(input('radius'))
area = math.pi * (r**2)
rounded = round(area,2)
print(rounded)

#perimeter
perimeter = 2 * math.pi * r
print(round(perimeter, 3))