# Exercise 3
# Your solution comes here
n = int(input("Enter how many seconds since the begining of the day: "))
hours = n // 3600 % 24
minutes = (n % 3600) // 60
seconds = (n % 3600) % 60
print(f"{hours}:{minutes}:{seconds}")