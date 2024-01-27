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
    
hangman = {"���":"��� ����� �����",
            "����":"� ���� ���� ���������� ��� ������",
            "���������": "�������������� ������, �� ������ � ��������",
            "�����":"����� ������� ��������� �����������"}
import random
les = random.choice(list(hangman.keys()))
    rletters = list(les)

    board = ["__"] * len(les)
    win = False
    print("����� ���������� �� �����!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "������� �����: "
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
            print("�� ��������! ���� �������� �����: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("�� ���������! ���� �������� �����: {}.".format(word))
  