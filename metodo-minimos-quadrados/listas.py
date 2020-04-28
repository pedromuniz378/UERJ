"""Operações com listas"""


class Lista:
    def __init__(self, lista):
        self.__valores = lista
        self.__tam = len(lista)

    def __len__(self):
        c = i = 0
        while True:
            try:
                if self.__valores[i] is not None:
                    c += 1
            except IndexError:
                return c
            i += 1

    def __repr__(self):
        repr = '['
        for c in range(len(self)):
            if c != len(self) - 1:
                repr += f'{self.__valores[c]}, '
            else:
                repr += f'{self.__valores[c]}]'
        return repr

    def __pow__(self, power, modulo=None):
        aux = list()
        for c in range(self.__tam):
            aux.append(self.__valores[c] ** power)
        return Lista(aux)

    def __add__(self, lista2):
        soma = list()
        if self.__tam == len(lista2):
            for i in range(self.__tam):
                soma.append(self.__valores[i] + lista2.get_valores()[i])
            return Lista(soma)
        else:
            return 'As Listas devem ser do mesmo tamanho.'

    def __mul__(self, lista2):
        mult = list()
        if self.__tam == len(lista2):
            for i in range(self.__tam):
                mult.append(self.__valores[i] * lista2.get_valores()[i])
            return Lista(mult)
        else:
            return 'As Listas devem ser do mesmo tamanho.'

    def __getitem__(self, item):
        return self.__valores[item]

    def soma(self):
        soma = 0
        for i in range(self.__tam):
            soma += self.__valores[i]
        return soma

    def get_valores(self):
        return self.__valores

l1 = Lista([1,2,3])
# l2 = Lista([1,2,3])


# lista = []
# for i in range(len(l1)):
#     lista.append(l1.get_valores()[i])
# print(lista)
# print(l1[1])
# print(l2)