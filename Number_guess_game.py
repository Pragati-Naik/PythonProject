"""
secret number

guess number from 1-10=5

Hurray! you guessed it right
Oh NO!, You guessed wrong. Number was 3

"""

import random

secret_number=random.randint(1,10)

user_num=int(input("Guess a number from 1-10 = "))

if user_num==secret_number:
    print("You guessed right")
else:
    print(f"You guessed wrong. The number was {secret_number}")

"""
import random

secret_num= random.randint(1,10)
number=int(input("Guess a number from 1-10: "))
if number>=1 and number<=20:
    print("Hurray! you guessed it right")
else:
    print(f"Oh NO!, You guessed wrong. Number was {secret_num}")    

"""




# print("You Win!")
# elif random_num!=user:
    # print("Sorry You Lose!")