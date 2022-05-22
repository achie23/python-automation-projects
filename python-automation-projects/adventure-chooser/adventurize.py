name = input("Enter your name: ")
print("Welcome", name, "to My Adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You've come to a river, you can walk around it or wim accross. Type walk to walk around it or swim to swim accross: ").lower()
    
    if answer == "swim":
        print("You swam accross and were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked for several miles, ran out of drinking water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
    
elif answer == "right":
    answer = input("You've come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    
    if answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you want to talk to her (yes/no)? ").lower()
        
        if answer == "yes":
            print("Great job! You talked to the keeper of the treasure and she gave you gold. You WIN!")
        elif answer == "no":
            print("You ignored the keeper of the treasure and you got nothing. You LOSE!")
        else:
            print("Not a valid option. You lose.")
        
    elif answer == "back":
        print("You went back to the main road. You lose!")
    else:
        print("Not a valid option. You lose.")
    
else:
    print("Not a valid option. You lose.")
    
print("Thank you", name, "for trying")