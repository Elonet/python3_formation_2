# -*- coding: utf-8 -*-

import docopt
from terminaltables import AsciiTable
from exercice3 import PileDisqueOrdered, Disque


class MyExit(Exception):
    usage = ''

    def __init__(self, message=''):
        Exception.__init__(self, (message + '\n' + self.usage).strip())


class HanoiApp:

    def __init__(self, nombre_disques=4):
        self.__nombre_disques = nombre_disques
        self.__piles = []

    def __init_piles(self):
        self.__piles = [PileDisqueOrdered(), PileDisqueOrdered(), PileDisqueOrdered()]
        for i in range(self.__nombre_disques, 0, -1):
            self.__piles[0].empiler(Disque(2 * i - 1))

    def __demander_mouvement(self):
        usage = "Usage: from <src> to <dst>"
        print(usage)

        mouvement_effectue = False
        while not mouvement_effectue:
            response = input('Entrez votre mouvement : from ')

            parts = response.split(' ')

            try:
                args = docopt.docopt(usage, argv=parts)
                src = int(args['<src>'])
                dst = int(args['<dst>'])

                if max(src, dst) > len(self.__piles) - 1 or min(src, dst) < 0:
                    print('Saisie incorrecte : indices invalides.')
                    continue

                if src == dst:
                    print('Saisie incorrecte : Indices identiques')
                    continue

                if self.__piles[src].top is None:
                    print('Saisie incorrecte : Pile source vide')
                    continue

                if self.__piles[dst].top is not None:
                    if self.__piles[src].top > self.__piles[dst].top:
                        print('Saisie inccorecte : Disque trop grand pour la pile destination')
                        continue

                self.__piles[dst].empiler(self.__piles[src].top)
                self.__piles[src].depiler()
                mouvement_effectue = True

            except Exception:
                print('Saisie incorrecte.')
                print(usage)

    def start(self):
        self.__init_piles()
        print('== Tours de Hanoi ==')
        self.afficher_piles()
        self.__demander_mouvement()
        self.afficher_piles()

    def afficher_piles(self):
        head = ['Pile ' + str(i) for i in range(0, len(self.__piles))]
        data = [str(pile) for pile in self.__piles]

        table = [head]
        table.extend([data])

        astable = AsciiTable(table)
        print(astable.table)