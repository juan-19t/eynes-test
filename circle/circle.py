import math

class Circle():
    def __init__(self,radius):
        try:
            if radius <= 0:
                raise ValueError ('El valor ingresado no puede ser igual o menor a 0')
        except ValueError as e:
            print("Ocurrió un error:",e)
        self.radius=radius


    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        try:
            if radius <= 0:
                raise ValueError("El valor ingresado debe ser mayor que 0 para que sea modificado con éxito")
            self.radius = radius
        except ValueError as e:
            print("Ocurrió un error:",e)
        return f"El radio tiene un nuevo valor de {self.radius}"

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area
    
    def get_perimeter(self):
        # la variable 'd' hace referencia al diametro
        d = self.radius*2
        return math.pi * d
    
    def __mul__(self, n):
       try: 
            if n <= 0:
                raise ValueError ("El radio se debe multiplicar por un numero mayor a 0")
            return Circle(self.radius * n)
       except ValueError as e:
           print(e)
    
    def __str__(self):
        if self.radius > 0:
            return f"Círculo de radio {self.radius}"
        else:
            return ""