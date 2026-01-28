_sum: int = 0
_avg: int = 0
i: int = 0

while True:

    grade: int = int(input("Enter a grade: "))

    if grade == -999:
        break

    if grade > 100 or grade < 0:
        continue


    i += 1
    _sum += grade

if i == 0:
    print("No grades")

else:
    _avg = _sum // i
    print("Average grade: ", _avg)