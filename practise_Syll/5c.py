# three positive integers a, b, and c are Pythagorean triples if a2+ b2 =c2. Write 
# a function to generate all Pythagorean triples in a certain range. 

def Pythagorean_(start,end):
  triples = []

  for a in range(start,end+1):
    for b in range(a,end+1):
      c=int((a**2+b**2)**0.5)

      if c**2 == (a**2+b**2) and c<=end:
        triples.append((a,b,c))
  return triples

print((Pythagorean_(1,20)))