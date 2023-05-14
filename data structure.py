# dictionary comprehension
from typing import List

s = str(input("enter a string")).lower()
print(s)
keys = set(s)
my_dict = {k: s.count(k) for k in keys}
print(my_dict)
# finding pairs
l = [1, 2, 4, 4, 5, 3, 6, 7, 1, 3]
s=len(l)
pairs  = []
sum = int(input("enter the expected sum "))
for i in range(0,s):
    for j in range(i+1,s-1):
        if l[i]+l[j]== sum:
            pairs.append((min(l[i], l[j]),max(l[i],l[j])))
print(set(pairs))
#task5

str1=str(input("enter the first string"))
s1= set(str1)
print(s1)
str2= str(input("enter the second string" ))
s2= set(str2)
print(s2)
str3= (s1^s2)
print(str3)
