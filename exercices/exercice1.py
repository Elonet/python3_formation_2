# -*- coding: utf-8 -*-


class Pile:
    """
    Represente une pile d'elements
    """

    def __init__(self):
        self.__elements = []

    @property
    def elements(self):
        return self.__elements

    @property
    def top(self):
        if len(self.elements) > 0:
            return self.elements[len(self.elements) - 1]

        return None

    def empiler(self, element):
        self.__elements.append(element)

    def depiler(self):
        if len(self.elements) > 0:
            self.elements.remove(self.elements[len(self.elements) - 1])

    def __str__(self):
        result = ''
        for i in range(len(self.elements) - 1, -1, -1):
            result += str(self.elements[i])

            if i > 0:
                result += '\n'

        return result


class Disque:
    """
    Represente un disque
    """

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def __str__(self):
        result = '|'
        for i in range(self.size):
            result += '-'
        return result + '|'

    def __eq__(self, other):
        if type(other) == self.__class__:
            return self.size == other.size
        else:
            return False

    def __gt__(self, other):
        if type(other) == self.__class__:
            return self.size > other.size
        return False

    def __lt__(self, other):
        if type(other) == self.__class__:
            return self.size < other.size
        return False
