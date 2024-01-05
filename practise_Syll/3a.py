''' Ask the user for two strings, print a new string where the first string is 
reversed, and the second string is converted to upper case. Sample strings: 
“Pets“, “party”, output: “steP PARTY”. Only use string slicing and + 
operators.'''

str1= input("enter the first string ")
str2= input("enter the second string ")

#reversing a string using slicing
str1= str1[::-1]
print(str1)

#using reversed
print(''.join(reversed(str2)))

#using predefined function
print(str2.upper())

# reversing without using predefined function
str3=""
for i in range(len(str2)-1,-1,-1):
  str3= str3 + str2[i]
print(str3)

#changing to uppercase without using predefined function ASCII of A=65 and a =97
str4=""
for i in range(len(str2)):
  if ord(str2[i])>=97 and ord(str2[i])<=122:
   str4+= chr(ord(str2[i])-32)
  else:
    str4+= str2[i]

print(f'The upper case of {str2} is {str4}')
