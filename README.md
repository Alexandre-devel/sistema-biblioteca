# 📚 Sistema de Gestão de Acervo Bibliotecário

Projeto prático desenvolvido para demonstração dos pilares de Programação Orientada a Objetos (POO) em Python: abstração, herança, polimorfismo, encapsulamento e tratamento de exceções.

---

## 📌 Funcionalidades
- Cadastro de livros com controlo de estado (disponível/emprestado).
- Diferenciação de perfis (`Usuário` e `Bibliotecário`) a partir da classe abstrata `Pessoa`.
- Gestão de empréstimos com limite por leitor (máximo de 3 exemplares).
- Prazos automáticos de devolução (14 dias) e identificação de atrasos.
- Busca no acervo por título parcial ou ISBN exato.
- Utilização de decoradores para registo de operações concluídas com sucesso.

---

## 🛠️ Tecnologias e Bibliotecas
- **Python 3.10+**
- Módulos nativos da linguagem: `abc`, `datetime`, `functools`

---

## 📐 Diagrama de Classes

```mermaid
classDiagram
    class Pessoa {
        <<abstract>>
        #_nome: str
        #_cpf: str
        +nome() str
        +cpf() str
        +apresentar()* str
    }

    class Usuario {
        -_matricula: str
        -_livros_emprestados: list
        +matricula() str
        +livros_emprestados() list
        +pode_pegar_emprestado() bool
        +adicionar_livro(livro) void
        +remover_livro(livro) void
        +apresentar() str
    }

    class Bibliotecario {
        -_registro_funcional: str
        +registro_funcional() str
        +apresentar() str
    }

    class Livro {
        -_titulo: str
        -_autor: str
        -_isbn: str
        -_ano: int
        -_disponivel: bool
        +titulo() str
        +autor() str
        +isbn() str
        +ano() int
        +disponivel() bool
        +marcar_como_emprestado() void
        +marcar_como_disponivel() void
        +__eq__(other) bool
        +__str__() str
    }

    class Emprestimo {
        +livro: Livro
        +usuario: Usuario
        +data_emprestimo: date
        +data_prevista_devolucao: date
        +data_devolucao: date
        +registrar_devolucao() void
        +esta_atrasado() bool
        +__str__() str
    }

    class Biblioteca {
        +nome: str
        -_acervo: list
        -_usuarios: list
        -_emprestimos: list
        +cadastrar_livro(livro) void
        +cadastrar_usuario(usuario) void
        +buscar_livro_por_isbn(isbn) Livro
        +buscar_livro_por_titulo(titulo) list
        +buscar_usuario_por_matricula(matricula) Usuario
        +emprestar_livro(matricula, isbn) Emprestimo
        +devolver_livro(matricula, isbn) Emprestimo
    }

    Pessoa <|-- Usuario
    Pessoa <|-- Bibliotecario
    Biblioteca "1" *-- "*" Livro
    Biblioteca "1" *-- "*" Usuario
    Biblioteca "1" *-- "*" Emprestimo
    Emprestimo "1" --> "1" Livro
    Emprestimo "1" --> "1" Usuario
```

---

## 🚀 Como Executar

```bash
python src/main.py
```

---

## 👥 Divisão de Tarefas

| Integrante | Atribuição / Responsabilidade |
| :--- | :--- |
| **Integrante 1** | Modelagem das entidades `Pessoa`, `Usuario` e `Bibliotecario` (Herança e Polimorfismo) |
| **Integrante 2** | Modelagem das classes `Livro` e `Emprestimo` (Regras de comparação e datas) |
| **Integrante 3** | Classe `Biblioteca`, Dunder Methods e gestão central do acervo |
| **Integrante 4** | Exceções personalizadas, Decoradores e script `main.py` de testes |
