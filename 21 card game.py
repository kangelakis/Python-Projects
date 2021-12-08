import random
import time
import os

def drawCards(hand,i):
    print (f"P{i}'s turn!")
    global n
    hand=[]
    n = 0
    while True and n <= 10:
        print ("Your hand: ", hand)
        choice = input(f"Pull a card.. (Y/n)? [{n+1}/10]: ")
        while (choice != 'y' and choice != 'Y' and choice !='N' and choice != 'n'):
            choice = input(f"Invalid option try again.. [{n+1}/10]: ")
        if (choice == 'Y' or choice =='y'):
            hand.append(deck[n])
            n += 1
        else:
            break
    print (f"End of P{i}'s turn!")
    time.sleep(2)
    return hand


def addCards(players,i):
    cardsum = 0
    l=len(players)
    for j in range (l):
        if (players[j][0] == "K" or players[j][0] == "Q" or players[j][0] == "J"):
            cardsum += 10
        else:
            cardsum += int(players[j][0])
    if cardsum > 21:
        print(f"Sum is {cardsum} > 21. P{i+1} eliminated")
    else:
        return cardsum

    

sums=[]
players=[]
deck=[]
colors=['♥','♠','♣','♦']
fig=['K','Q','J']
cards=[i for i in range(1,11)]

for i in (cards+fig):
    for j in colors:
        deck.append([i,j])

#UI friendly chatter to help user
print("Deck of cards: ", deck)
time.sleep(3)
os.system('cls')
print("Let the games begin!")
time.sleep(1.5)
print ("Shuffling...")
time.sleep(4)
random.shuffle(deck)

#Selection of max players
number = int(input("Select the number of players(1-4): "))
while number>4 or number <1:
    number = int(input("Invalid option select again..: "))

#These two loops work on giving each player his own hand
for i in range (number):
    players.append(f"P{i+1}")
    print(players[i], "joined the game!")
    time.sleep(.2)
print("#############################################")
time.sleep(.7)
for i in range (number):
    players[i] = drawCards(players[i],i+1)
    deck = deck[n:] #This command removes the cards picked by players from the deck
    print("#############################################")


for i in range(number):
    sums.append(addCards(players[i],i))
for i in range(number):
    print(f"P{i+1}'s total sum: {sums[i]}")
print (sums)





input("Press any key to continue..")




#todo list:
'''
-Maybe make it so the addCards function gets called in the drawCards for a simpler and easier interface

'''