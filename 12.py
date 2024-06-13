#Write a python program that calculates the sum of the digits of a given number.
number=int(input("Enter a number: "))
sumOfDigits=sum(int(digit) for digit in number)
print("The sum of the digits of the given number is: ", sumOfDigits)