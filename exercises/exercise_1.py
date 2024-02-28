# Exercise 1
# Your solution comes here
number = int(input("Enter a five digit number: "))
first = (number // 10000) + (number //100 % 10) + (number % 10)
second = (number // 1000 % 10) + (number // 10 % 10)
print(str(first)+str(second))