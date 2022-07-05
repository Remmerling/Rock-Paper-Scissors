from random import randint

Computer = randint(1,3)
Player = input()

if (Computer == 1): print ("rock")
if (Computer ==2): print ("paper")
if (Computer == 3): print ("scissors")
    
if (Computer == 1 and Player == "paper"): print ("Player wins!")  
if (Computer == 1 and Player == "rock"): print ("Tie")
if (Computer == 1 and Player == "scissors"): print ("Computer Wins! You suck")
if (Computer == 2 and Player == "rock"): print ("Computer Wins! You are even worse than the last guy")
if (Computer == 2 and Player == "paper"): print ("Tie!")
if (Computer == 2 and Player == "scissors"): print ("Player wins! An L for Tech everywhere")
if (Computer == 3 and Player == "rock"): print ("Player wins!")
if (Computer == 3 and Player == "paper"): print ("Computer Wins!") 
if (Computer == 3 and Player == "scissors"): print ("Tie!")
