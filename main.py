import random 
def play():
  print("Welcome to Coin Flip Game \nYou get to choose if the possible outcome is head or tail")
  user= str(input("Enter choice h for head while t for tail: ")).lower()
  computer = random.choice(["h", "t"])

  
  return user 
