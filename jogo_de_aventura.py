# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas

# Eu quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

# Qual é o cenário : Eu estou numa guerra entre duas nações, e nós temos 2 lados: LadoA e LadoB. Somente o ladoA irá vencer, e o ladoB irá perder! então eu tenho que tomar as decisões corretas para chegar até a vitória, que somente o ladoA irá conseguir!
import PySimpleGUI as sg
class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte eu ou sul? (n/s)' # norte = LadoA, sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' # espada = Lado1, escudo = Lado2
        self.pergunta3 = 'Qual é a sua especialidade?(linha de frente/tatico)' # linha de frente = Lado1, tático = Lado2
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'

        
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        # criar a janela
        self.janela = sg.Window('Jogo de Aventura!',layout=layout)
        while True:
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)
        
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()