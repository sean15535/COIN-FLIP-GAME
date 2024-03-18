import random 

def play():
  user= str(input("Enter choice 'h' for head while 't' for tail: ")).lower()
  output = random.choice(['h', 't'])
  computer = output
  guess_limit = 3 
  if user == computer:
     print  ("You Won !")
  if user != computer:
    print("You Lost !")
  return user 

def about():
    print("""\Coin Flip Game is game that allows you to choose  
                if the possible outcome is head or tail
            """)

def exit():
    print("Exiting App")
