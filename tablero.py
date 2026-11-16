# Importando la librería pyxel
import pyxel
# Importando la clase Chef para poder usarla en la clase Tablero
from chef import Chef
# Importando la clase Ingrediente
from ingrediente import Ingrediente


class Tablero:
    """Esta clase contiene un tablero simple"""
    def __init__(self, width: int, height: int):
        """ Método que crea el tablero.
        :param width: El ancho del tablero
        :param height: El alto del tablero
        """
        # Asignando los atributos
        self.width = width
        self.height = height
        # El tablero contendrá dos Chefs
        self.chef = Chef(self.width // 2, self.height // 2)
        # El tablero contendrá una lista de ingredientes
        NAMES = ('chorizo', 'patata', 'cebolla', 'tomate', 'huevos')
        self.ingredientes = []
        for nombre in NAMES:
            ingr = Ingrediente(nombre)
            self.ingredientes.append(ingr)
        # En este init también necesitamos inicializar pyxel
        # Esta instrucción se usa para inicializar pyxel, ver la API para más
        # parámetros
        pyxel.init(self.width, self.height, title="Demo de juego Pyxel",
                   display_scale=4)
        # Cargando el archivo pyxres con las imágenes
        pyxel.load("assets/resources.pyxres")
        # Ejecutando el juego, esto llamará a los métodos update y draw en
        # cada frame, ver la API para más
        pyxel.run(self.update, self.draw)

    # Propiedades y setters
    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @width.setter
    def width(self, width: int):
        if not isinstance(width, int):
            raise TypeError("El ancho debe ser un entero")
        elif width < 1:
            raise ValueError("El ancho debe ser un entero positivo")
        else:
            self.__width = width

    @height.setter
    def height(self, height: int):
        if not isinstance(height, int):
            raise TypeError("El alto debe ser un entero")
        elif height < 1:
            raise ValueError("El alto debe ser un entero positivo")
        else:
            self.__height = height

    def update(self):
        """ Este es el método de pyxel que se ejecuta en cada iteración del
        juego (cada frame). Aquí hay que poner todo el código que debe
        ejecutarse en cada frame. Ahora contiene la lógica para salir del
        programa si se pulsa la tecla Q y para mover a los chefs."""
        # Para salir del juego
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        # Para mover al chef1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.chef.mover("izquierda", self)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.chef.mover("derecha", self)

    def draw(self):
        """Este es el método de pyxel que se ejecuta en cada iteración del
        juego (cada frame). Aquí hay que poner todo el código para dibujar
        los sprites del juego.
        """
        # Borrando la pantalla anterior
        pyxel.cls(0)
        # Dibujando al chef.
        # Los parámetros de pyxel.blt son (x, y, tupla_sprite)
        # El * se usa para desempaquetar la tupla del sprite
        pyxel.blt(self.chef.x, self.chef.y, *self.chef.imagen)
        # Un texto para mostrar la posición del chef, los parámetros de
        # pyxel.text son (x, y, texto, color)
        pyxel.text(10, 1, f"({self.chef.x}, {self.chef.y})", 7)
        # Dibujando los ingredientes
        y = 20
        x = 30
        for ingrediente in self.ingredientes:
            pyxel.blt(x, y, *ingrediente.imagen)
            x += 20
