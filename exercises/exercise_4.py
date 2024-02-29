# Exercise 4
# Your solution comes here

input = int(input())
num1 = input // 1000
num2 = (input % 1000) // 100
num3 = (input % 100) // 10
num4 = input % 10


result = (num1 == num4) * (num3 == num2)
print(result)