# Exercise 9
# Your solution comes here
h = int(input("Enter hours"))
m = int(input("Enter minutes"))
s = int(input("Enter seconds"))
total_seconds = h * 3600 + m * 60 + s
angle = 360 / (12*3600 / total_seconds)
print(angle)