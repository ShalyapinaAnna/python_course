number = int(input("number: "))
summary = 0
while number != 0:
    summary = summary + number % 10
    number = number // 10
print(summary)

