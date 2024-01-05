fruits=["apples", "kiwi", "mango"]

#instead of this code 
# for fruit in fruits:
#   print(fruit)

#write the below one
# [print(fruit) for fruit in fruits]
# _____________________________________

#example 2 --->
# new_fruits = []

# for fruit in fruits:
#   fruit =fruit.upper()
#   new_fruits.append(fruit)

# fruits = new_fruits
# print(fruits)

# fruits=[fruit.upper() for fruit in fruits]
# print(fruits)

# ______________________________________________

#example 3 -->
bits = [False,True,True,False]
# new_bits = []

# for b in bits:
#   if b == True:
#     new_bits.append(1)
#   else:
#     new_bits.append(0)

# print(new_bits) 

# new_bits=[1 if b == True else 0 for b in bits ]
# print(new_bits)

# _________________________________________

# example 4 --->

my_string = "HelloMyNameIsSruti"
my_string = "".join(
  [i if i.islower() else " " +i for i in my_string])
print(my_string)
# _______________________________________