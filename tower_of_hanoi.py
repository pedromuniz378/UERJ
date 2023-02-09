class Hanoi:
    """Implementação da Torre de Hanoí com Autômatos de Pilha para 4 discos."""

    def __init__(self):
        """Cria a classe e define:

            -self.__n é o número de discos, 4 por padrão;\n
            -self.stack é a pilha e inicia com 'Z';\n
            -self.states são os estados possíveis para o autômato;\n
            -self.curr_state é o estado atual do autômato;\n
            -self.tower é a Torre de Hanoí, um dicionário com uma lista pra
                cada pino.
        """
        self.__n = 4
        self.stack = ['Z']

        self.states = ['q0', '400', '310', '211', '202', '112',
                       '220', '130', '031', '022', '013', '004', 'qf']
        self.curr_state = self.states[0]

        self.tower = {'0': [d for d in range(self.__n, 0, -1)],
                      '1': [], '2': []}

        self.lb = '\u03BB'
        self.tf = {
            f'{self.lb}, Z':  [self.states[1], '100'],  # 400
            'a, 100': [self.states[2], '210'],  # 310
            'b, 210': [self.states[3], '312'],  # 211
            'd, 134': [self.states[4], '103'],  # 202
            'd, 312': [self.states[4], '301'],  # 202
            'd, 124': [self.states[4], '132'],  # 202
            'a, 301': [self.states[5], '431'],  # 112
            'a, 103': [self.states[5], '213'],  # 112
            'a, 132': [self.states[5], '012'],  # 112
            'e, 431': [self.states[3], '132'],  # 211
            'e, 231': [self.states[3], '134'],  # 211
            'f, 132': [self.states[6], '120'],  # 220
            'a, 120': [self.states[7], '410'],  # 130
            'b, 410': [self.states[8], '014'],  # 031
            'd, 014': [self.states[9], '021'],  # 022
            'c, 021': [self.states[5], '231'],  # 112
            'b, 213': [self.states[10], '012'],  # 013
            'd, 012': [self.states[11], '001'],  # 004
            f'{self.lb}, 001': [self.states[-1], self.lb]  # qf
        }

    def print_status(self, c, stack_top, transition):
        """Imprime na tela a disposição dos discos em cada pino e informações
        do automato."""
        dt = '\u03B4'
        c = '\u03BB' if c == ' ' else c
        transition = self.tf[f'{c}, {stack_top}']
        # print(c, stack_top)

        print(f'\t[ Torre de Hanoí 0 ] {str(self.tower["0"]):<12} ' +
              f'\t[ Autômato ] Estado: {self.curr_state}')
        print(f'\t[ Torre de Hanoí 1 ] {str(self.tower["1"]):<12} ' +
              f'\t[ Autômato ] Topo da Pilha: {self.stack[-1]}')
        print(f'\t[ Torre de Hanoí 2 ] {str(self.tower["2"]):<12} ' +
              f'\t[ Autômato ] Entrada: {c}')
        print(f'{" "*47} [ Autômato ] Transição: {dt}({c}, {self.curr_state}, ' +
              f'{stack_top}) = {{({transition[0]}, {transition[1]})}}\n')

    def __move(self, src, dest):
        """Move um disco de src (origem) para dest (destino)."""
        disk = self.tower[src].pop()
        self.tower[dest].append(disk)

    def evolve_status(self, input, stack_top):
        """Função de Transição.

        Evolui do autômato, dado um caractere de entrada(input) e o que está no
        topo da pilha(stack_top)."""
        # Define as transições
        # Move os discos na Torre
        match input:
            case 'a':
                self.__move('0', '1')
            case 'b':
                self.__move('0', '2')
            case 'c':
                self.__move('1', '0')
            case 'd':
                self.__move('1', '2')
            case 'e':
                self.__move('2', '0')
            case 'f':
                self.__move('2', '1')

        # Tenta evoluir a configuração do autômato
        try:
            '''Se a combinação (entrada, topo da pilha) existir,
            evolui o estado, tira o que está no topo da pilha
            e empilha o que for necessário e retorna True.'''
            result = self.tf[f'{input.replace(" ", self.lb)}, {stack_top}']
            self.print_status(input, self.stack[-1], result)
            self.curr_state = result[0]
            self.stack.pop()
            self.stack.append(result[1])
            return result
        except KeyError:
            # Se a combinação não existir mata o automato e retorna False
            print('\t[ Autômato ] Não foi possível ler ' +
                  f'{input.replace(" ", self.lb)}, e desempilhar {stack_top}!')
            print('\t[ Autômato ] O Autômato morreu!')
            return False

    def run(self, input_):
        """Executa o autômato."""
        '''Coloca um caractere em branco antes e depois da cadeia para sair
        do estado q0 e chegar no estado qf.'''
        input_ = f' {input_.strip()} '

        # Itera sobre cada caractere da entrada, evoluindo a configuração
        # result = ['400', '100']
        for c in input_:
            # Imprime a configuração do autômato e da torre.
            # self.print_status(c, self.stack[-1], result)
            result = self.evolve_status(c, self.stack[-1])
            '''Se a evolução dos estados retornar False, quer dizer que o
            autômato está morto e as iterações devem terminar'''
            if not result:
                break
        # Se todos os discos estiverem no pino 2, problema resolvido.
        if len(self.tower['2']) == self.__n:
            print('\t[ Torre de Hanoí ] Problema resolvido!')


if __name__ == '__main__':
    # Cria uma Torre e executa a entrada
    hanoi = Hanoi()
    hanoi.run('abdaefabdcedabd')
