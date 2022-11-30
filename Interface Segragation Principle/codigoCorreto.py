"""
Exemplo de código para o ISP implementado da maneira CORRETA, pois respeita o ISP.

"""

from abc import ABC, abstractmethod

class Chamada(ABC):
    @abstractmethod
    def fazerLigaçao(self):
        pass

class mensagemTexto():
    @abstractmethod
    def enviarMensagem(self):
        pass
    
class acessoInternet():
    @abstractmethod
    def acessarInternet(self):
        pass

class celular(Chamada, mensagemTexto, acessoInternet):
    def fazerLigaçao(self):
        print("Celular realizando ligação")
        
    def enviarMensagem(self):
        print("Celular enviando mensagem")
        
    def acessarInternet(self):
        print("Celular acessando a internet")
        
class telefoneFixo(Chamada):
    def fazerLigaçao(self):
        print("Telefone fixo realizando ligação")
        
        
# Instanciando as classes
celular = celular()
telefoneFixo = telefoneFixo()

celular.fazerLigaçao()
celular.enviarMensagem()
celular.acessarInternet()

telefoneFixo.fazerLigaçao()
