class LivroIndisponivelException(Exception):
    """Levantada quando alguém tenta pegar emprestado um livro que já está emprestado."""

    def __init__(self, titulo_livro):
        self.titulo_livro = titulo_livro
        super().__init__(f"O livro '{titulo_livro}' não está disponível no momento.")


class LivroNaoEncontradoException(Exception):
    """Levantada quando o livro não é encontrado no acervo da biblioteca."""

    def __init__(self, referencia):
        self.referencia = referencia
        super().__init__(f"Nenhum livro encontrado com a referência '{referencia}'.")


class UsuarioNaoEncontradoException(Exception):
    """Levantada quando o usuário não é encontrado no sistema."""

    def __init__(self, matricula):
        self.matricula = matricula
        super().__init__(f"Nenhum usuário encontrado com a matrícula '{matricula}'.")


class LimiteEmprestimosExcedidoException(Exception):
    """Levantada quando um usuário tenta pegar mais livros do que o permitido."""

    def __init__(self, nome_usuario, limite):
        self.nome_usuario = nome_usuario
        self.limite = limite
        super().__init__(
            f"O usuário '{nome_usuario}' já atingiu o limite de {limite} livros emprestados."
        )
