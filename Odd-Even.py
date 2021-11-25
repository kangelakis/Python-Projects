import matplotlib.pyplot as plt
import numpy as np
number = int(input ("Input a number to begin the test: "))
gr = (input ("Choose the graph method (stem/plot): ")) #gr for graph
x=[0] # x-cords of graph
y=[number] # y-cords of graph
steps = 0

#Checks whether the user has not entered one of the two graph options and makes him choose again
while (gr != 'stem' and gr != 'plot'): 
    gr = (input ("Invalid option, try again... (stem/plot): "))

while (number>1):

    if (number%2==0):
        print((number),"Even: ",number,"/ 2 =", number//2)
        if (number//2 == 1):
            print("Finish!")
        number = number//2
    else:
        print((number),"Odd: ",number,"* 3 + 1 =", (number*3)+1)
        number = (number*3)+1

    steps += 1
    x.append(steps) #Adds the x-cords to the list
    y.append(number) #Adds the y-cords to the list

    if (gr == 'stem'): #Stem graph settings
        markerline, stemlines, baseline = plt.stem(
        x, y, linefmt='gray', markerfmt='D', bottom=1.1)
        markerline.set_markerfacecolor('none')
        plt.title("Stem Graph")
    else: #Plot graph settings
        plt.plot(x,y)
        plt.title("Plot Graph")
    plt.pause(0.001) #The delay between when each point gets added to the graph animation
    plt.xlabel('Steps')
    plt.ylabel('Numbers')

print("The steps needed to reach 1 were:", steps)
plt.legend()
plt.show()

