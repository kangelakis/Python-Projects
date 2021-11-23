print ("Please enter the price of the product as well as the discount..")
price = float(input("Price = "))
discount = int(input("Discount = "))

while (price<0):
    print ("Invalid price, try again..")
    price = float(input("Price = "))

while (discount<0 or discount>price):
    print ("Invalid discount value, try again..")
    discount = int(input("Discount = "))

#Η δεκαδική έκπτωση
fdisc = discount/100

#Το τελικό ποσό
total = price - price*fdisc

#Το ποσό της έκπτωσης
discvalue = total - price

print("The price off is:", discvalue)
print("The final value is:", total)

input("Press any button to continue...")