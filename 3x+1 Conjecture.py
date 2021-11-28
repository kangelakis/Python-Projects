import matplotlib.pyplot as plt
import numpy as np

#Function that plots the graph
def graphf(k,l):
    for i in range(k,l+1):
        number = i
        steps = 0
        x=[0] # x-cords of graph
        y=[i] # y-cords of graph
        z=[i] #The legend indication
        max = number

        while (number>1):
            if (number > max):
                max = number
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


            #Plot graph settings
            plt.plot(x,y, color='#6F6F6F', linewidth=0.2, alpha=0.5,marker="o", markersize=0.375,
            markerfacecolor='black',markeredgecolor="black")

            plt.pause(0.15) #The delay between when each point gets added to the graph animation
            plt.legend(z) #Indication on graph of the current number
            plt.xlabel('Steps')
            plt.ylabel('Numbers')
            plt.title(('Y =', number,'Peak =', max))

        print(f"The steps needed for {i} to reach 1 were:", steps)
        plt.pause(2)
        list.clear(x)    
        list.clear(y)


################################################################################
f=True
while (f==True):
    sel = (input("Select <1> for a single number or <2> for multiple: "))
    while (sel != '1' and sel != '2'):
        sel = (input("Invalid input... try again (1/2)"))

    if (sel==1):
        n = int(input ("Select a number to begin the test: "))
        m=n
        x=[0] # x-cords of graph
        y=[n] # y-cords of graph
        z=[n] #The legend indication
        graphf(n,m)
    else:
        n = int(input ("First number: "))
        m = int(input ("Second number: "))
        x=[0] # x-cords of graph
        y=[n] # y-cords of graph
        z=[n] #The legend indication
        graphf(n,m)

    choice = (input ("Continue? (Y/n): ")) #Check whether the user wants to continue

    while(choice!='y' and choice!='Y' and choice!='n' and choice!='N'):
        choice = (input ("Invalid option.. Continue? (Y/n): "))

    if (choice=='Y' or choice=='y'):
        f = True
        clear = (input ("Do you wish to reset the canvas? Y/n: ")) #Check whether the user wants to clear the current figure
        while(clear!='y' and clear!='Y' and clear!='n' and clear!='N'):
            clear = (input ("Do you wish to reset the canvas? Y/n: "))
        if (clear=='Y' or clear=='y'):
            plt.clf() #Clears the current graph 
    else:
        f = False

input("Press any button to continue...") #Terminates the program

