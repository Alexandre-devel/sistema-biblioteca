from pessoa import Pessoa


class Bibliotecario(Pessoa):
    """
    Representa o funcionário responsável por registrar empréstimos e devoluções.
    """

    def __init__(self, nome, cpf, registro_funcional):
        super().__init__(nome, cpf)
        self._registro_funcional = registro_funcional

    @property
    def registro_funcional(self):
        return self._registro_funcional

    def apresentar(self):
        return f"Bibliotecário(a): {self._nome} (registro {self._registro_funcional})"
