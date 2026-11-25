
x = int(input("Enter the first side: "))
y = int(input("Enter the second side: "))
z = int(input("Enter the third side: "))

if (abs(y - z) < x < y + z) and \
   (abs(x - z) < y < x + z) and \
   (abs(x - y) < z < x + y):

    print("A triangle can be formed with these sides.")
else:
    print("A triangle cannot be formed with these sides.")
