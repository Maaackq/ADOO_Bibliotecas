from types import  list,  Optional

class Libro:
    def __init__(self, isbn: str, titulo: str, autores: str):
        self.__isbn: str = isbn
        self.__titulo: str = titulo
        self.__autores: str = autores 
        self.__copias: list[Copia] = []
    
    @property
    def isbn(self) -> str:
        return self.__isbn
    @property
    def titulo(self) -> str:
        return self.__titulo
    @property
    def autores(self) -> str:
        return self.__autores
    @property
    def copias(self) -> list['Copia']:
        return self.__copias

    
    def agregar_copia(id_copia: str, self, ubicacion: str)-> Copia:
        copia = Copias(id_copia, self, ubicacion)
        self.__copias.append(copia)
        return copia

    def obtener_disponibles(self) -> list[Copia]:
        return self.__copias
    




    