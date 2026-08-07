class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem / 100)
        self.preco -= desconto

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def __str__(self):
        return f"Livro - {self.nome} ({self.autor}): R$ {self.preco:.2f}"


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem

    def __str__(self):
        return f"Eletrônico - {self.nome} ({self.voltagem}V): R$ {self.preco:.2f}"


if __name__ == "__main__":
    livro = Livro("Python Básico", 79.90, "Marcos Silva")
    eletronico = Eletronico("Fone de Ouvido", 199.90, 110)

    livro.aplicar_desconto(15)
    eletronico.aplicar_desconto(10)

    print(livro)
    print(eletronico)
