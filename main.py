print ("Welcome to the Slot Machine Simulator!")
MAX_LINES = 3

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
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)
    
main()