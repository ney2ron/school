""" 
    ������� ��������������� ������ 
    � ��� ������ float � ���������� 
    ���������.���������� ��������� 
    ���������� ����� ����������� 
    ��������� ����������.

"""

def star (string) :
    try:
        return float (string)
    except ValueError :
        print("Could not star")
        
c = star (55.0)
print(c)