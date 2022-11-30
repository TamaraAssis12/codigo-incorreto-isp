"""
O padrão Bridge perimite que você divida uma classe grande ou um conjunto de classes 

intimamente ligadas em duas hierarquias separadas - Abstração e Implementação - 

que podem ser desenvolvidas independentemente umas das outras.
"""
from abc import ABC, abstractmethod

class quadrado(ABC):
    @abstractmethod
    def desenharQuadrado(self):
        pass

class circulo():
    @abstractmethod
    def desenharCirculo(self):
        pass

class corVermelha():
    @abstractmethod
    def pintarCorVermelha(self):
        pass

class corAzul():
    @abstractmethod
    def pintarCorAzul(self):
        pass
        
class quadradoVermelho(quadrado, corVermelha):
    def desenharQuadrado(self):
        print("Quadrado Vermelho")
        
    def pintarCorVermelha(self):
        print("Pintando de vermelho")

class quadradoAzul(quadrado, corAzul):
    def desenharQuadrado(self):
        print("Quadrado Azul")
        
    def pintarCorAzul(self):
        print("Pintando de azul")
        
class circuloVermelho(circulo, corVermelha):
    def desenharCirculo(self):
        print("Circulo Vermelho")
        
    def pintarCorVermelha(self):
        print("Pintando de vermelho")
        
class circuloAzul(circulo, corAzul):
    def desenharCirculo(self):
        print("Circulo Azul")
        
    def pintarCorAzul(self):
        print("Pintando de azul")
        
# Instanciando as classes
quadrado_vermelho = quadradoVermelho()
quadrado_vermelho.desenharQuadrado()
quadrado_vermelho.pintarCorVermelha()

circulo_vermelho = circuloVermelho()
circulo_vermelho.desenharCirculo()
circulo_vermelho.pintarCorVermelha()

quadrado_azul = quadradoAzul()
quadrado_azul.desenharQuadrado()
quadrado_azul.pintarCorAzul()

circulo_azul = circuloAzul()
circulo_azul.desenharCirculo()
circulo_azul.pintarCorAzul()


    