#random lib
import random


print(">>>>>>>>>>>>>ROCK-PAPER-SCISSORS GAME<<<<<<<<<<<<<<<<")

options=("rock","paper","scissors")


while True:
    #random choice of computer
  computer= random.choice(options)
  player=input("Enter your choice(rock,paper,scissors):").lower()

  #Display the choices
  print(f"Player choice:{player}\n")
  print(f"Computer choice:{computer}\n")

  #Determining the winner
  if player=="rock" and computer=="scissors":
        print("Rock smashes the scissors!! Player wins")
  elif player=="rock" and computer=="rock":
        print("It is a tie!!!!")
  elif player=="paper" and computer=="rock":
        print("Paper wraps the rock !!! Player wins")
  elif player=="paper" and computer=="paper":
        print("It is a tie!!!!")
  elif player=="scissors" and computer=="paper":
        print("Scissors cuts the paper!! Player wins")
  elif player=="scissors" and computer=="scissors":
        print("It is a tie!!!!")

  else:
        print("Computer wins")
  choice=input("Do you want to play again(yes/no):").lower()
  if(choice!="yes" and choice!="y"):
    print("Game Over")
    break

print("Thank you for playing!!!!")

