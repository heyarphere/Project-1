# My code
import random
'''
1 for snake
0 for gun
-1 for water
'''
computer = random.choice([-1, 0, -1])
userstr = input("Enter your choice: ")
userDict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "water", 0: "Gun"}

user = userDict[userstr]


print(f"user chose {reversedict[user]}\nComputer chose {reversedict[computer]}")

# condition 
if (computer == user):
    print("It's Draw!")

else:
    if(computer ==-1 and user ==1):
        print("You wiin!")

    elif(computer ==-1 and user ==0):
        print("You lose!")

    elif(computer ==1 and user ==-1):
        print("You lose!")

    elif(computer ==1 and user ==0):
        print("You Win!")

    elif(computer ==0 and user ==-1):
        print("You win!")

    elif(computer ==0 and user ==1):
        print("You lose!")

    else:
        print("Something went wrong!")                             



# chatgpt code
import random

'''
1 for snake
-1 for water
0 for gun
'''

youDict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
if youstr not in youDict:
    print("Invalid input! Please choose 's', 'w', or 'g'.")
    exit()

you = youDict[youstr]
computer = random.choice([-1, 0, 1])

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

# Win rules: your_choice beats this computer_choice
win_map = {
    1: -1,  # Snake drinks Water
    -1: 0,  # Water damages Gun
    0: 1    # Gun kills Snake
}

if computer == you:
    print("It's a draw.")
elif win_map[you] == computer:
    print("You Win!")
else:
    print("You Lose!")
