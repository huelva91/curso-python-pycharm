import random
from abc import ABC, abstractmethod
import logging as log
import Excepciones as ex

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('logs/Orquesta_log.log'),
                    log.StreamHandler()
                ])


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo
        self.afinado = False

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @abstractmethod
    def afinar(self):
        numero_afinar_aleatorio = random.randint(0, 10)
        if numero_afinar_aleatorio > 1:
            self.afinado = True
        else:
            self.afinado = False

    @abstractmethod
    def tocar(self):
        """"""
        if self.afinado == True:
            log.info("Tocando el instrumento {} y esta afinado".format(self.nombre))
        else:
            raise ex.AfinadoException("Un instrumento no esta afinado")

        self.afinar()
        self.tocar()


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, num_cuerdas):
        super().__init__(nombre, tipo)
        self._num_cuerdas = num_cuerdas

    def afinar(self):
        pass


class Guitarra_electrica(Guitarra):
    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        super().__init__(nombre, tipo, num_cuerdas)
        self._potencia = potencia


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre, tipo)
        self._num_teclas = num_teclas


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, tamanio):
        super().__init__(nombre, tipo)
        self._tamanio = tamanio

    def aporrear(self):
        pass


class Orquesta:

    def crear_orquesta(self):
        guitarra1 = Guitarra("Guitarra 1", "Cuerda", 6)
        guitarra2 = Guitarra_electrica("Guitarra 2", "Cuerda", 150, 5)
        piano = Piano("Piano 1", "Cuerda", 105)
        tambor = Tambor("Tambor1", "Percusion", 30)
        lista_instrumentos = [guitarra1, guitarra2, piano, tambor]
        return lista_instrumentos

    def iniciar_concierto(self, lista_instrumentos):
        for instrumento in lista_instrumentos:
            try:
                instrumento.afinar()
            except:
                ex.AfinadoException
                log.info("El instrumento {} no esta afinado".format(instrumento.nombre))
            instrumento.tocar()


orquesta = Orquesta()
orquesta.iniciar_concierto(orquesta.crear_orquesta())
