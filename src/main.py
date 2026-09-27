from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario
from bibliotecario import Bibliotecario
from excecoes import (
    LivroIndisponivelException,
    LivroNaoEncontradoException,
    UsuarioNaoEncontradoException,
    LimiteEmprestimosExcedidoException,
)


def main():
    biblioteca = Biblioteca("Biblioteca Municipal")

    # Cadastrando livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis", "111", 1899)
    livro2 = Livro("O Estrangeiro", "Albert Camus", "222", 1942)
    livro3 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "333", 1881)

    biblioteca.cadastrar_livro(livro1)
    biblioteca.cadastrar_livro(livro2)
    biblioteca.cadastrar_livro(livro3)

    # Cadastrando pessoas
    usuario1 = Usuario("Ana Souza", "111.111.111-11", "2024001")
    bibliotecaria = Bibliotecario("Carla Lima", "222.222.222-22", "F001")

    biblioteca.cadastrar_usuario(usuario1)

    print(usuario1.apresentar())
    print(bibliotecaria.apresentar())
    print(biblioteca)
    print()

    # Mostrando o acervo (usando o iterador da Biblioteca)
    print("Acervo atual:")
    for livro in biblioteca:
        print(" -", livro)
    print()

    # Fazendo um empréstimo
    try:
        biblioteca.emprestar_livro(usuario1.matricula, livro1.isbn)
    except (LivroIndisponivelException, LivroNaoEncontradoException,
            UsuarioNaoEncontradoException, LimiteEmprestimosExcedidoException) as erro:
        print("Erro:", erro)

    print()
    print("Livro 1 depois do empréstimo:", livro1)
    print("Livros com Ana:", [str(l) for l in usuario1.livros_emprestados])
    print()

    # Tentando emprestar o mesmo livro de novo (deve dar erro)
    try:
        biblioteca.emprestar_livro(usuario1.matricula, livro1.isbn)
    except LivroIndisponivelException as erro:
        print("Erro esperado:", erro)

    print()

    # Devolvendo o livro
    biblioteca.devolver_livro(usuario1.matricula, livro1.isbn)
    print("Livro 1 depois da devolução:", livro1)


if __name__ == "__main__":
    main()
