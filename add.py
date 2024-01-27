#-*- coding: cp1251 -*-
class Clock:
    __DAY = 86400 #����� ������ � ����� ���
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("������� ������ ���� ����� ������")
        self.seconds = seconds % self.__DAY
        
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds //60) % 60
        h = (self.seconds // 3600) % 24 
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")
    def __add__(self, other):
        return Clock(self.seconds + other)
    
c1 = Clock(1000)
#c1.seconds = c1.seconds +100
c1 = c1 + 100
print(c1.get_time())
