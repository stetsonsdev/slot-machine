
import random

MAX_LINES = 3
MAX_BET= 100
MIN_BET = 1
def deposit():
    while True:
        amount = (input("Enter the amount you want to deposit: $"))
        if amount.isdigit(): 
            amount = int(amount) 
            if amount > 0:
                break
            else:
                print("Invalid input. Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount
def get_number_of_lines():
    while True:
        lines = (input("Enter the number of lines you want to play (1-" + str(MAX_LINES) + "): "))
        if lines.isdigit(): 
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Invalid input. Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines
def get_bet():
    while True:
        bet = (input("Enter the amount you want to bet on each line: (between $" + str(MIN_BET) + " and $" + str(MAX_BET) + "): $"))
        if bet.isdigit(): 
            bet = int(bet) 
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Invalid input. Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"Insufficient funds. Please deposit more money. Your current balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines for a total bet of ${total_bet}.")


print ("Welcome to the Slot Machine Simulator!")    
main()
