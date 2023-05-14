# largest among three numbers
a = int(input("enter first no."))
b = int(input("enter second no"))
c = int(input("enter third no"))
if a > b and a > c:
    print(a, "is biggest")
elif b > c:
    print(b, "is biggest")
else:
    print(c, "is biggest")
# printing pattern A
for i in range(5):
    j = 5 - i - 1
    while j >= 0:
        print("*", end="")
        j -= 1
    print()
# printing pattern B
for i in range(4):
    for j in range(5):
        if i == 0 or i == 3 or j == 0 or j == 4:
            print("#", end="")
        else:
            print(" ", end="")
    print()
# printing pattern C

for i in range(3):
   for j in range(i):
       print(" ", end="")
   for k in range(i, 5-i):
       print("$", end="")
   print()

