import Libro
from Libro import Libro


class Copia: 
    def __init__(self, id_copia: str, libro: Libro, ubicacion: str):
        self.__id_copia: str = id_copia
        self.__libro: Libro = libro
        self.__ubicacion: str = ubicacion
        self.__estado: bool = True

    def get_estado(self) -> str:
        return self.__estado if "Disponible" else "Prestado"
    
    
        