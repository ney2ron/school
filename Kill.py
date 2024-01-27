#-*- coding: cp1251 -*-

def hangman(word) :
    wrong = 0
    stages = ["",
              "________        ",
              "|      |        ",
              "|      O        ",
              "|     /|\\      ",
              "|     / \\      ",
              "|               ",
              ]
    
hangman = {"кот":"кто ловит мышей",
            "крот":"у кого жила дюймовочка под землей",
            "компьютер": "Вычислительная машина, но можной и поиграть",
            "крыса":"самый живучий обитатель канализации"}
import random
les = random.choice(list(hangman.keys()))
    rletters = list(les)

    board = ["__"] * len(les)
    win = False
    print("Добро пожаловать на казнь!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join (board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Вы выйграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))
  