# -*- coding: utf-8 -*-

from exercice1 import Pile, Disque


class PileDisqueOrdered(Pile):

    def empiler(self, element):
        if not isinstance(element, Disque):
            raise Exception('Disque object expected')

        if len(self.elements) > 0:
            if self.top < element:
                raise Exception('Too large')

        super().empiler(element)