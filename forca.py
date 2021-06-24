import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            verifica_chute(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print(chute)
        enforcou = erros == 8
        acertou = ('_' not in letras_acertadas)
        print(letras_acertadas)
    if acertou:
        print('parabens você acertou todas as letras')
        imprime_mensagem_vencedor()
    else:
        print(f'você esgotou as tentativas a palavra secreta era: {palavra_secreta}')
        imprime_mensagem_perdedor(palavra_secreta)


print('Fim do jogo')


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    palavra = open('palavra.txt', 'r')
    palavras = []

    with open('palavra.txt') as palavra:
        for linha in palavra:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def pede_chute():
    chute = input('digite uma letra')
    chute = chute.strip().upper()
    return chute


def verifica_chute(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[i] = letra
        i = i + 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if __name__ == "__main__":
    jogar()
