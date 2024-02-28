# Exercise 4
# Your solution comes here
input = int(input("Enter a four digit number"))
num1 = input // 1000
num2 = (input % 1000) // 100
num3 = (input % 100) // 10
num4 = input % 10

result = (num1 + num2) // (num3 + num4)
print(result)