"""
User    Computer    Result
Rock    Paper       Computer Wins
Rock    Scissors    Rock Win
Paper   Rock        Paper Wins
Paper   Scissors    Scissors Win
Scissor Paper       Scissors win
Scissor Rock        Rock win

computer_choice =
user_choice=
enter your choice=

you win

you lost.computer choose paper

you tied
"""
import random

ch=["rock","paper","scissors"]
computer_choice=random.choice(ch)
user_choice=input("Type rock,paper or scissors = ").lower()

if computer_choice=="Paper" and user_choice=="Rock":
    print("Computer Wins")
elif user_choice=="rock" and user_choice=="scissors":
    print("You Win")
elif user_choice=="Scissors" and user_choice=="Rock":
    print("Rock Wins")
elif user_choice=="Rock" and user_choice=="Paper":
    print("Paper Wins")    
elif user_choice==user_choice:
    print("Tie")
else:
    print("You lost! computer chose",computer_choice)      
      

import random

ch=["rock","paper","scissors"]
computer_choice=random.choice(ch)
user_choice=input("Type rock, paper or scissors = ").lower()

if user_choice!="rock" and user_choice!="paper" and user_choice!="scissors":
    print("Invalid")
elif user_choice=="rock" and computer_choice=="scissors":
    print("You win")
elif user_choice=="paper" and computer_choice=="rock":
    print("You win")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You win")
elif user_choice==computer_choice:
    print("Tie")
else:
    print("You lost. The computer chose",computer_choice)
