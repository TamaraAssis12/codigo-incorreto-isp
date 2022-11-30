""" 
Exemplo de código para o DIP implementado da maneira CORRETA.

"""

from abc import ABC

class Somar(ABC):
    def somar(self, digito1, digito2) -> any:
        pass
    
class operacaoSoma(Somar):
    def somar(self, digito1, digito2) -> any:
        print(f'A soma entre {digito1} e {digito2} é = {digito1 + digito2}')
        return digito1 + digito2
    
    
class App:
    def __init__(self, somar: Somar):
        self.somar = somar

    def start(self):
        self.somar.somar(5, 10)
        
if __name__ == '__main__':
    somar = operacaoSoma()
    app = App(somar)
    app.start()