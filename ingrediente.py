class Ingrediente:
    """ Esta clase contiene un ingrediente. Tiene un nombre y una
    imagen. La imagen es un atributo de solo lectura que depende del nombre.
    En el futuro la imagen dependerá también del estado del ingrediente:
    troceado, cocinado, etc. """
    def __init__(self, nombre: str):
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        NAMES = ('chorizo', 'patata', 'cebolla', 'tomate', 'huevos')
        if not isinstance(value, str):
            raise TypeError("El nombre del ingrediente debe ser un str")
        elif value.lower() not in NAMES:
            raise ValueError("Los nombres válidos son " + str(NAMES))
        else:
            self.__nombre = value.lower()

    @property
    def imagen(self) -> tuple:
        # Usamos un diccionario para asociar el nombre del ingrediente con su
        # imagen.
        IMAGES_RAW = {
            "chorizo": (0, 48, 16, 16, 16),
            "patata": (0, 16, 16, 16, 16),
            "cebolla": (0, 32, 16, 16, 16),
            "tomate": (0, 0, 16, 16, 16),
            "huevos": (0, 64, 16, 16, 16),
        }
        return IMAGES_RAW[self.nombre]
