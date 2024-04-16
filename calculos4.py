class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):
        print("Valor actual:", self.valor)

    def sumar_dos(self):
        self.valor += 2

    def multiplicar_por_dos(self):
        self.valor *= 2

    def dividir_por_tres(self):
        self.valor /= 3


class OperacionDecorator:
    def __init__(self, numero):
        self.numero = numero

    def imprimir_valor(self):
        self.numero.imprimir_valor()

    def sumar_dos(self):
        self.numero.sumar_dos()
        self.imprimir_valor()

    def multiplicar_por_dos(self):
        self.numero.multiplicar_por_dos()
        self.imprimir_valor()

    def dividir_por_tres(self):
        self.numero.dividir_por_tres()
        self.imprimir_valor()


numero = Numero(5)

print("Valor original:")
numero.imprimir_valor()

print("\nRealizando operaciones con el decorador:")

decorador = OperacionDecorator(numero)
print("\nSumar 2:")
decorador.sumar_dos()

print("\nMultiplicar por 2:")
decorador.multiplicar_por_dos()

print("\nDividir por 3:")
decorador.dividir_por_tres()
