# Exercise 1: Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 2: Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 3: Same last digit
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a % 10 == b % 10:
    print("True")
else:
    print("False")

# Exercise 4: Print 1 to 10 with tab
for i in range(1, 11):
    print(i, end='\t')
print()

# Exercise 5: Even numbers between 23 and 57
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# Exercise 6: Prime number check
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# Exercise 7: Prime numbers between 10 and 99
for num in range(10, 100):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 8: Sum of digits
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)

# Exercise 9: Reverse number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)

# Exercise 10: Palindrome check
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
