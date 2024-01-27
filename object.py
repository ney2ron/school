#-*- coding: cp1251

class Apple ():
    """ Описание яблок """
    def __init__(self, weith, color):
        self.weith = weith
        self.color = color
        
    def days_of_collecting (self, days):
        self.days = days
        
    def taste_fruit (self, fruit):
        self.fruit = fruit
        
Fruct = Apple(25,"зеленое")
print("Класс яблоко: ")
print(Fruct.weith,"Граммов")
print(Fruct.color)
Fruct.days_of_collecting(6)
print(Fruct.days,":" ,"дней назад было собрано")
Fruct.taste_fruit("Сладкое")
print(Fruct.fruit)