import random 
def game():
  print("Welcome to Coin Flip Game")
  while True:
    print("Dashboard \n1. Play Game \n2.About Game \n3. Quit")
    reply = int(input(">> "))
    if reply == 1:
      play()
    elif reply == 2:
      print("""\Coin Flip Game is game that allows you to choose  
                if the possible outcome is head or tail
            """)
    elif reply == 3:
      print("Exiting App")
      break
    else:
      print ("invalid input")
  

def play():
  user= str(input("Enter choice 'h' for head while 't' for tail: ")).lower()
  output = random.choice(['h', 't'])
  computer = output
  if user == computer:
     print  ("You Won !")
  if user != computer:
    print("You Lost !")
  return user 


game()