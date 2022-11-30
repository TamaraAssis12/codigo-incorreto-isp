from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    A interface Handler declara um método para construir a cadeia de manipuladores.
    Ele também declara um método para executar uma solicitação.
    """

    @abstractmethod
    def set_proximo(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    O comportamento de encadeamento padrão pode ser implementado dentro de um manipulador base
    handler class.
   
    """

    _proximo_handler: Handler = None

    def set_proximo(self, handler: Handler) -> Handler:
        self._proximo_handler = handler
        # Retornar um manipulador daqui nos permitirá vincular 
        # manipuladores de uma maneira conveniente como esta:
        # macaco.set_proximo(Esquilo).set_proximo(cachorro)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._proximo_handler:
            return self._proximo_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class MacacoHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Macaco: Vou comer  {request}"
        else:
            return super().handle(request)


class EsquiloHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Noz":
            return f"Esquilo: Vou comer  {request}"
        else:
            return super().handle(request)


class CachorroHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Almôndega":
            return f"Cachorro: Vou comer  {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    O código do cliente geralmente é adequado para trabalhar com um único manipulador. Na maioria
    Nos casos, ele nem sequer está ciente de que o manipulador faz parte de uma cadeia.
    """

    for comida in ["Noz", "Banana", "Xícara de café"]:
        print(f"\nCliente:Quem quer uma {comida}?")
        result = handler.handle(comida)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {comida} foi deixado intocado.", end="")


if __name__ == "__main__":
    macaco = MacacoHandler()
    Esquilo = EsquiloHandler()
    cachorro = CachorroHandler()

    macaco.set_proximo(Esquilo).set_proximo(cachorro)

    # O cliente deve ser capaz de enviar uma solicitação para qualquer manipulador, não apenas para o
    # primeiro da cadeia.
    print("Cadeia: Macaco > Esquilo > Cachorro")
    client_code(macaco)
    print("\n")

    print("Subcadeia: Esquilo > Cachorro")
    client_code(Esquilo)