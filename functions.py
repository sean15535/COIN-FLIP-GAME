import random 

def play():
    guess_limit = 3 
    while guess_limit > 0 :
        user = str(input("Enter choice 'h' for head while 't' for tail: ")).lower()
        output = random.choice(['h', 't'])
        computer = output
        if user == computer:
            print(f"The coin flipped on {computer}. You Won!")
            return
        else:
            guess_limit -= 1
            print(f"The coin flipped on {computer}. You Lost! You have {guess_limit} guesses left.")
    print("Chances exceeded. Game Over")

def about():
    print("This is a simple coin flip game. You can guess whether the coin will land on heads or tails.")

def exit():
    print("Exiting App")
