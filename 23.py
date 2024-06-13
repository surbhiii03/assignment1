#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()
if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius,"°C is ",fahrenheit,"°F")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit,"°F is", celsius,"°C")
else:
    print("Invalid input. Please enter 'C' or 'F'.")
