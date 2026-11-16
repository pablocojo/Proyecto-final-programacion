"""
Autor: Angel Garcia Olaya. PLG. UC3M
Desde: 2026-10-21
Versión: 1.2
"""


class Chef:
    """ Una versión de la clase Chef para el proyecto final.
    Contiene propiedades, setters, un método mover.
    El sprite del chef es un atributo de solo lectura que depende de su
    posición, que es un atributo privado. """
    def __init__(self, x: int, y: int, ):
        """ Método init de la clase
        :param x: la x del chef
        :param y: la y del chef
        :param pos: la posición del chef: ("arriba", "abajo")
        """
        self.x = x
        self.y = y
        # Al principio no tiene plato y no está actuando
        self.tiene_plato = False

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def imagen(self) -> tuple:
        """ La imagen será un atributo de solo lectura, que dependerá
         inicialmente de la POSICIÓN. En Pyxel la imagen es una tupla con las
         coordenadas de la imagen en el banco de imágenes. La tupla es
         (banco_imagen, x_inicial, y_inicial, tamaño_horizontal,
         tamaño_vertical)
        """
        result = (0, 0, 0, 16, 16)

        return result

    @property
    def tiene_plato(self) -> bool:
        return self.__tiene_plato

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("La posición x debe ser un int")
        elif x < 0:
            raise ValueError("La x no puede ser negativa")
        else:
            self.__x = x

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("La posición y debe ser un int")
        elif y < 0:
            raise ValueError("La y no puede ser negativa")
        else:
            self.__y = y

    @tiene_plato.setter
    def tiene_plato(self, dish: bool):
        if not isinstance(dish, bool):
            raise TypeError("El atributo tiene_plato debe ser bool")
        else:
            self.__tiene_plato = dish

    # Notar que no podemos poner el tipo de board como Tablero ya que eso
    # requeriría importar Tablero y tendríamos un import circular, por lo que
    # indicamos el tipo usando "Tablero"
    def mover(self, direccion: str, board: "Tablero"):
        """
        Este es un ejemplo de cómo mover al chef. No se consideran obstáculos
        en el tablero.
        :param direccion: un string que puede ser 'izquierda', 'derecha',
         'arriba' o 'abajo'
        :param board: el Tablero, podríamos haber recibido sus tamaños
         vertical y horizontal, pero como en el futuro, para mover,
         necesitaremos considerar otros componentes del tablero es mejor
         recibir el tablero completo como parámetro
        """
        DIRECCIONES = ("izquierda", "derecha")
        board_x_size = board.width
        # Comprobando el tipo y valor de los parámetros, no podemos comprobar
        # el tipo de board ya que es un import circular
        if not isinstance(direccion, str):
            raise TypeError("La dirección debe ser un string")
        elif direccion.lower() not in DIRECCIONES:
            raise ValueError("La dirección debe estar en " + str(DIRECCIONES))
        # Convertimos la dirección a minúsculas para evitar problemas con las
        # mayúsculas
        direccion = direccion.lower()
        # La posición (0, 0) del chef es la esquina superior izquierda del
        # sprite. Podemos mover al chef a la derecha si la coordenada x más a
        # la derecha del chef es menor que el tamaño del tablero. Será la
        # coordenada x del chef más el ancho del sprite. El ancho del sprite
        # es el 4º elemento de la tupla imagen.
        if direccion == "derecha" and self.x + self.imagen[3] < board_x_size:
            self.x += 1
