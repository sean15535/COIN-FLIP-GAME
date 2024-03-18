import random 

def play():
  guess_limit = 3 
  guess = 0
  while guess > guess_limit :
     user= str(input("Enter choice 'h' for head while 't' for tail: ")).lower()
     output = random.choice(['h', 't'])
     computer = output
     if user == computer:
        print(f"The coin fliped on{computer}You Won !")
     if user != computer:
        print(f"The coin fliped on{computer} You Lost !")
     guess +=1
  return "Guess Limit Exceeded , Try again"

def about():
    print("This is a simple coin flip game. You can guess whether the coin will land on heads or tails.")

def exit():
    print("Exiting App")
