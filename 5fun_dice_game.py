import random

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    try:
        players = int(input("Enter number of players(2 to 4): "))
        if 2 <= players <= 4:
            break 
        else:
            print("Please enter players between 2 to 4")               
    except ValueError:
        print("Invalid Input")

win_score = 20
players_score = [0 for _ in range(players)]
game_over = False

while True:
    for player in range(players):
        print(f"\nplayer number {player + 1}")
        print(f"score = {players_score[player]}")
        current_score = 0
        while True:
            user = input("\nDo you want roll a dice? (Y/N): ").lower()

            if user != "y":
                print("Okay! :)")
                break

            elif user == "y":
                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn over.")
                    current_score = 0
                    break
                else:
                    current_score += value
                    players_score[player] += value
                    print(f"You rolled {value}")
                    print(f"Your current score = {current_score}")

                    if players_score[player] >= win_score:
                        final_score = players_score[player]
                        print(f"Congratulations! Winner player is {player + 1}")
                        game_over = True
                        break

            else:
                print("Type Yes/No")
                continue

        print(f"Your final score is {players_score[player]}.")
        if game_over:
            break

    if game_over:
        break
      
            
      

       

           
        
    

            
































