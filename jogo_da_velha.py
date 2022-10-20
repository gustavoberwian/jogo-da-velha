def menu():
    continuar = 1
    while continuar:
        continuar = int(input("0. Sair \n" +
                              "1. Jogar novamente\n"))
        if continuar:
            escolha = 0
            while not escolha:
                escolha = int(input("Escolha qual jogar \n" +
                                    "1. X \n" +
                                    "2. O\n"))
            JogoDaVelha(escolha)
        else:
            print("Saindo...")


def JogoDaVelha(escolha):
    tabuleiro = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    acabou = False
    QuadradoMagico = [4, 9, 2, 3, 5, 7, 8, 1, 6]

    def ImprimirTabuleiro():
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                print('|', tabuleiro[i][j], '|', end="")
            print()
            print("|---+----+----|")

    def PegarNumero():
        while True:
            numero = input()
            try:
                numero = int(numero)
                if numero in range(1, 10):
                    return numero
                else:
                    print("\nNúmero não está no tabuleiro.")
            except ValueError:
                print("\nIsso não é um número. Tente novamente.")
                continue

    def Turno(jogador):
        espaco_colocado = PegarNumero()

        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                if espaco_colocado == tabuleiro[i][j]:
                    print(tabuleiro[i][j])
                    if tabuleiro[i][j] == "X" or tabuleiro[i][j] == "O":
                        print("\nEspaço já ocupado. Tente colocar em outro.")
                        Turno(jogador)
                    else:
                        tabuleiro[i][j] = jogador

    def ChecaVitoria(jogador):
        jogadas = 0

        # checando linhas
        for i in range(3):
            if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
                print("Jogador", jogador, "ganhou!\n")
                return True

        # checando colunas
        for i in range(3):
            if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
                print("Jogador", jogador, "ganhou!\n")
                return True

        # checando diagonais
        diagonal = False
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            diagonal = True
        elif tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
            diagonal = True

        if diagonal:
            print("Jogador", jogador, "ganhou!\n")
            return True

        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                if tabuleiro[i][j] == "X" or tabuleiro[i][j] == "O":
                    jogadas += 1
                if jogadas == 9:
                    print("O jogo acabou em um empate\n")
                    return True

    while not acabou:
        if escolha == 2:
            ImprimirTabuleiro()
            acabou = ChecaVitoria("X")
            if acabou:
                break
            print("Jogador O, escolha um espaço.")
            Turno("O")

            acabou = ChecaVitoria("O")
            if acabou:
                break
            print("Jogador X, escolha um espaço.")
            Turno("X")
        elif escolha == 1:
            ImprimirTabuleiro()
            acabou = ChecaVitoria("O")
            if acabou:
                break
            print("Jogador X, escolha um espaço.")
            Turno("X")

            ImprimirTabuleiro()
            acabou = ChecaVitoria("X")
            if acabou:
                break
            print("Jogador O, escolha um espaço.")
            Turno("O")


menu()
