class Livro:
    """
    Representa um livro do acervo da biblioteca.
    """

    def __init__(self, titulo, autor, isbn, ano):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._ano = ano
        self._disponivel = True  # todo livro começa disponível no acervo

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def ano(self):
        return self._ano

    @property
    def disponivel(self):
        # Só permite CONSULTAR se está disponível. Quem controla essa mudança
        # é a própria Biblioteca, através dos métodos abaixo.
        return self._disponivel

    def marcar_como_emprestado(self):
        self._disponivel = False

    def marcar_como_disponivel(self):
        self._disponivel = True

    def __eq__(self, other):
        # Dois livros são considerados o mesmo livro se o ISBN for igual.
        if not isinstance(other, Livro):
            return False
        return self._isbn == other._isbn

    def __str__(self):
        status = "disponível" if self._disponivel else "emprestado"
        return f"'{self._titulo}' - {self._autor} ({self._ano}) [{status}]"
