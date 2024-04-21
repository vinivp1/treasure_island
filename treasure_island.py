from art import map, beast, treasure, hole, crocodile, fire

print(map)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
option1 = input("You are at a cross road in the forest. Where do you want to go? Type left or right\n").lower()

if (option1 == "left"):
  option2 = (input("You have come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across\n")).lower()
  if(option2 == "wait"):
    option3 = (input("You came to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Wich color do you choose?\n")).lower()
    if(option3 == "red"):
      print("You got burned by fire. Game over")
      print(fire)
    elif(option3 =="blue"):
      print("You got eaten by wild beasts. Game Over.")
      print(beast)
    elif(option3 == "yellow"):
      print("You found the treasure. You win!")
      print(treasure)
    else:
      print("This door doesn't exist. Game Over!")
  else:
    print("You got attacked by an angry alligator. Game over!")
    print(crocodile)
else:
  print("You fell into a hole. Game Over!")
  print(hole)