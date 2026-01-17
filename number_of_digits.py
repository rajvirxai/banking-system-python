# Number of Digits

num = int(input("Enter a number:"))
temp = num
count = 0
num = abs(num)

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num = num // 10

print(f"Number of digits in {temp} is : {count}")
