""" 
Exemplo de código para o DIP implementado da maneira CORRETA.

"""

from abc import ABC
class Somar(ABC):
    """
    Classe Somar abstrata que atua como interface para a classe operacaoSoma.
    """
    def somar(self, digito1, digito2) -> any:
        pass
    
class operacaoSoma(Somar):
    """ 
    Módulo baixo nível: A classe operacaoSoma é um módulo baixo nível 
    pois ela depende de uma classe abstrata (Somar) para funcionar.
    """
    def somar(self, digito1, digito2) -> any:
        print(f'A soma entre {digito1} e {digito2} é = {digito1 + digito2}')
        return digito1 + digito2
    
    
class App: 
    """
    Módulo alto nível: A classe App é um módulo alto nível.
    Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações;
    """
    
    def __init__(self, somar: Somar):
        self.somar = somar

    def start(self):
        self.somar.somar(5, 10)
        
if __name__ == '__main__':
    somar = operacaoSoma()
    app = App(somar)
    app.start()