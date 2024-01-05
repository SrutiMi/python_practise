''' Explore the ‘key’ function of sum( ), min( ), max( ), and sort( ) functions 
using lambdas '''

numbers = [1,2,3,4]
result = sum((map(lambda x: x**2,numbers)))
print(result)

words = ["apple", "banana", "cherry", "date"]

#find the word with minimum and maximum length
min_length = min(words, key=lambda x:len(x))
max_length = max(words, key=lambda x:len(x))

print(min_length, max_length)

#sorting the numbers on their remainder when divided by 3
sorted_numbers = sorted(numbers,key=lambda x:x%3)
print(sorted_numbers)

print(sorted(words))