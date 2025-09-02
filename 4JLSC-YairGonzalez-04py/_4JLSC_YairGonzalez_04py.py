import math
##Ejemplo de creación de  Clase padre y clases hijas dentro de python 
#usando de ejemplos objetos Figuras geometricas
class FiguraGeometrica:
    def __init__(self):
        pass
    def descripcion(self):
        return "Soy una figura geometrica"
    def area(self):
        return 0

class Cuadrilatero(FiguraGeometrica):
    def __init__(self,base, altura):
        self.base = base
        self.altura =altura
    def descripcion(self):
        return "Cuadrilatero"
    def area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def __init__(self,base, altura):
        self.base = base
        self.altura =altura
    def descripcion(self):
        return "Triangulo"
    def area(self):
        return (self.base * self.altura)/2
class Circulo(FiguraGeometrica):
    def __init__(self,radio):#, altura):
        self.radio = radio
        #self.altura =altura
    def descripcion(self):
        return "Circulo"
    def area(self):
        return 3.1416 *(self.radio * self.radio)
        #return math.pi *(self.radio **2)
    ##return super().descripcion()

def main():
    print("Selecciona una figura geometrica")
    print("1. Cuadrilatero")
    print("2. Triangulo")
    print("3. Circulo")
    try:
        opcion=int(input("ingrese un valor del 1 al 3 : \n"))
    except ValueError:
        print("Ingrese un valor correcto")
        return
    if opcion == 1:
        try:
            base = float(input("Ingrese el valor de la base"))
            altura = float(input("Ingrese el valor de la altura"))
            figura =Cuadrilatero(base, altura)
        except ValueError:
            print("Ingrese valores correctos para el cuadrilatero")
            return
    elif opcion ==2:
        try:
            base =float(input("Ingrese el valor de la base"))
            altura =float(input("Ingrese el valor de la altura"))
            figura = Triangulo(base, altura)
            ##print("")
        except ValuError:
            print("Error: Ingrese valores correctos para el triangulo")
            return
    elif opcion ==3:
        try:
            radio = float(input("Ingrese el valor del radio"))
            figura = Circulo(radio)
        except ValuError:
            print("Error : Ingrese valores validos para el circulo")
            return
    else:
       print("Opción invalida")
       return
    print(figura.descripcion())
    print(f"EL area es:{figura.area():.2f}")
if __name__=="__main__":
    main()