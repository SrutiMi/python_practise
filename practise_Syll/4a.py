''' Use list comprehension to find all the odd numbers and numbers divisible by 
3 from a list of numbers. '''

#rememeber new_list = [expression for item in iterable if condition]

num = [1,7,6,3,9,14]
result =[i for i in num if i % 3 == 0 or i%2 !=0] 
print(result)