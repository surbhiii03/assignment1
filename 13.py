#Write a program that asks the user for their birth year and calculates their age.
birthyear=int(input("Enter the user's Birth Year: "))
currentyear=int(input("Enter current year: "))
age=currentyear-birthyear
print("User's age in",currentyear,"is: ", age)