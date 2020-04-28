from listas import Lista
import numpy as np
from numpy.linalg import inv, det

# Função para colocar numeros Sobre escritos
def sobrescrito(numero):
    sups = {'0': u'\u2070',
            '1': u'\xb9',
            '2': u'\xb2',
            '3': u'\xb3',
            '4': u'\u2074',
            '5': u'\u2075',
            '6': u'\u2076',
            '7': u'\u2077',
            '8': u'\u2078',
            '9': u'\u2079'}
    return sups[f'{str(numero)}']

# Função para cálcular a equação de ajuste
def mmq(grau, lista_x, lista_y, usual=False):
    # Cria uma tabela para guardar os valores que serão usados no ajuste
    tabela = {}

    # Gera os valores necessários para o ajuste
    for i in range(1, (grau * 2) + 1):
        # x^1 até x^(grau do polinomio * 2)
        tabela[f'x^{i}'] = [lista_x[c] ** i for c in range(len(lista_x))]
    for i in range(grau + 1):
        # y*x^0 até y*x^(grau do polinomio +1)
        if i == 0:
            tabela['y'] = lista_y
        else:
            tabela[f'y*x^{i}'] = [lista_y[x] * tabela[f'x^{i}'][x] for x in range(len(lista_x))]

    # Faz os somatórios dos valores gerados acima
    tabela_soma = {}
    for i in range(1, (grau * 2) + 1):
        tabela_soma[f'x^{i}'] = sum(tabela[f'x^{i}'])
    for i in range(grau + 1):
        if i == 0:
            tabela_soma['y'] = sum(tabela['y'])
        else:
            tabela_soma[f'y*x^{i}'] = sum(tabela[f'y*x^{i}'])

    # Cria a matriz dos somatórios de X
    aux = list()
    for c in range(0, grau + 1):
        for i in range(c, c + grau + 1):
            if i == 0:
                aux.append(len(tabela['x^1']))
            else:
                aux.append(tabela_soma[f'x^{i}'])
    a = np.round(np.array(aux).reshape(grau + 1, grau + 1), 3)

    # Cria a matriz dos somatórios Y*X
    aux.clear()
    aux.append(tabela_soma['y'])
    for i in range(1, grau + 1):
        aux.append(tabela_soma[f'y*x^{i}'])
    b = np.round(np.array(aux).reshape(grau + 1, 1), 3)

    # Verifica se a matriz pode ser invertida
    if det(a) == 0:
        # Se não, mostra ao usuario
        print('A matriz não é inversível')
    else:
        # Se sim, monta a equação ajustada
        x = np.round(np.dot(inv(a), b), 3)
        eq_ajustada = ''
        if not usual:
            # Monta a equação na forma matemática
            for i in range(grau + 1):
                if i == 0:
                    eq_ajustada += f'{float(x[0])}'
                elif i == 1:
                    eq_ajustada += f' + {float(x[i])}x'
                else:
                    eq_ajustada += f' + {float(x[i])}x^{sobrescrito(i)}'
        else:
            # Monta a equação na forma computacional
            for i in range(grau + 1):
                if i == 0:
                    eq_ajustada += f'{float(x[i])}'
                else:
                    eq_ajustada += f'+{float(x[i])}x^{i}'

    return eq_ajustada


def r2(grau_poli, valores_x, valores_y):
    def f(x):
        res = 0
        eq = mmq(grau_poli, valores_x, valores_y, True).split('+')

        for i in range(len(eq)):
            if i == 0:
                res += float(eq[0])
            else:
                aux = eq[i].split('x')
                res += float(aux[0]) * (x ** int(aux[1][1:]))
        return res

    # Somatório dos Quadrados Total
    media_y = sum(valores_y) / len(valores_y)
    sqtot = 0
    for i in range(len(valores_y)):
        sqtot += (valores_y[i] - media_y) ** 2

    # Soma do Quadrado dos Resíduos
    y_est = [f(x) for x in valores_x]
    sqres = 0
    for i in range(len(valores_y)):
        sqres += (valores_y[i] - y_est[i]) ** 2

    return round(1 - sqres/sqtot, 3)


if __name__ == '__main__':

    l1 = [2, 3, 4]
    l2 = [3, 4, 5]
    print(mmq(1, l1, l2))
    print(r2(1, l1, l2))
