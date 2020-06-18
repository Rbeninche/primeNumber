number = int(input("Please enter a number: "))

print()


if number <= 1:
    print("{} is not a prime number".format(number))

else:

    is_prime = True

    for x in range(2, number//2+1):
        if number % x == 0:
            is_prime = False
            break

    if is_prime == True:
        print("{} is a prime number".format(number))

    else:
        print("{} is not a prime number".format(number))
