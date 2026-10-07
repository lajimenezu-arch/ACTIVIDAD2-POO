from enum import Enum, auto


class TipoPlaneta(Enum):
    GASEOSO = auto()
    TERRESTRE = auto()
    ENANO = auto()


class Planeta:
    """Clase que representa un cuerpo celeste tipo Planeta.

    Constantes de clase
    -------------------
    LIMITE_EXTERIOR_UA : float
        Distancia en km que delimita el cinturón de asteroides (~3.4 UA).
    """

    LIMITE_EXTERIOR_KM: float = 149_597_870 * 3.4

    def __init__(
        self,
        nombre: str,
        cantidad_satelites: int,
        masa: float,
        volumen: float,
        diametro: int,
        distancia_sol: int,
        tipo: TipoPlaneta,
        es_observable: bool,
    ) -> None:
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def calcular_densidad(self) -> float:
        """Calcula la densidad media del planeta ($\rho = m / V$).

        Returns
        -------
        float
            Densidad calculada.
        Raises
        ------
        ZeroDivisionError
            Si el volumen ingresado es menor o igual a cero.
        """
        if self.volumen <= 0:
            raise ZeroDivisionError(
                "El volumen debe ser mayor a 0 para calcular la densidad."
            )
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        """Determina si se considera un planeta exterior al cinturón de asteroides."""
        return self.distancia_sol > self.LIMITE_EXTERIOR_KM

    def imprimir(self) -> None:
        """Muestra en pantalla las propiedades físicas del planeta."""
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa} kg")
        print(f"Volumen del planeta = {self.volumen} km³")
        print(f"Diámetro del planeta = {self.diametro} km")
        print(f"Distancia al sol = {self.distancia_sol} km")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")


if __name__ == "__main__":
    p1 = Planeta(
        "Tierra",
        1,
        5.9736e24,
        1.08321e12,
        12742,
        150_000_000,
        TipoPlaneta.TERRESTRE,
        True,
    )
    p1.imprimir()
    print(f"Densidad = {p1.calcular_densidad():.4e} kg/km³")
    print(f"Es planeta exterior = {p1.es_planeta_exterior()}\n")

    p2 = Planeta(
        "Júpiter",
        79,
        1.899e27,
        1.4313e15,
        139820,
        750_000_000,
        TipoPlaneta.GASEOSO,
        True,
    )
    p2.imprimir()
    print(f"Densidad = {p2.calcular_densidad():.4e} kg/km³")
    print(f"Es planeta exterior = {p2.es_planeta_exterior()}")
