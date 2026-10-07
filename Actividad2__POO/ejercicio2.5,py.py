import math


class Circulo:
    """Clase geométrica que modela un Círculo a partir de su radio.

    Attributes
    ----------
    radio : float
        Radio del círculo (debe ser mayor o igual a cero).
    """

    def __init__(self, radio: float) -> None:
        self._radio = 0.0
        self.radio = radio  # Invoca el setter con validación

    @property
    def radio(self) -> float:
        """float: Devuelve el radio del círculo."""
        return self._radio

    @radio.setter
    def radio(self, valor: float) -> None:
        """Establece el radio validando que no sea negativo."""
        if valor < 0:
            raise ValueError("El radio no puede ser un número negativo.")
        self._radio = float(valor)

    def calcular_area(self) -> float:
        r"""Calcula el área del círculo: $A = \pi \cdot r^2$."""
        return math.pi * math.pow(self._radio, 2)

    def calcular_perimetro(self) -> float:
        r"""Calcula el perímetro o longitud de la circunferencia: $P = 2 \cdot \pi \cdot r$."""
        return 2 * math.pi * self._radio

    def imprimir(self) -> None:
        """Muestra en consola las propiedades y cálculos del círculo."""
        print(f"Radio del círculo = {self._radio}")
        print(f"Área del círculo = {self.calcular_area():.4f}")
        print(f"Perímetro del círculo = {self.calcular_perimetro():.4f}\n")


if __name__ == "__main__":
    circulo = Circulo(2.0)
    circulo.imprimir()
