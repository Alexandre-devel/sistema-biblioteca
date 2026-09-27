from datetime import date, timedelta

DIAS_PARA_DEVOLUCAO = 14


class Emprestimo:
    """
    Representa a relação entre um usuário e um livro emprestado.
    """

    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = date.today()
        self.data_prevista_devolucao = self.data_emprestimo + timedelta(days=DIAS_PARA_DEVOLUCAO)
        self.data_devolucao = None  # só é preenchida quando o livro é devolvido

    def registrar_devolucao(self):
        self.data_devolucao = date.today()

    def esta_atrasado(self):
        if self.data_devolucao is not None:
            return self.data_devolucao > self.data_prevista_devolucao
        return date.today() > self.data_prevista_devolucao

    def __str__(self):
        situacao = "devolvido" if self.data_devolucao else "em aberto"
        return (
            f"Empréstimo de '{self.livro.titulo}' para {self.usuario.nome} "
            f"({situacao}, previsto para {self.data_prevista_devolucao})"
        )
