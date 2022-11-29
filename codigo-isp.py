"""
Exemplo de código para o ISP implementado da maneira INCORRETA.

Nesse exemplo, a função do código é alimentar os animais de um zoológico

e coloca-los para dormir.
"""

class Cobra:
    def alimentar_cobra(self):
        print("Alimentando a cobra com ratos")
        
    def dormir(self):
        print("A cobra está dormindo")
        
class Macaco:
    def alimentar_macaco(self):
        print("Alimentando o macaco com bananas")
        
    def dormir(self):
        print("O macaco está dormindo")
        
class Leao:
    def alimentar_leao(self):
        print("Alimentando o leão com carne")
        
    def dormir(self):
        print("O leão está dormindo")
        
class Panda:
    def alimentar_panda(self):
        print("Alimentando o panda com bambu")
        
    def dormir(self):
        print("O panda está dormindo")

# Instanciando as classes:
cobra = Cobra()
macaco = Macaco()
leao = Leao()
panda = Panda() 

cobra.alimentar_cobra()
macaco.alimentar_macaco()
leao.alimentar_leao()
panda.alimentar_panda()