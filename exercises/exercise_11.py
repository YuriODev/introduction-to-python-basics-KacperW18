# Exercise 11
# Your solution comes here
s = int(input("Enter the price: "))
fhundred = s // 500
hundred = (s % 500) // 100
fifty = (s % 100) // 50
ten = (s % 50) // 10
five = (s % 10) // 5
one = (s % 5) // 1
print(fhundred,"(500),",hundred,"(100),",fifty,"(50),",ten,"(10),",five,"(5),",one,"(1)")
