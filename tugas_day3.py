# Program game menemukan harta karun
"""
RULES :
1. ada persimpangan jalan milih left atau right, kalau left lanjut ke level berikutnya kalo pilih right game over.
2. setelah milih left > kita harus ke sebuah pulau di tengah danau, pilih wait for a boad atau swim? jika pilih wait lanjut ke level
   berikutnya kalau pulih swim akan game over.
3. setelah pilih wait dan sampai di pulau, disana ada sebuah rumah yg mempunyai 3 pintu yaitu red, blue, yellow. 
    - jika memilih red (game over)
    - jika memilih blue (game over)
    - jika memilih yellow (kita akan menemukan harta karun nya)
"""

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

cross = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if cross == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    Lake = lake.lower()
    if Lake == "wait":
        house = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")  
        House = house.lower()
        if House == "red":
            print("It's a room full of fire. Game Over.")
        elif House == "blue":
            print("You enter a room of beasts. Game Over.")
        elif House == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door tha doesn't exist. Game over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over")



