n = 10
max_prime=0
for num in range(1, n + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            max_prime = num

print( max_prime)
