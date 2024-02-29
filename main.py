import random, time

comp_turn = ['k', 'n', 'b']
count = [0, 0]


def knb_choice(turn):
    if turn == "k":
        print("камень")
    elif turn == "n":
        print("ножницы")
    elif turn == "b":
        print("бумага")

def main():
    gameloop = True
    while gameloop:

        turn = input("k - камень, n - ножницы, b - бумага, exit - выход\n")
        print()
        time.sleep(0.5)

        if turn == "exit":
            print("выход")
            gameloop = False
        else:
            knb_choice(turn)
            c_turn = random.choice(comp_turn)
            knb_choice(c_turn)
            if turn == 'k' and c_turn == 'n' or turn == 'n' and c_turn == 'b' or turn == 'b' and c_turn == 'k':
                print('Ты выиграл')
                count[0] += 1

            if turn == 'n' and c_turn == 'k' or turn == 'b' and c_turn == 'n' or turn == 'k' and c_turn == 'b':
                print('Я выиграл')
                count[1] += 1
        print('Счет - ', count[0], ':', count[1])
        if count[0] == 10 or count[1] == 10:
            gameloop = False


if __name__ == "__main__":
    main()

