from enum import Enum, auto


class TipoCuenta(Enum):
    AHORROS = auto()
    CORRIENTE = auto()


class CuentaBancaria:
    """Gestión de balance contable y operaciones esenciales sobre una cuenta bancaria."""

    def __init__(
        self,
        nombres_titular: str,
        apellidos_titular: str,
        numero_cuenta: int,
        tipo_cuenta: TipoCuenta,
    ) -> None:
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self._saldo: float = 0.0

    @property
    def saldo(self) -> float:
        return self._saldo

    def consultar_saldo(self) -> None:
        """Muestra el saldo actual disponible."""
        print(f"El saldo actual es: ${self._saldo:,.2f}")

    def consignar(self, valor: float) -> bool:
        """Deposita una suma a la cuenta.

        Parameters
        ----------
        valor : float
            Monto a ingresar (debe ser estricto positivo).
        """
        if valor <= 0:
            print("Error: El monto a consignar debe ser mayor a cero.")
            return False

        self._saldo += valor
        print(
            f"Consignación exitosa de ${valor:,.2f}. Nuevo saldo: ${self._saldo:,.2f}"
        )
        return True

    def retirar(self, valor: float) -> bool:
        """Débito de fondos sujeto a liquidez disponible."""
        if valor <= 0:
            print("Error: El valor a retirar debe ser mayor a cero.")
            return False
        if valor > self._saldo:
            print("Error: Fondos insuficientes para realizar la transacción.")
            return False

        self._saldo -= valor
        print(
            f"Retiro exitoso de ${valor:,.2f}. Nuevo saldo: ${self._saldo:,.2f}"
        )
        return True

    def imprimir(self) -> None:
        """Muestra el estado financiero básico del cuentahabiente."""
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.name}")
        print(f"Saldo = ${self._saldo:,.2f}\n")


if __name__ == "__main__":
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200_000)
    cuenta.consignar(300_000)
    cuenta.retirar(150_000)
