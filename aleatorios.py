# Autor: Tomàs Lloret Martínez
# Data: 13/04/2025
# Pràctica 4: Generació de nombres aleatoris

# Generacion de números aleatorios usando la clase Aleat

class Aleat:
    """
    Clase generadora de números aleatorios usando el método LGC.

    Atributos:
    - m: modulo
    - a: multiplicador
    - c: incremento
    - x0: semilla inicial

    Métodos:
    - __init__(m, a, c, x0): Inicializa el generador con los valores de los atributos.
    - __next__(): Genera el siguiente número aleatorio.
    - __call__(seed): Reinicia la secuencia con la semilla que se pone en la variable seed.

    Pruebas unitarias:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**31, a=1103515245, c=7, x0=1212121):
        """
        Inicializa el generador con los valores de los atributos.

        - m: modulo c: incremento a: multiplicador x0: semilla inicial (por defecto, 1212121)
        - m y c no deben tener factores primos en común.
        - (a - 1) debe ser divisible por todos los factores primos de m (aunque no mucho).
        - Si m es divisible por 4, a - 1 también debe serlo, pero no por 8.
        """
        self.m = m
        self.a = a
        self.c = c
        self.x = x0 

    def __next__(self):
        """
        Genera el siguiente número aleatorio.
        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, seed):
        """
        Reinicia la secuencia con la semilla indicada.
        """
        self.x = seed


def aleat(*, m=2**31, a=1103515245, c=7, x0=1212121):
    """
    Función generadora de números aleatorios usando el método LGC.

    Argumentos:
    - m: módulo
    - a: multiplicador
    - c: incremento
    - x0: semilla inicial

    Salida:
    Se devuelve un generador que produce números aleatorios.
    Se puede reiniciar la secuencia usando el método send().

    Pruebas unitarias:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        # Recibe un nuevo valor de semilla si se usa aleat.send()
        new_seed = (yield x)
        if new_seed is not None:
            x = new_seed
        else:
            x = (a * x + c) % m

if __name__ == "__main__":
    import doctest
    doctest.testmod()