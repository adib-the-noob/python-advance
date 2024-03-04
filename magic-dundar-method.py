import math
from typing import Any 

class Vector:
    
    def __init__(self, x, y, angle = None):
        self.x = x 
        self.y = y
        self.angle = angle
        
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )
        
    def __repr__(self) -> str:
        return f"X is {self.x}, Y is {self.y}"
    
    def __len__(self):
        val = math.sqrt((self.x * self.x) + (self.y * self.y) + (2 * self.x * self.y * math.cos(self.angle if self.angle is not None else 0)) )
        return int(val)
    
    def __call__(self):
        print("I was called")
    
vector1 = Vector(x=23, y=13, angle=45)
vector2 = Vector(x=50, y=29)

vector_final = vector1 + vector2

print(vector_final)
print(len(vector_final))
vector_final()