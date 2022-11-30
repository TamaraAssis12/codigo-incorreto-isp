class Email(object):
    def __init__(self):
        self._de = None
        self._para = None
        self._assunto = None
        self._corpo = None
        
class BuilderEmail(object):
    def __init__(self):
        self.email = Email()
        
    def add_de(self, de):
        self.email._de = de
        return self
    
    def add_para(self, para):
        self.email._para = para
        return self
    
    def add_assunto(self, assunto):
        self.email._assunto = assunto
        return self
    
    def add_corpo(self, corpo):
        self.email._corpo = corpo
        return self
    
    def get_email(self):
        return self.email
    
    def enviar_email(self):
        print("Enviando email...")
        print("De: {}".format(self.email._de))
        print("Para: {}".format(self.email._para))
        print("Assunto: {}".format(self.email._assunto))
        print("Corpo: {}".format(self.email._corpo))
        
if __name__ == "__main__":
    email = BuilderEmail()
    email.add_de("thamaraassis@hotmail.com")
    email.add_para("fabricio.dias@email.com")
    email.add_assunto("Exemplo de Builder")
    email.add_corpo("Exemplo de código para o Builder implementado da maneira CORRETA, pois respeita o Builder.")
    email.enviar_email()



        