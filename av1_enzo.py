# Classe Base: Funcionario
class Funcionario:

    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base  # Atributo privado

    # Getter para o salario_base
    def get_salario_base(self):
        return self.__salario_base

    # Setter para o salario_base com validação
    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario

    # Método de cálculo que será sobrescrito
    def calcular_salario_final(self):
        return self.__salario_base


# Subclasse: Gerente
class Gerente(Funcionario):

    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    # Sobrescrita do método calcular_salario_final
    def calcular_salario_final(self):
        return self.get_salario_base() + self.bonus_gestao


# Subclasse: Desenvolvedor
class Desenvolvedor(Funcionario):

    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    # Sobrescrita do método calcular_salario_final
    def calcular_salario_final(self):
        salario_base = self.get_salario_base()
        if self.nivel == "Senior":
            return salario_base + 1500.00
        return salario_base


# ==========================================
# TESTES E EXECUÇÃO DO SISTEMA
# ==========================================
if __name__ == "__main__":
    print("=== TESTE DE ENCAPSULAMENTO E HERANÇA - TECHCORP ===\n")

    # 1. Instanciando 1 Gerente
    gerente = Gerente(
        nome="Carlos Silva",
        matricula="G101",
        salario_base=8000.00,
        bonus_gestao=2000.00,
    )

    # 2. Instanciando 1 Desenvolvedor Senior
    dev_senior = Desenvolvedor(
        nome="Ana Souza", matricula="D202", salario_base=6000.00, nivel="Senior"
    )

    # 3. Teste de proteção de atributo privado
    print("--- Teste de Alteração Direta do Salário Base ---")
    print(
        f"Salário Base Original da Ana (Getter): R$ {dev_senior.get_salario_base():.2f}"
    )

    # Tentativa incorreta de alteração direta (não afeta o atributo encapsulado real)
    dev_senior.__salario_base = -100

    print(
        f"Tentativa de alteração direta com valor negativo: dev_senior.__salario_base = -100"
    )
    print(
        f"Salário Base após tentativa (Getter): R$ {dev_senior.get_salario_base():.2f}"
    )
    print(
        "-> O valor privado do salário base permaneceu protegido!\n"
    )

    # 4. Exibição dos resultados no terminal
    print("--- Folha de Pagamento ---")
    print(
        f"Funcionario: {gerente.nome} | Cargo: Gerente | Salário Final: R$ {gerente.calcular_salario_final():.2f}"
    )
    print(
        f"Funcionario: {dev_senior.nome} | Cargo: Dev {dev_senior.nivel} | Salário Final: R$ {dev_senior.calcular_salario_final():.2f}"
    )