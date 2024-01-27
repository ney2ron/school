# -*- coding: cp1251 -*-


rock = []
country = []

def collect_songs():
    song = "Укажите песню."
    ask = "Введите p (рок) или к (кантри) . Введите X для выхода: "
    
    while True:
        genre = input(ask)
        if genre == "X":
            break
        if genre == "p":
            rk = input(song)
            rock.append(rk)
            
        elif genre == ("к"):
            cy = input(song)
            country.append(cy)
        else:
            print("Наверно.")
    print(rock)
    print(country)
    
collect_songs()

        