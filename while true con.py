i:int = 0
j:int = 0
_sum:int = 0
max:int = None
t:int = 0


while True:
    a: int = int(input("Enter a number: "))

    if a == 0:
        t += 1
        continue

    if a % 7 == 0:
        print("!!!!boom!!!!")
        break

    if a < 0:
        i += 1
        continue

    j += 1
    _sum += a

    if max is None or a > max:
        max = a


print('sum is:', _sum)
print('max is:', max)
print("neg:", i)
print("pos:", j)
print("zeroes:", t)