# -*- coding: utf-8 -*-

from exercice1 import Pile, Disque


class PileDisque(Pile):

    def empiler(self, element):
        if not isinstance(element, Disque):
            raise Exception('Disque object expected')
        super().empiler(element)