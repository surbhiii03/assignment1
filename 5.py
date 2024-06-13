#Write a program that takes a string input from the user and writes it to a text file
userinput=str(input("Enter a string: "))
samplefile=open("C:/Users/devja/Desktop/code/question5.txt",'w')
print(userinput,file=samplefile)
print("String has been written to the required text file")