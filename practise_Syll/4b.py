''' Using while loops to do Gaussian addition on a list having an even number of 
numbers. Print each partial sum. Eg: if the list is [1, 2, 3, 4, 5, 6], the program 
should output “1 + 6”, “2 + 5”, and “3+4” in separate lines, and the result of 
the addition “21”. Extend it to handle lists of odd length'''

list1=[1, 2, 3, 4, 5, 6]
i=0
sum=0
while i<len(list1)/2 :
   print (f'{list1[i]} + {list1[-(i+1)]}')
   sum+=list1[i]+list1[-(i+1)]
   i+=1

print(f'The sum is {sum}')