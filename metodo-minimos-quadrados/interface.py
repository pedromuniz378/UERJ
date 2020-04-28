from tkinter import *
from mmq import mmq, r2, sobrescrito
import matplotlib.pyplot as plt
from os import remove, rename

# Função que cria a janela de confirmação de dados inseridos
def confirma():
    def confirmado():
        # Validação simples dos dados inseridos
        try:
            # Verifica se o primeiro campo (valores de X) está vazio
            if get_texto()[0] == 0:
                lbl_msg['text'] = 'Favor inserir o grau do polinomio.'
                confirmar.destroy()

            # Verifica se o segundo campo (valores de Y) está vazio
            elif len(get_texto()[1]) == 0:
                lbl_msg['text'] = 'Favor inserir os valores de X.'
                confirmar.destroy()

            # Verifica se o terceiro campo (graudo polinomio a ser ajustado) está vazio
            elif len(get_texto()[2]) == 0:
                lbl_msg['text'] = 'Favor inserir os valores de Y.'
                confirmar.destroy()

            # Verifica se a quantidade de valores é a mesma nos campos 1 e 2
            elif len(get_texto()[1]) != len(get_texto()[2]):
                lbl_msg['text'] = 'Favor inserir a mesma quantidade de valores de X e Y.'
                confirmar.destroy()

            # Verifica se a quantidade de valores nos campos 1 e 2 é igual e se o campo 3 não está vazio
            elif len(get_texto()[1]) == len(get_texto()[2]) and len(get_texto()[2]) != 0:
                frame_princ.pack_forget()
                lbl_msg.pack_forget()
                frame_sec.pack()
                # lb_resp['text'] = mmq(get_texto()[0], get_texto()[1], get_texto()[2])
                plota_grafico(get_texto()[1], get_texto()[2])
                img_grafico['file'] = 'grafico.png'
                interface.geometry('640x480')
                confirmar.destroy()
        except:
            # Se houver algum erro não implementado pede para o usuário verificar os dados
            lbl_msg['text'] = 'Favor verificar os dados.'
            confirmar.destroy()

    # Cria a janela de confirmação dos dados
    confirmar = Toplevel()
    frame_confirmar = Frame(confirmar)
    msg = Label(frame_confirmar, text='Os dados inseridos estão corretos?', padx=20, pady=20).grid(column=0, row=0, columnspan=2)
    btn_confirma = Button(frame_confirmar, text='Confirmar', command=confirmado, padx=15).grid(column=0, row=1)
    btn_cancela = Button(frame_confirmar, text='Cancelar', command=confirmar.destroy, padx=15).grid(column=1, row=1)
    frame_confirmar.pack()
    # Define o tamanho e a posição da janela
    confirmar.geometry('300x100+175+200')

# Função para recolher os dados inseridos pelo usuario
def get_texto():
    # Salva o texto dos comapos 1 e 2 em variaveis
    texto_x = txtx.get(1.0, END).split('\n')
    texto_y = txty.get(1.0, END).split('\n')

    # Limpa o texto das vaiaveis ( tira possíveis espaços, tab's e linhas em branco)
    for c in range(texto_x.count('')):
        for i in texto_x:
            if i == '' or i == '\t':
                texto_x.pop(texto_x.index(i))
            elif '\t' in i:
                posicao = i.find('\t')
                i = i[:posicao]
    for c in range(texto_y.count('')):
        for i in texto_y:
            if i == '' or i == '\t':
                texto_y.pop(texto_y.index(i))
            elif '\t' in i:
                posicao = i.find('\t')
                i = i[:posicao]
    # Salva o valor do grau do polinômio a ser ajustado
    grau_poli = entrada_grau.get()

    return [0 if grau_poli == '' or grau_poli == ' ' else int(grau_poli), [float(x) for x in texto_x], [float(y) for y in texto_y]]

# Função para plotar o grafico
def plota_grafico(valores_x, valores_y):
    # Gera a função ajustada
    def f(x):
        res = 0
        eq = mmq(get_texto()[0], get_texto()[1], get_texto()[2], True).split('+')

        for i in range(len(eq)):
            if i == 0:
                res += float(eq[0])
            else:
                aux = eq[i].split('x')
                res += float(aux[0]) * (x ** int(aux[1][1:]))
        return res

    # Plota os valores experimentais
    plt.plot(valores_x, valores_y, linestyle=' ', marker='o', color='red')
    # Plota a função ajustada
    plt.plot(valores_x, [f(x) for x in valores_x], color='blue')
    plt.plot(valores_x[0], f(valores_x[0]), marker=' ', color='white')  # Go Horse!
    # plt.title('Gráfico X/Y')
    # plt.xlabel('Eixo X')
    # plt.ylabel('Eixo Y')
    plt.legend(['Pontos experimentais',
                f'F(x) = {mmq(get_texto()[0], get_texto()[1], get_texto()[2])}',
                f'R{sobrescrito(2)} = {r2(get_texto()[0], get_texto()[1], get_texto()[2])*100}%'])
    plt.savefig('grafico.png')


