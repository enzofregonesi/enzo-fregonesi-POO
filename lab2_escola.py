class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_perfil(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}"


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina

    def exibir_perfil(self):
        perfil = super().exibir_perfil()
        return f"{perfil}\nDisciplina: {self.disciplina}"


class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula

    def exibir_perfil(self):
        perfil = super().exibir_perfil()
        return f"{perfil}\nMatrícula: {self.matricula}"


if __name__ == "__main__":
    professor = Professor("Ana Silva", "123.456.789-00", "ana.silva@escola.com", "Matemática")
    aluno = Aluno("Bruno Souza", "987.654.321-00", "bruno.souza@escola.com", "2024001")

    print("Perfil do Professor:")
    print(professor.exibir_perfil())
    print("\nPerfil do Aluno:")
    print(aluno.exibir_perfil())
