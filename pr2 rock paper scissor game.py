# Roc Paper Scissor Game

import random

hand1 = {
    "rock": """
        ___
    ---'   ___)
          (_____)
          (____)
          (___)
    ---._(___)
    """,
    "paper": """
        ___
    ---'   _)_____
              _____)
              _____)
             _____)
    ---.____)
    """,
    "scissor": """
        ___
    ---'   __)
            ______)
           ______)
          (__)
    ---._(__)
    """,
}
hand2 = {
    "rock": """
         ___
    (___   '---
    (____)
    (____)
     (___)
      (___)__.---
    """,
    "paper": """
         ___
    (_____ '---
    (_____     
     (_____     
      (_____    
       (_____.---
    """,
    "scissor": """
         ___
    (_____'---
    (_____      
        (__   
          (__)  
           (_)__.---
    """,
}

print(f"{'Rock':<{10}} {'Paper':<{10}} {'Scissor':<{12}} {'Game':<{12}}")

print("-" * 40)

list = ["rock", "paper", "scissor"]

print("\nEnter :-\n1. rock.\n2. paper.\n3. scissor.")

n = 1

m = 10

computer = 0

player = 0

while n < m:

    b = input("\nEnter :").lower()

    a = random.choice(list)

    if b in list:

        if b in a:
            print(f"\nComputer :-{hand1[a]} \nUser :-{hand2[b]}\nYou drawed its {a}")

        else:

            p = False

            if b in "rock" and a in "paper":
                p = True

            elif b in "scissor" and a in "rock":
                p = True

            elif b in "paper" and a in "scissor":
                p = True

            if p:
                print(f"\nComputer :-{hand1[a]} \nUser :-{hand2[b]}\nYou lost its {a} ")
                computer += 1

            else:
                print(f"\nComputer :-{hand1[a]} \nUser :-{hand2[b]}\nYou won its {a} ")
                player += 1
    else:
        print("\nInvalid input. Please enter rock paper or scissor")
        m += 1
    n += 1

if n == 10:
    if computer > player:
        print(f"\nThe computer won the match by {computer} points.")
    elif computer == player:
        print("\nThe match is draw")
    else:
        print(f"\nCongratulations you won by {player} points")

print(f"\n{'MATCH OVERVIEW':>{21}}")

print(f"\n{'Players':<{15}} {'Points':<{15}}")

print("-" * 30)

print(f"{'Computer':<{15}}  {computer:<{15}}")

print(f"\n{'YOU':<{15}}  {player:<{15}}")
