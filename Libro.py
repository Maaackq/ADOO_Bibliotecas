from types import  list,  Optional

class Libro:
    def __init__(self, isbn: str, titulo: str, autores: str):
        self.__isbn: str = isbn
        self.__titulo: str = titulo
        self.__autores: str = autores 
        self.__copias: list[Copia] = []
    
    def agregar_copia(id_copia: str, self, ubicacion: str)-> Copia:
        copia = Copias(id_copia, self, ubicacion)
        self.__copias.append(copia)
        return copia




    