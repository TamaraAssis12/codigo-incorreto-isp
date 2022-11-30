"""
Exemplo de código para o ISP implementado da maneira INCORRETA.

Nesse exemplo, a função do código é realizar chamadas de voz, enviar mensagens de texto e acessar a internet. 

Porém o código está implementado de maneira incorreta, pois não respeita o ISP. O ISP diz que uma classe não deve ser forçada a implementar métodos que ela não vai usar.

E como o método enviarMensagem e acessarInternet estão sendo forçados a serem implementados na classe telefoneFixo, que não vai usar esses métodos, o código está incorreto.

"""

from abc import ABC, abstractmethod

class dispositivoComunicacao():
    @abstractmethod
    def fazerLigaçao(self):
        pass
    
    @abstractmethod
    def enviarMensagem(self):
        pass
    
    @abstractmethod
    def acessarInternet(self):
        pass
    
class celular(dispositivoComunicacao):
    def fazerLigaçao(self):
        print("Celular realizando ligação")
        
    def enviarMensagem(self):
        print("Celular enviando mensagem")
        
    def acessarInternet(self):
        print("Celular acessando a internet")
        
        
class telefoneFixo(dispositivoComunicacao):
    def fazerLigaçao(self):
        print("Telefone fixo realizando ligação")
        
    def enviarMensagem(self):
        raise Exception("Telefone fixo não envia mensagem")
    
    def acessarInternet(self):
        raise Exception("Telefone fixo não acessa internet")

# Instanciando as classes
celular = celular()
celular.fazerLigaçao()
celular.enviarMensagem()
celular.acessarInternet()

telefone = telefoneFixo()
telefone.fazerLigaçao()
telefone.enviarMensagem()
telefone.acessarInternet()



