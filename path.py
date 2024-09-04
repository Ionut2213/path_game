name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across: ").lower()

    if answer == "swim":
        print("You swim across and were eaten by an alligator. You lose!")
    
    elif answer == "walk":
        answer = input("You walked for many miles and find a cabin. Do you want to enter the cabin or keep walking? (enter/keep walking): ").lower()
        
        if answer == "enter":
            answer = input("Inside the cabin, you find a mysterious box. Do you want to open it or leave it? (open/leave): ").lower()

            if answer == "open":
                print("You open the box and find a map to a hidden treasure! You WIN!")
            elif answer == "leave":
                print("You decide to leave the box alone, but without it, you get lost in the woods. You lose!")
            else:
                print("Not a valid option. You lose.")

        elif answer == "keep walking":
            print("You keep walking, but eventually run out of water and get lost in the wilderness. You lose!")

        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back): ").lower()

    if answer == "back":
        print("You go back and lose the adventure. Try again next time!")
    
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them or ignore them? (talk/ignore): ").lower()

        if answer == "talk":
            answer = input("The stranger offers you a choice: a sword or a shield. Which do you choose? (sword/shield): ").lower()

            if answer == "sword":
                print("You take the sword and the stranger reveals themselves to be an enemy! You fight bravely and WIN!")
            elif answer == "shield":
                print("You take the shield, but the stranger attacks and you cannot defend yourself well. You lose!")
            else:
                print("Not a valid option. You lose.")

        elif answer == "ignore":
            print("You ignore the stranger and they turn out to be a wizard. Angered by your rudeness, they cast a spell and you lose!")

        else:
            print("Not a valid option. You lose.")
    
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name + ".")

