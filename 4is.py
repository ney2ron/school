#-*- coding: cp1251 -*-
class Song:
    def __init__(self):
        self.name = "���� ����"
        
treck = Song()
music = treck
print(treck is music)

albom = Song()
print(treck is albom)