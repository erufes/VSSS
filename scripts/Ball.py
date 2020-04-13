""" Nome do módulo :        Ball
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que define bola em campo
    Versão :                2.0
    Pré-requisitos :        Agente
                            Ponto
    Membros :               Lorena Bassani
"""
from Agente import Agente
from Geometria import Ponto
from Patterns.Singleton import Singleton


class Ball(Agente, Singleton):

    def __init__(self, *args, **keyargs):
        super().__init__()
        pass

    def inicializa(self, ponto=Ponto()):
        Agente.__init__(self, ponto)

    def __str__(self):
        return '[Ball] ' + super().__str__()
