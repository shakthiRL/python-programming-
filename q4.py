a, b = 0, 1
print(a)
print(b)

for _ in range(10):  
    c = a + b
    print(c)
    a, b = b, c
