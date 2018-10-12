# -*- coding: utf-8 -*-

from terminaltables import AsciiTable
from exercice3 import PileDisqueOrdered, Disque


class HanoiApp:

    def __init__(self, nombre_disques=4):
        self.__nombre_disques = nombre_disques
        self.__piles = []

    def __init_piles(self):
        self.__piles = [PileDisqueOrdered(), PileDisqueOrdered(), PileDisqueOrdered()]
        for i in range(self.__nombre_disques, 0, -1):
            self.__piles[0].empiler(Disque(2 * i - 1))

    def start(self):
        self.__init_piles()

    def afficher_piles(self):
        head = ['Pile ' + str(i) for i in range(0, len(self.__piles))]
        data = [str(pile) for pile in self.__piles]

        table = [head]
        table.extend([data])

        astable = AsciiTable(table)
        print(astable.table)
