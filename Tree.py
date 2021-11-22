print("Welcome to my first tree program made in python!")
from os import linesep as endl
#Choice a is the quickest python way whereas choice b is a more c++ oriented and standard way
choice = input("Select an option a, b:")
while(choice != "a" and choice != "A" and choice != "b" and choice != "B" ):
    print("Invalid option, try again.")
    choice = input("Select an option a, b: ")

x = int(input("Select the size of the tree: "))

if (choice=="a" or choice=="A"):
    for i in range(x):
        print((x-i-1)*' ' + (2*i+1)*'*')

#Fix why the stars dont appear in line
if (choice=="b" or choice=="B"):
    for i in range(1, x):
        for j in range(1, x-i):
            print(" ")
        for k in range(j+1, x-1+i):
            print("*")