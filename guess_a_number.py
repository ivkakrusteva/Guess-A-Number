import random

random_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100):")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(player_input)

    if player_number == random_number:
        print(f"You guess it! The number is indeed {random_number}")
        break
    elif player_number > random_number:
        print("Too High!")
        print(f'Guess number is: {random_number}')
    else:
        print("Too Low!")
        print(f'Guess number is: {random_number}')




