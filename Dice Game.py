import random

#Player scores
player_1_score = 0
player_2_score = 0

for i in range (10):
#Generate the numbers
    player_1_value = random.randint(1,6)
    player_2_value = random.randint(1,6)

#Display the numbers
    print("Player 1 rolled:", player_1_value)
    print("player 2 rolled:", player_2_value)

#Updating the scores
    if player_1_value > player_2_value:
        print("PLAYER 1 WINS")
        player_1_score = player_1_score + 1

    elif player_2_value > player_1_value:
        print("PLAYER 2 WINS")
        player_2_score = player_2_score + 1

    else:
        print("Its a draw")

    input ("Press enter to continue")

print("###Game Over!###")
print("Player_1 score:", player_1_score)
print("Player_2 score:", player_2_score)
