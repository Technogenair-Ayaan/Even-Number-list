print("Welcome to even number list from 1 to 1000")
print("Designed and programmed by Ayaan Ansari")
print("Type the password if you want to continue")
var1 = int(input())
if var1==1234:
    print("Welcome")
    x = 2
    while x < 1000:
        if x%2 == 0:
            print(x)
            x = x+2
else:
    print("Invalid Password")
