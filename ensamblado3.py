from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):
    @abstractmethod
    def operacion(self) -> str:
        pass

class Pieza(Componente):
    def operacion(self) -> str:
        return "Pieza"

class Subconjunto(Componente):
    def __init__(self, nombre: str, piezas: List[Componente] = None) -> None:
        self.nombre = nombre
        self.piezas = piezas or []

    def agregar(self, componente: Componente) -> None:
        self.piezas.append(componente)

    def quitar(self, componente: Componente) -> None:
        self.piezas.remove(componente)

    def operacion(self) -> str:
        resultado = [f"Subconjunto {self.nombre} con:"]
        for pieza in self.piezas:
            resultado.append(pieza.operacion())
        return "\n".join(resultado)

class Ensamblado(Componente):
    def __init__(self, nombre: str, componentes: List[Componente] = None) -> None:
        self.nombre = nombre
        self.componentes = componentes or []

    def agregar(self, componente: Componente) -> None:
        self.componentes.append(componente)

    def quitar(self, componente: Componente) -> None:
        self.componentes.remove(componente)

    def operacion(self) -> str:
        resultado = [f"Ensamblado {self.nombre} con:"]
        for componente in self.componentes:
            resultado.append(componente.operacion())
        return "\n".join(resultado)

if __name__ == "__main__":
    ensamblado_principal = Ensamblado("Ensamblado Principal", [
        Subconjunto("Subconjunto 1", [Pieza() for _ in range(4)]),
        Subconjunto("Subconjunto 2", [Pieza() for _ in range(4)]),
        Subconjunto("Subconjunto 3", [Pieza() for _ in range(4)])
    ])

    print(ensamblado_principal.operacion())
    print("\nAgregando un subconjunto opcional adicional...\n")

    subconjunto_opcional_1 = Subconjunto("Subconjunto Opcional 1", [Pieza() for _ in range(4)])
    subconjunto_opcional_2 = Subconjunto("Subconjunto Opcional 2", [Pieza() for _ in range(4)])

    ensamblado_principal.agregar(subconjunto_opcional_1)
    ensamblado_principal.agregar(subconjunto_opcional_2)

    print(ensamblado_principal.operacion())
