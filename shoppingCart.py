item = input("What item would you like to buy?")
price = float(input("What is the price?"))
quantity = int(input("How much quantity do you need: "))

total = price * quantity

print(f"Your have bought {quantity} x {item}")
print(f"Your price is: Rs{round(total,2)}")