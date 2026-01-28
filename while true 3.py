


num:int = int(input("Enter a number: "))

if num == 1:
    print("not prime")

else:

    i:int = 2
    while True:

        if num % i == 0:
            print("not prime")
            break

        else:
            print("prime")
            break

        i = i + 1