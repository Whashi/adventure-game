print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You start at a fork in the path. Which way would you like to go?")
direction = input("Left or Right: ")
if direction == "left" or direction == "Left":
    print("You next come across a lake and it looks pretty big. Do you try to swim across or wait for a boat?")
    lake = input("Swim or Wait: ")
    if lake == "wait" or lake == "Wait":
        print('''A boat eventually comes along and ferries you across the lake. 
        On the shore you come across a mysterious looking house. 
        You decide to enter and immediately see three different doors. A red one, a yellow one and a blue one. 
        Which door do you enter?
              ''')
        door = input("Red, Yellow or Blue: ")
        if door == "yellow" or door == "Yellow":
            print("YOU FOUND THE TREASURE!!! "
                  "How astute of you to realize that the yellow door had gold.")
            print("You win!")
        elif door == "red" or door == "Red":
            print("There is a raging fire behind this door. You are engulfed in flames! "
                  "How did you not feel the heat...")
            print("Game over")
        elif door == "blue" or door == "Blue":
            print("There are ravenous beasts behind this door and they tear you to shreds. "
                  "If you had been listening you would have heard them barking..")
            print("Game over")
        else:
            print("That wasn't one of the choices sorry")
            print("Game over")
    elif lake == "swim" or lake == "Swim":
        print("You are attacked by killer trout.")
        print("Game over")
    else:
        print("That wasn't one of the choices sorry")
        print("Game over")
elif direction == "right" or direction == "Right":
    print("You fall into a hole and die of embarrassment.")
    print("Game over")
else:
    print("That wasn't one of the choices sorry")
    print("Game over")