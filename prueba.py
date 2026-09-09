class MiPrueba:
    def __init__(self,codigo:int):
        self.__codigo=codigo
        self.atributopublico=1

    def ObtenerCodigo(self) -> int:
        return self.__codigo

    # def __str__(self) -> str:
    #     return f"MiPrueba con codigo {self.__codigo}"

if __name__ == "__main__":
    variableprueba = MiPrueba(111)
    print (variableprueba)

