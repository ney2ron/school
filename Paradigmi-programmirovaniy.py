# -*- coding: cp1251 -*-


rock = []
country = []

def collect_songs():
    song = "������� �����."
    ask = "������� p (���) ��� � (������) . ������� X ��� ������: "
    
    while True:
        genre = input(ask)
        if genre == "X":
            break
        if genre == "p":
            rk = input(song)
            rock.append(rk)
            
        elif genre == ("�"):
            cy = input(song)
            country.append(cy)
        else:
            print("�������.")
    print(rock)
    print(country)
    
collect_songs()

        