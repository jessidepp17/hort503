# Text game called "Save the Princess!"

from sys import exit

# gold room fxn
def gold_room():
   print("Great! You've entered the castle.")
   print("There's a chest and a locked door in the room.")

   choice = input("> ")
   if "open chest" in choice:
      print("There's a shitload of gold and a key inside! You take the key, but will you take the gold?")
   elif "ignore chest" in choice:
      dead("You stumble around the room until you starve.")
   # need to change so that any number can be entered
   choice = input("> ")
   if "yes" in choice:
      print("Good idea! You might need the money later.")
      print("Use the key to open the massive door in front of you.")
      choice = input("> ")
      if "open door" in choice:
         print("You're in!")
         boss_battle()
      else:
         print("Whaaaaaat...")
   elif "no" in choice:
      print("If you say so...")
      print("Use the key to open the massive door in front of you.")
      choice = input("> ")
      if "open door" in choice:
         print("You're in!")
         boss_battle()
      else:
         print("Whaaaaaat...")
   else:
      dead("You stumble around the room until you starve.")

def boss_battle():
   print("Oh no, the door has locked behind you!")
   print("There's a crazy huge dragon in the room!")
   print("You must slay the dragon to save the princess!")
   print("Wait... did you pick up that gold?")
   choice = input("> ")
   if "yes" in choice:
       print("Maybe you can try to make a trade: the gold for the princess.")
   else "no" in choice:
       print("Well... you have no choice by to slay the dragon. GO!!!")

       choice = input("> ")
       if "slay dragon" in choice:
       print("Hooray, you saved the princess, but you're still broke! YOU WIN!")
   else:
       dead("You suck.")

def dead(why):
   print(why, "GAME OVER")
   exit(0)

def start():
   print("The princess has been taken deep into the castle by a huge dragon!")
   print("You must save the princess before it's too late!")
   print("What will you do?")

   choice = input("> ")

   if "run away" in choice:
     dead("You ran home to your mommy. Shame, Shame.")
   elif "enter castle" in choice:
      gold_room()
   else:
      print("Whaaaaaat...")

# call start() to begin game
start()
