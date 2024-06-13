#Write a python program that takes a list of numbers and returns their sum.
lst=list(map(int,input("Enter numerical elements of the desired list separated by space: ").split()))
sumOfNumbers=sum(lst)
print("The sum of the numbers in the list: ",sumOfNumbers)