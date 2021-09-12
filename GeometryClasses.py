
class Circle:
    pi = 3.14

    def __init__(self,radius) -> None:
        self.radius = radius
    
    def get_area(self):
        return Circle.pi*self.radius**2



class triange:
    def __init__(self,length,height) -> None:
        self.length = length
        self.height = height
        
    def get_area(self):
        return 0.5 * self.length * self.height