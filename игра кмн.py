import random


def play_game():
    options = ["камень", "ножницы", "бумага"]
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player_choice = input("Ваш ход (камень/ножницы/бумага): ").strip().lower()

        if player_choice not in options:
            print("Некорректный выбор. Попробуйте снова.")
            continue

        computer_choice = random.choice(options)
        print(f"Компьютер выбрал: {computer_choice}")

        if player_choice == computer_choice:
            print("Ничья!")
        elif (
                (player_choice == "камень" and computer_choice == "ножницы") or
                (player_choice == "ножницы" and computer_choice == "бумага") or
                (player_choice == "бумага" and computer_choice == "камень")
        ):
            print("Вы выиграли раунд!")
            player_score += 1
        else:
            print("Вы проиграли раунд!")
            computer_score += 1

        print(f"Счёт: Игрок {player_score} : Компьютер {computer_score}")

    winner = "Игрок" if player_score > computer_score else "Компьютер"
    print(f"{winner} победил!")


play_again = True
while play_again:
    play_game()
    replay = input("Хотите сыграть снова? (да/нет): ")
    play_again = replay.lower() == "да"

print("Спасибо за игру!")
