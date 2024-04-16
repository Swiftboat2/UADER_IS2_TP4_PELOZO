from abc import ABC, abstractmethod


class LaminaDeAcero(ABC):
    def __init__(self, tren_laminador):
        self._tren_laminador = tren_laminador

    @abstractmethod
    def producir_lamina(self):
        pass


class LaminaDeAcero05(LaminaDeAcero):
    def producir_lamina(self):
        return f"Lámina de acero de 0.5'' producida en tren laminador de {self._tren_laminador} mts."


class TrenLaminador(ABC):
    @abstractmethod
    def producir(self):
        pass


class TrenLaminador5(TrenLaminador):
    def producir(self):
        return "Generando planchas de 5 mts."

class TrenLaminador10(TrenLaminador):
    def producir(self):
        return "Generando planchas de 10 mts."


if __name__ == "__main__":
    
    tren_5 = TrenLaminador5()
    tren_10 = TrenLaminador10()

    
    lamina_05_tren_5 = LaminaDeAcero05(tren_5.producir())
    lamina_05_tren_10 = LaminaDeAcero05(tren_10.producir())

  
    print(lamina_05_tren_5.producir_lamina())
    print(lamina_05_tren_10.producir_lamina())
