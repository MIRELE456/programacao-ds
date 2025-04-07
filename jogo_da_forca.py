# Palavra secreta e configurações iniciais
palavra_secreta = "girafa".lower()
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6
partes_do_corpo = [
    " O ",      # Cabeça
    " O \n |",  # Corpo
    " O \n/|",  # Braço esquerdo
    " O \n/|\\",# Braço direito
    " O \n/|\\\n/", # Perna esquerda
    " O \n/|\\\n/ \\" # Perna direita
]

# Função para mostrar o estado da forca
def mostrar_forca(erros):
    print("\n----")
    print("|   |")
    if erros > 0:
        print("|  ", partes_do_corpo[erros - 1])
    else:
        print("|")
    print("|\n|\n-----")

# Jogo
while tentativas > 0 and "_" in letras_acertadas:
    mostrar_forca(6 - tentativas)
    print(" ".join(letras_acertadas))
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra_secreta and len(palpite) == 1:
        # Usando index() e replace()
        for index, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[index] = letra
        print("\nBoa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print(f"\nErrou! Você tem {tentativas} tentativas restantes.")

# Verificação de vitória ou derrota
if "_" not in letras_acertadas:
    print("\nParabéns, você ganhou! A palavra era:", palavra_secreta.upper())
else:
    mostrar_forca(6)
    print("\nQue pena, você perdeu. A palavra era:", palavra_secreta.upper())
