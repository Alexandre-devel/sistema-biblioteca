from functools import wraps


def avisar_operacao(func):
    """
    Decorador que "embrulha" uma função da Biblioteca (como emprestar_livro
    ou devolver_livro) para sempre avisar no console que a operação foi
    concluída com sucesso, sem precisar repetir esse aviso dentro de cada
    método.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"[Aviso] Operação '{func.__name__}' concluída com sucesso.")
        return resultado

    return wrapper
