#Write a python program that returns the minimum and maximum values in a list of numbers
lst=list(map(int,input("Enter numerical elements of the desired list separated by space: ").split()))
print("The list provided: ",lst)
print("Maximum value in the list: ",max(lst))
print("Minimum value in the list: ",min(lst))