class Vector:
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )
        
vector1 = Vector(x=23, y=13)
vector2 = Vector(x=50, y=29)

vector_final = vector1 + vector2

print(f"Value of x is {vector_final.x}")
print(f"Value of x is {vector_final.y}")