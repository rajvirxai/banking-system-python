numbers = []
n = int(input("How many numbers: "))

for i in range(n):
    value = int(input("Enter a number: "))
    numbers.append(value)

sum = 0
highest = numbers[0]
lowest = numbers[0]

for num in numbers:
    sum += num
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print(numbers)
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Sum: {sum}")
