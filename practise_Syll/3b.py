''' From a list of words, join all the words in the odd and even indices to form 
two strings. Use list slicing and join methods. '''

# Code:
words = ["hello" ,"girl" ,"you","did","it"]

even = words[::2] #this will return a list
odd =words[1::2]

print (even)
print (odd)

#using join
even1= " ".join(words[::2])
odd1= " ".join(words[1::2])
print(even1,odd1)