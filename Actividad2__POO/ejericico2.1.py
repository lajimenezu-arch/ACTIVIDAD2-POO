class Persona:
    """Representa a una persona dentro del sistema.

    Attributes
    ----------
    nombre : str
        Nombre principal de la persona.
    apellidos : str
        Apellidos completos de la persona.
    numero_documento_identidad : str
        Documento único de identificación.
    ano_nacimiento : int
        Año de nacimiento (YYYY).
    """

    def __init__(
        self,
        nombre: str,
        apellidos: str,
        numero_documento_identidad: str,
        ano_nacimiento: int,
    ) -> None:
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.ano_nacimiento = ano_nacimiento

    def imprimir(self) -> None:
        """Muestra en consola la información general de la persona."""
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(
            f"Número de documento de identidad = {self.numero_documento_identidad}"
        )
        print(f"Año de nacimiento = {self.ano_nacimiento}\n")


if __name__ == "__main__":
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)

    p1.imprimir()
    p2.imprimir()
