from functions import play, about, exit

def game():
  print("Welcome to Coin Flip Game")
  while True:
    print("Dashboard \n1. Play Game \n2.About Game \n3. Quit")
    reply = int(input(">> "))
    if reply == 1:
      play()
    elif reply == 2:
      about()
    elif reply == 3:
      exit()
      break
    else:
      print ("invalid input")
  
game()