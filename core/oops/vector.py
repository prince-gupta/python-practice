class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector((self.a + other.a), (self.b + other.b));

    def __str__(self):
        return "Vector (%f, %f) " % (self.a, self.b)


vector1 = Vector(12.2, 12.3)
vector2 = Vector(14.2, 13.4)

resultant_vector = vector1 + vector2

print(resultant_vector)
