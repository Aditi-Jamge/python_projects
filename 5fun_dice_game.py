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
game_over = False

while True:
    for player in range(players):
        current_score = 0
        print(f"\nplayer number {player + 1}")
        print(f"score = {current_score}")
        while True:
            user = input("\nDo you want roll a dice? (Y/N): ").lower()

            if user != "y":
                print("Okay! :)")
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled {value}")
                print(f"Your current score = {current_score}")

                if current_score >= win_score:
                    print(f"Congratulations! Winner player is {player + 1}.")
                    game_over = True
                    break

        print(f"Your final score is {current_score}.")
        if game_over:
            break

    if game_over:
        break
      
            
      

       

           
        
    

            
































