""" 
    Функция преобразовывает строку 
    в тип данных float и возвращает 
    результат.Использует обработку 
    исключений чтобы перехватить 
    возможные исключения.

"""

def star (string) :
    try:
        return float (string)
    except ValueError :
        print("Could not star")
        
c = star (55.0)
print(c)