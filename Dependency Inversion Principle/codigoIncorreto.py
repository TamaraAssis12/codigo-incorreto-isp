"""
Exemplo de código para o DIP implementado da maneira INCORRETA, pois não respeita o DIP.

O DIP diz que as classes de alto nível não devem depender de classes de baixo nível, mas sim de abstrações.

"""
class operacaoSomar:
    def somar(self, digito1, digito2):
        print(f'A soma entre {digito1} e {digito2} é = {digito1 + digito2}')
        return digito1 + digito2


class App:
    def start(self):
        operacaoSomar().somar(5, 10)

if __name__ == '__main__':
    app = App()
    app.start()
