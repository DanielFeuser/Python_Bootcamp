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
print("You’ve landed on a mysterious island. Your mission is to find the hidden treasure,but beware—one wrong decision could end your adventure!")
choice1 = input("left or right?")
if choice1 =="left":
    choice2=input("After walking for some time, you reach the edge of a lake. In the middle of the lake, you see a small island with something shiny on it.\nSwim or Wait?").lower()
    if choice2 =="wait":
        choice3 =input("You choose to wait patiently. After a few minutes, a small boat appears, drifting calmly toward you. "
                       "\nYou get on the boat and sail safely to the island."
                       "\nOn the island, you find three doors: one red, one blue, and one yellow.Each door leads to a different fate.\nWhich colour do you choose?").lower()
        if choice3 =="red":
            print("As soon as you open the red door, flames engulf the entire area, burning everything in sight.\nGame Over.")
        elif choice3=="blue":
            print("You open the blue door and are immediately attacked by wild beasts lurking inside.\nGame Over.")
        elif choice3 =="yellow":
            print("You open the yellow door and find a glittering chest of gold and jewels! Congratulations, you’ve found the treasure!\nYou Win!")
        else:
            print("You choose the wrong door, you die.\nGame Over.")
else:
    print("You take the path to the right, but suddenly the ground beneath your feet gives way. You fall into a deep hole, never to be seen again.\nGame Over.")
