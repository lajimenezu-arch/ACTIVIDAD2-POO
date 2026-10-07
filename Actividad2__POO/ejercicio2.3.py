from enum import Enum, auto


class TipoCombustible(Enum):
    GASOLINA = auto()
    BIOETANOL = auto()
    DIESEL = auto()
    BIODIESEL = auto()
    GAS_NATURAL = auto()


class TipoAutomovil(Enum):
    CIUDAD = auto()
    SUBCOMPACTO = auto()
    COMPACTO = auto()
    FAMILIAR = auto()
    EJECUTIVO = auto()
    SUV = auto()


class Automovil:
    """Modela el comportamiento y propiedades cinemáticas de un vehículo automotor."""

    def __init__(
        self,
        marca: str,
        modelo: int,
        motor: float,
        tipo_combustible: TipoCombustible,
        tipo_automovil: TipoAutomovil,
        numero_puertas: int,
        cantidad_asientos: int,
        velocidad_maxima: float,
        color: str,
        velocidad_actual: float = 0.0,
    ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self._velocidad_actual = 0.0
        self.velocidad_actual = velocidad_actual  # Usa el setter con validación

    @property
    def velocidad_actual(self) -> float:
        return self._velocidad_actual

    @velocidad_actual.setter
    def velocidad_actual(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("La velocidad no puede ser negativa.")
        if valor > self.velocidad_maxima:
            raise ValueError(
                f"La velocidad excede la velocidad máxima permitida ({self.velocidad_maxima} km/h)."
            )
        self._velocidad_actual = valor

    def acelerar(self, incremento: float) -> None:
        """Incrementa la velocidad verificando los límites del vehículo."""
        if incremento < 0:
            raise ValueError("El incremento de aceleración debe ser positivo.")
        self.velocidad_actual = min(
            self._velocidad_actual + incremento, self.velocidad_maxima
        )

    def desacelerar(self, decremento: float) -> None:
        """Reduce la velocidad actual asegurando que no descienda de cero."""
        if decremento < 0:
            raise ValueError("El decremento debe ser positivo.")
        self.velocidad_actual = max(self._velocidad_actual - decremento, 0.0)

    def frenar(self) -> None:
        """Detiene completamente el vehículo."""
        self._velocidad_actual = 0.0

    def calcular_tiempo_llegada(self, distancia: float) -> float:
        """Calcula el tiempo estimado ($t = d / v$).

        Returns
        -------
        float
            Tiempo en horas.
        """
        if self._velocidad_actual == 0:
            raise ZeroDivisionError(
                "El vehículo está detenido. Imposible calcular tiempo de llegada."
            )
        return distancia / self._velocidad_actual

    def imprimir(self) -> None:
        """Muestra el estado completo del automóvil."""
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor} L")
        print(f"Tipo de combustible = {self.tipo_combustible.name}")
        print(f"Tipo de automóvil = {self.tipo_automovil.name}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima} km/h")
        print(f"Color = {self.color}")
        print(f"Velocidad actual = {self._velocidad_actual} km/h\n")


if __name__ == "__main__":
    auto = Automovil(
        "Ford",
        2018,
        3.0,
        TipoCombustible.DIESEL,
        TipoAutomovil.EJECUTIVO,
        5,
        6,
        250.0,
        "Negro",
    )
    auto.imprimir()
    auto.velocidad_actual = 100.0
    print(f"Velocidad actual = {auto.velocidad_actual} km/h")
    auto.acelerar(20.0)
    print(f"Velocidad tras acelerar = {auto.velocidad_actual} km/h")
    auto.desacelerar(50.0)
    print(f"Velocidad tras desacelerar = {auto.velocidad_actual} km/h")
    auto.frenar()
    print(f"Velocidad tras frenar = {auto.velocidad_actual} km/h")
