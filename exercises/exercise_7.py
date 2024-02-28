# Exercise 7
# Your solution comes here
num = int(input("Enter a four digit number: "))
num1 = num // 1000
num2 = (num % 1000) // 100
num3 = (num % 100) // 10
num4 = num % 10
result = num1 + num2 + num3 + num4
print(result)