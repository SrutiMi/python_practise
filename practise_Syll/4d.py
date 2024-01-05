#  generate a list of primes within a user-given range.  

start = int(input("Enter the start:"))
end = int(input("Enter the end:"))
list=[]
'''
Using for loop

for i in range(start,end+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        list.append(i)

print(list)

'''

# Using while loop
i=start
while i<=end:
  count=0
  j=1
  while j<=i:
    if i%j==0:
      count+=1
    j+=1
  if count==2:
    list.append(i)
  i+=1
print(list)