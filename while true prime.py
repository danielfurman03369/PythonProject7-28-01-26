sum_: int = 0
i:int = 0

while True:

    a: int = int(input("Enter a price: "))
    sum_ += a
    i += 1

    if sum_ > 1000:
        break

print("The sum is: ", sum_)
print('the amount of products: ',i)