# Função para voltar para a primeira tela
def voltar():
    # Função para limpar os dados inseridos antes de voltar para a primeira tela
    def volta_limpa():
        # Apaga a segunda tela e cria a primeira novamente
        frame_sec.pack_forget()
        frame_princ.pack()
        lbl_msg.pack()

        # Limpa os campos 1, 2 e 3
        txtx.delete(1.0, 'end')
        txty.delete(1.0, 'end')
        entrada_grau.delete(0, 'end')

        # Fecha ajanela de confirmação
        volta.destroy()
        # Tenta abrir a imagem da UERJ
        try:
            with open('uerj.png'):
                pass
            interface.geometry('400x276+100+100')
            # Se consegue cria a janela principal de um tamanho
        except:
            interface.geometry('270x292+100+100')
            # Se não consegue cria a jenela principal de um tamanho diferente

    # Função para voltar a primeira tela mantendo os dados inseridos
    def volta_mantem():
        # Apaga a segunda tela e cria a primeira novamente
        frame_sec.pack_forget()
        frame_princ.pack()
        lbl_msg.pack()
        # Fecha a janela de confirmação
        volta.destroy()
        # Tenta abrir a imagem da UERJ
        try:
            with open('uerj.png'):
                pass
            interface.geometry('400x276+100+100')
            # Se consegue cria a janela principal de um tamanho
        except:
            interface.geometry('270x292+100+100')
            # Se não consegue cria a jenela principal de um tamanho diferente

    # Cria uma janela de confirmação
    volta = Toplevel()

    frame_volta = Frame(volta)
    lbl_volta = Label(frame_volta, text='Deseja apagar os pontos?', padx=20, pady=20).grid(column=0, row=0, columnspan=2)
    btn_sim = Button(frame_volta, text='Sim', command=volta_limpa, padx=20).grid(column=0, row=1)
    btn_nao = Button(frame_volta, text='Não', command=volta_mantem, padx=20).grid(column=1, row=1)
    frame_volta.pack()

    # Define o tamanho e a posição da janela de confirmação
    volta.geometry('300x100+270+290')

# Função que salva o gráfico
def salvar():
    def salva():
        # Renomea o gráfico
        rename('grafico.png', f'{nome_salva.get()}.png')
        # Fecha a janela
        salvar.destroy()

    # Cria uma janela para dar um nome ao gráfico
    salvar = Toplevel()
    frame_salva = Frame(salvar)
    lbl_salva = Label(frame_salva, text='Nome', padx=20).grid(column=0, row=0, pady=20)
    nome_salva = Entry(frame_salva).grid(column=1, row=0, pady=20)
    btn_salva = Button(frame_salva, text='Salvar', command=salva, padx=20).grid(column=0, row=1, columnspan=2)
    frame_salva.pack()

    # Define o tamanho da janela criada
    salvar.geometry('300x100+270+290')

# Função para apagar o gráfico toda vez que o programa é fechado
def apaga_grafico():
    try:
        # Tenta remover o gráfico
        remove('grafico.png')
    except FileNotFoundError:
        # Se ja houver sido apagado mostra uma mensagem para o usuário
        print('O gráfico já foi excluido.')

    # Fecha a janela principal
    interface.destroy()

# Cria a janela principal
interface = Tk()

# PRIMEIRA TELA
frame_princ = Frame(interface)

# Cria uma caixa para o primeiro campo de texto
frame_x = Frame(frame_princ)
lbx = Label(frame_x, text='Insira os valores de X:')
txtx = Text(frame_x, height=10, width=10)

# Cria uma caixa para o segundo campo de texto
frame_y = Frame(frame_princ)
lby = Label(frame_y, text='Insira os valores de Y:')
txty = Text(frame_y, height=10, width=10)

# Cria uma caixa para o terceiro campo de texto
frame_grau = Frame(frame_princ)
lb_frame = Label(frame_grau, text='Insira o maior grau do polinomio:')
entrada_grau = Entry(frame_grau)

# Cria um botão para confirmar os dados inseridos
btn_confirmar = Button(frame_princ, text='Confirmar', command=confirma, padx=15)

# Cria um rodapé para mensagens de erro
lbl_msg = Label(interface, text='', bg='white')

# Coloca a imagem da UERJ à direita da janela
try:
    fundo = PhotoImage(file='uerj.png').subsample(2, 2)
    lbl_fundo = Label(frame_princ, image=fundo).grid(column=2, row=0, sticky='e')
    btn_confirmar.grid(column=2, row=2)
    interface.geometry('400x276+100+100')
    lbl_msg['width'] = 57
    frame_grau['pady'] = 15
except:
    print('Está faltando a imagem da UERJ')
    btn_confirmar.grid(column=0, row=3, columnspan=2, pady=10)
    lbl_msg['width'] = 38
    interface.geometry('270x292+100+100')

# Faz a primeira tela aparecer
frame_princ.pack()

# Faz a caixa do primeiro campo aparecer
frame_x.grid(column=0, row=0)
lbx.pack()
txtx.pack()

# Faz a caixa do segundo campo aparecer
frame_y.grid(column=1, row=0)
lby.pack()
txty.pack()

# Faz a caixa do terceiro campo aparecer
frame_grau.grid(column=0, row=2, columnspan=2)
lb_frame.pack()
entrada_grau.pack()

# Faz a caixa de texto de erro aparecer
lbl_msg.pack()

# SEGUNDA TELA
frame_sec = Frame(interface)
img_grafico = PhotoImage(file='')
grafico = Label(frame_sec, image=img_grafico)
btn_voltar = Button(frame_sec, text='Voltar', command=voltar, padx=20)
btn_salvar = Button(frame_sec, text='Salvar gráfico', command=salvar, padx=20)

grafico.pack()
btn_voltar.place(x=10, y=10)
btn_salvar.place(x=100, y=10)

# ---------------------------

interface.title('Método dos Minimos Quadrados')
interface.protocol('WM_DELETE_WINDOW', apaga_grafico)
interface.mainloop()


