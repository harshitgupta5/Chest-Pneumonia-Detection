# Python program to check if the number is an Armstrong number or not

# take input from the user
n = int(input("Enter a number: "))

sum = 0

temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")