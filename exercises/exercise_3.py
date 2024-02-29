# Exercise 3
# Your solution comes here
n = int(input())
hours = n // 3600 % 24
minutes = (n % 3600) // 60
seconds = (n % 3600) % 60
print(f"{hours}:{minutes}:{seconds}")