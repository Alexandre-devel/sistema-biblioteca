from abc import ABC, abstractmethod


class Pessoa(ABC):
    """
    Classe abstrata que representa qualquer pessoa que interage com o sistema
    (Usuario ou Bibliotecario). Não pode ser instanciada sozinha, pois define
    apenas o que é comum a todas as pessoas do sistema.
    """

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @abstractmethod
    def apresentar(self):
        """
        Cada subclasse (Usuario, Bibliotecario) deve implementar esse método
        do seu próprio jeito. Isso é um exemplo de polimorfismo.
        """
        pass
