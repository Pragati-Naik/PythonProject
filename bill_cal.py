"""
Bill Calculator

enter your bill amount

Above 50000
"""
Amount=int(input("Enter amount = "))

if Amount>50000:
    # print("You got 40% discount")
    discount=40
elif Amount>=40000 and Amount<=50000:
    # print("You got 30% discount")
    discount=30
elif Amount>=20000 and Amount<=40000:
    # print("You got 20% discount")
    discount=20  
elif Amount<20000:
    print("No discount") 
else:
    discount=0    
print(f"Your final bill is Rs.{Amount}")         



