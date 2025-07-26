import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

REELS = 3 #column
LINES = 3 #rows

symbols_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbols_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2   
}

def check_winnings(grid,lines,bet,value):
    winnings = 0
    for line in range(lines):
        symbol = grid[0][line]
        for reel in grid:
            symbol_check = reel[line]
            if symbol != symbol_check:
                break
        else:
            winnings += value[symbol] * bet
                
    return winnings

def get_slot_machine_grid(reels,lines,symbols):
    all_symbols = []
    for symbol,count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    grid = []
    for _ in range(reels):
        reel = []
        current_symbols = all_symbols[:]
        for _ in range(lines):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            reel.append(value)
        grid.append(reel)
    return grid

def print_slot_machine(grid):
    for line in range(len(grid[0])):
        for i,reel in enumerate(grid):
            if i != len(grid) - 1:
                print(f"{reel[line]}",end = "|")
            else:
                print(f"{reel[line]}",end = "")
        print()

def insert_money():
    while True:
        try:
            total_balance = int(input("How much would you like to insert money? Rs"))
            if total_balance >= 50:
                break
            else:
                print("Minimum insert amount is Rs50.")
        except ValueError:
            print("Invalid Input! Please enter a amount.")
    
    return total_balance

def get_no_of_lines():
    while True:
        try:
            lines = int(input(f"Enter the line number to bet on 1-{MAX_LINES}? "))
            if 1<= lines <=3:
                break
            else:
                print("Please enter valid line number.")
        except:
            print("Invalid Input! Please enter correct line number!")
    
    return lines

def get_bet():
    while True:
        try:
            bet_amount = int(input("What would you like to bet on the line? "))
            if MIN_BET<= bet_amount <=MAX_BET:
                break
            else:
                print(f"Amount must be between Rs{MIN_BET}-Rs{MAX_BET}.")
        except:
            print("Invalid Input! Please enter valid amount!")

    return bet_amount

def game(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You do not have enough amount.")
            continue
        else:
            break
    print(f"you are betting Rs{bet} on the {lines} line.\nTotal bet amount = {total_bet}\n")

    slots = get_slot_machine_grid(REELS,LINES,symbols_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots,lines,bet,symbols_value)
    print(f"You won Rs{winnings}")
    print("---------------------")

    return winnings - total_bet

def main():
    balance = insert_money()
    while True:
        print(f"\nCurrent balance = Rs{balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += game(balance)

    print(f"You left with Rs{balance}.")
    print("--------------------------")

main()

