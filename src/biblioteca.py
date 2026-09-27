from excecoes import (
    LivroIndisponivelException,
    LivroNaoEncontradoException,
    UsuarioNaoEncontradoException,
    LimiteEmprestimosExcedidoException,
)
from emprestimo import Emprestimo
from decoradores import avisar_operacao


class Biblioteca:
    """
    Classe responsável por gerenciar o acervo de livros, os usuários
    cadastrados e os empréstimos feitos. Ninguém deve mexer diretamente
    nas listas internas por fora dessa classe (encapsulamento).
    """

    def __init__(self, nome):
        self.nome = nome
        self._acervo = []       # lista de objetos Livro
        self._usuarios = []     # lista de objetos Usuario
        self._emprestimos = []  # lista de objetos Emprestimo

    # ---------- Cadastro ----------

    def cadastrar_livro(self, livro):
        self._acervo.append(livro)

    def cadastrar_usuario(self, usuario):
        self._usuarios.append(usuario)

    # ---------- Buscas ----------

    def buscar_livro_por_isbn(self, isbn):
        for livro in self._acervo:
            if livro.isbn == isbn:
                return livro
        raise LivroNaoEncontradoException(isbn)

    def buscar_livro_por_titulo(self, titulo):
        encontrados = [livro for livro in self._acervo if titulo.lower() in livro.titulo.lower()]
        return encontrados

    def buscar_usuario_por_matricula(self, matricula):
        for usuario in self._usuarios:
            if usuario.matricula == matricula:
                return usuario
        raise UsuarioNaoEncontradoException(matricula)

    # ---------- Empréstimo e devolução ----------

    @avisar_operacao
    def emprestar_livro(self, matricula_usuario, isbn_livro):
        usuario = self.buscar_usuario_por_matricula(matricula_usuario)
        livro = self.buscar_livro_por_isbn(isbn_livro)

        if not livro.disponivel:
            raise LivroIndisponivelException(livro.titulo)

        if not usuario.pode_pegar_emprestado():
            raise LimiteEmprestimosExcedidoException(usuario.nome, 3)

        livro.marcar_como_emprestado()
        usuario.adicionar_livro(livro)

        emprestimo = Emprestimo(livro, usuario)
        self._emprestimos.append(emprestimo)
        return emprestimo

    @avisar_operacao
    def devolver_livro(self, matricula_usuario, isbn_livro):
        usuario = self.buscar_usuario_por_matricula(matricula_usuario)
        livro = self.buscar_livro_por_isbn(isbn_livro)

        emprestimo = self._encontrar_emprestimo_em_aberto(usuario, livro)
        emprestimo.registrar_devolucao()

        livro.marcar_como_disponivel()
        usuario.remover_livro(livro)

        return emprestimo

    def _encontrar_emprestimo_em_aberto(self, usuario, livro):
        for emprestimo in self._emprestimos:
            if (
                emprestimo.usuario == usuario
                and emprestimo.livro == livro
                and emprestimo.data_devolucao is None
            ):
                return emprestimo
        raise LivroNaoEncontradoException(
            f"empréstimo em aberto de '{livro.titulo}' para {usuario.nome}"
        )

    # ---------- Recursos extras de POO ----------

    def __iter__(self):
        # Permite fazer: for livro in biblioteca:
        return iter(self._acervo)

    def __len__(self):
        return len(self._acervo)

    def __str__(self):
        return f"Biblioteca '{self.nome}' com {len(self._acervo)} livro(s) no acervo."
