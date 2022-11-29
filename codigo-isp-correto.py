"""
IMPLEMENTAÇÃO CORRETA DO ISP
"""

from abc import ABC, abstractmethod

class animaisZoo(ABC):
   
    def __init__(self, nome):
        self.nome = nome
        
    @abstractmethod
    def alimentarAnimal(self):
        pass
    
    def dormir(self):
        pass

class Cobra(animaisZoo):
    def alimentarAnimal(self):
        print("Alimentando a cobra com ratos")
        
    def dormir(self):
        print(f"A cobra {self.nome} está dormindo")
        
class Macaco(animaisZoo):
    def alimentarAnimal(self):
        print("Alimentando o macaco com bananas")
        
    def dormir(self):
        print(f"O macaco {self.nome} está dormindo")
        
class Leao(animaisZoo):
    def alimentarAnimal(self):
        print("Alimentando o leão com carne")
        
    def dormir(self):
        print(f"O leão {self.nome} está dormindo")
        
class Panda(animaisZoo):
    def alimentarAnimal(self):
        print("Alimentando o panda com bambu")
        
    def dormir(self):
        print(f"O panda {self.nome} está dormindo")
        
# Instanciando as classes:
zoo = [Cobra("Cobra"), Macaco("Macaco"), Leao("Leão"), Panda("Panda")]
for animal in zoo:
    animal.alimentarAnimal()
    animal.dormir()
