
import random
from art import logo
from os import system, name
from time import sleep

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)
choice = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score(card_list):
    total = 0
    for ele in range(0, len(card_list)):
      total = total + card_list[ele]
    return total

def check(deck):
    if 11 in deck and score(deck)>21:
        for i in range(0, len(deck)):
              if deck[i] == 11 and score(deck)>21:
                  deck[i] = 1



def dealer(card_list):
  while score(card_list) < 17:
    new_c = random.choice(cards)
    card_list.append(new_c)


def play():
  a = random.choice(cards)
  b = random.choice(cards)

  c = random.choice(cards)
  d = random.choice(cards)

  computer = []
  player = []

  computer.append(a)
  computer.append(b)

  player.append(c)
  player.append(d)


  print(f"Your cards: {player}, current score: {score(player)}")
  print(f"Computer's first card: {a}")

  #print(computer)
  #print(player)

  def replay():
    #print("go")
    choice_b = input("Type 'yes' to get another card, 'no' to pass: ")
    if choice_b == 'yes':
      new_p = random.choice(cards)
      player.append(new_p)

      dealer(computer)
      check(computer)
      check(player)


      computer_score = score(computer)
      player_score = score(player)

      #print(computer)
      #print(player)

      if computer_score > player_score and computer_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Dealer wins!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif player_score > computer_score and player_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("You win!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif computer_score > 21 and player_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("You win!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif player_score > 21 and computer_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Dealer wins!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")

      elif player_score == computer_score:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Draw!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif player_score > 21 and computer_score > 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Draw!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")


    elif choice_b == 'no':
      dealer(computer)
      check(computer)
      check(player)


      computer_score = score(computer)
      player_score = score(player)

      #print(computer)
      #print(player)

      if computer_score > player_score and computer_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Dealer wins!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif player_score > computer_score and player_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("You win!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif computer_score > 21 and player_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("You win!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif player_score > 21 and computer_score <= 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Dealer wins!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")

      elif player_score == computer_score:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Draw!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")
      elif player_score > 21 and computer_score > 21:
        print(f"Your final hand: {player}, final score: {score(player)}")
        print(f"Computer's final hand: {computer}, final score: {score(computer)}")
        print("Draw!!")
        choice = input("Do you want to play again? Type 'yes' or 'no': ")
        if choice == 'yes':
          clear()
          print(logo)
          play()
        elif choice == 'no':
          print("Goodbye!!")

    else:
      print("incorrect input. please type again")
      replay()

  replay()


if choice == 'yes':
  play()
elif choice == 'no':
  print("Goodbye!!")
else:
  print("incorrect input. please type again")
