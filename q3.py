print("Prime numbers from 0 to 20:")
for number in range(21):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                break
        else:
            print(number)
