class Repartidor:
    __VALORKM = 500
    __VALORKMEXTRA = 100

    def __init__(self, nombre:str, edad:int):
        if not isinstance(nombre,str):
            raise TypeError("error: nombre debe ser string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Error: nombre es obligatorio")
        if not isinstance(edad, int):
            raise TypeError("Error: edad debe ser entero")
        if edad < 18:
            raise ValueError("Error: debe ser mayor de edad")
        self.__nombre = nombre
        self.__edad = edad
        self.__cobros = []
        self.__pedidosEntregados = 0

    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerEdad(self)->int:
        return self.__edad

    def obtenerPedidosEntregados(self)->int:
        return self.__pedidosEntregados

    def obtenerRecaudacion(self)->float:
        return sum(self.__cobros)

    def hacerViaje(self, km:float, propina:float = 0):
        if not isinstance(km, (int, float)):
            raise TypeError("Error: km debe ser numero")
        if km < 0:
            raise ValueError("Error: el km debe ser mayor o igual a cero")
        if not isinstance(propina, (int, float)):
            raise TypeError("Error: propina debe ser numero")
        if propina < 0:
            raise ValueError("Error: propina debe ser mayor o igual a cero")
        self.__cobros.append(self.calcularViaje(km, propina))
        self.__pedidosEntregados += 1

    def calcularViaje(self, km:float, propina:float = 0)->bool:
        if not isinstance(km, (int, float)):
            raise TypeError("Error: km debe ser numero")
        if km < 0:
            raise ValueError("Error: el km debe ser mayor o igual a cero")
        if not isinstance(propina, (int, float)):
            raise TypeError("Error: propina debe ser numero")
        if propina < 0:
            raise ValueError("Error: propina debe ser mayor o igual a cero")
        dinero = 0
        if km <= 3:
            dinero = Repartidor.__VALORKM * km + propina
        else:
            dinero = Repartidor.__VALORKM * km + (km - 3 ) * Repartidor.__VALORKMEXTRA + propina
        return dinero

    def __str__(self):
        return (
            f"Nombre: {self.__nombre} \n"
            f"Edad: {self.__edad}\n"
            f"Cantidad de viajes {self.__pedidosEntregados}\n"
            f"Cobros: {self.__cobros}"
        )

class Test:
    @staticmethod
    def run():
        try:
            print("-"*50)
            print("Test de Repartidor")
            print("-"*50)
            repartidor1 = Repartidor("Nicolas", 29)
            print(repartidor1)
            print(repartidor1.obtenerNombre())
            print(repartidor1.obtenerEdad())
            print("-"*50)
            print("hacer viaje de 3km")
            print(f"Calculo de viaje 3km ${repartidor1.calcularViaje(3):.2f}")
            repartidor1.hacerViaje(3)
            print("-"*50)
            print("Estado interno")
            print(repartidor1)
            print("hacer viaje de 4km + propina 123")
            print(f"Calculo de viaje 4km + propina ${repartidor1.calcularViaje(4,123):.2f}")
            repartidor1.hacerViaje(4,123)
            print("-"*50)
            print("Estado interno")
            print(repartidor1)
            print(f"RECAUDACION: ${repartidor1.obtenerRecaudacion():.2f}")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
if __name__ == "__main__":
    Test.run()