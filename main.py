from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    La interfaz Sujeto declara un conjunto de métodos para administrar suscriptores.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Adjuntar un observador al sujeto.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Separar un observador del sujeto.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notificar a todos los observadores sobre un evento.
        """
        pass


class ConcreteSubject(Subject):
    """
    El Sujeto posee algún estado importante y notifica a los observadores cuando el estado
    cambios.
    """

    _state: int = None
    """
    En aras de la simplicidad, el estado del Sujeto, esencial a todo
    suscriptores, se almacena en esta variable.
    """

    _observers: List[Observer] = []
    """
    Lista de suscriptores. En la vida real, la lista de suscriptores se puede almacenar
    de manera más completa (categorizados por tipo de evento, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Sujeto: Adjunto un observador.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Los métodos de gestión de suscripciones.
    """

    def notify(self) -> None:
        """
        Activar una actualización en cada suscriptor.
        """

        print("Asunto: Observadoras notificantes...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Por lo general, la lógica de suscripción es solo una fracción de lo que un Sujeto puede
        realmente. Los sujetos comúnmente tienen alguna lógica comercial importante, que
        activa un método de notificación cada vez que algo importante está a punto de suceder
        suceder (o después).
        """

        print("\nSujeto: Estoy haciendo algo importante..")
        self._state = randrange(0, 10)

        print(f"Sujeto: Mi estado acaba de cambiar a: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recibir actualización del asunto.
        """
        pass


"""
Los Observadores Concretos reaccionan a las actualizaciones emitidas por el Sujeto que les había sido
adjunto a.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: reaccionó al evento")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: reaccionó al evento")


if __name__ == "__main__":
    # El código cliente.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()