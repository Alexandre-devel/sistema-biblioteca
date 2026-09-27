from pessoa import Pessoa

LIMITE_LIVROS_EMPRESTADOS = 3


class Usuario(Pessoa):
    """
    Representa um usuário que pode pegar livros emprestados na biblioteca.
    """

    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self._matricula = matricula
        self._livros_emprestados = []

    @property
    def matricula(self):
        return self._matricula

    @property
    def livros_emprestados(self):
        # Retorna uma cópia da lista, para que ninguém altere a lista original por fora.
        return list(self._livros_emprestados)

    def pode_pegar_emprestado(self):
        return len(self._livros_emprestados) < LIMITE_LIVROS_EMPRESTADOS

    def adicionar_livro(self, livro):
        self._livros_emprestados.append(livro)

    def remover_livro(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)

    def apresentar(self):
        return f"Usuário: {self._nome} (matrícula {self._matricula})"
