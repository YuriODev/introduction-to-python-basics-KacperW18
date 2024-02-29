# Exercise 9
# Your solution comes here
h = int(input())
m = int(input())
s = int(input())
total_seconds = h * 3600 + m * 60 + s
angle = 360 / (12*3600 / total_seconds)
print(angle)