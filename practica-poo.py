#crea una clase llamada Producto
#nombre, unidades y precio
#creas un producto camisa, 10, 9.95 de precio
#muestra el nombre de producto por consola

#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

#práctica de sobreescritura.
#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Producto:
    def __init__(self, nombre, unidades, precio):  # propiedades de instancia:cambia para cada instancia
        self.nombre = nombre
        self.unidades = unidades
        self.precio = precio

    def infoProducto(self):
        print(f'El producto es {self.nombre}, hay {self.unidades} unidades a un precio de {self.precio}')

class Servicio:
    def consultarDetalle(self):
        print("El servicio es básico")

class Estandar(Servicio):
    def consultarDetalle(self):
        print("El servicio es estándar")

class Premium(Servicio):
    def consultarDetalle(self):
        print("El servicio es premiumm")

product1=Producto('camisa',10,9.95)

print(product1.nombre)
product1.infoProducto()
servicioP=Premium()
servicioE=Estandar()


input=input("Dime el servicio: ")
if input == "premium":
    print(servicioP.consultarDetalle())
if input == "estandar":
    print(servicioE.consultarDetalle())
else:
    print("El servicio es básico")