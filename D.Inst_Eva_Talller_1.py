"""Construye dos superclases, donde una será la clase empleados que pida en consola el nombre del empleado en un método de instancia. 
La segunda clase será salario que pida en consola el salario del empleado en un método de instancia.
Cree una clase hija llamada Designación que herede las dos clases anteriores y que tenga un método de instancia que designe el cargo del empleado.
Verifique el código, instanciando un objeto de la clase hija, verificando si el objeto tiene el método nombre y salario."""

#Definimos las super clases y luego la clase hija

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def mostrar_informacion(self):
        print(f"El nombre completo del empleado es: {self.nombre}")

class Salario:
    def __init__(self, salariomensual):
        self.salariomensual = salariomensual
    
    def mostrar_informacionsalario(self):
        print(f"El salario mensual del empleado es: ${self.salariomensual}")


class Designacion(Empleado, Salario):
    def __init__(self, nombre, salariomensual, cargo):
        Empleado.__init__(self, nombre)
        Salario.__init__(self, salariomensual)
        self.cargo = cargo

    def mostrar_informacion_Designacion(self):
        self.mostrar_informacion()
        self.mostrar_informacionsalario()
        print(f"El cargo del empleado es: {self.cargo}")

# Se captura la información desde la consola
nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_empleado = float(input("Ingrese el salario mensual del empleado: "))
cargo_empleado = input("Ingrese el cargo que desempeña el empleado: ")

# Crear instancia de las clases derivadas
empleado = Designacion(nombre_empleado, salario_empleado, cargo_empleado)

# Mostrar información del empleado
print("\nInformación del empleado:")
empleado.mostrar_informacion_Designacion()
