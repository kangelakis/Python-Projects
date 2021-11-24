#import matplotlib.pyplot as plt

x = []
y=[]
steps=0
y.append(number = int(input ("Input a number to begin the test: ")))
while(number>1):
    if(number%2==0):
        number = number//2
        r = "/2= "
        t = "Even"
    else:
        number = 3*number+1
        r = number,"3x+1= "
        t= "Odd"
    steps += 1
    x.append(steps)
    if(number != 1):
        print(r,number,t)
    else:
        print(r,number,'Final')

    y.append(number)

print("The steps needed were: ",steps)
'''
plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Graph')
plt.show()'''