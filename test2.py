a = input("a:")
b = input("b:")
while b != 0:
    a, b = b, a%b

print(a)
