class Hexagon:
    def __init__(self, l, u="6"):
        self.ugol = u
        self.len = l
        
    def calculate_perimeter(self):
        r = (self.len * (3**3))/2
        self.radius = r
        s = (3*(3**2)/2)*(self.len**2)
        self.square = s
        p = self.ugol*self.len
        self.perimeter = p
        print("Perimetr: "+str(self.perimeter)+"; Radius: "+str(self.radius)+"; Square: "+str(self.square))
        
hexogon = Hexagon(2)
print(hexogon.calculate_perimeter())
        