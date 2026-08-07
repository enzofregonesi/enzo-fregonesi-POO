class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Veículo: {self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} - {self.qtd_portas} portas"


if __name__ == "__main__":
    meu_carro = Carro("Toyota", "Corolla", 4)
    print(meu_carro)
