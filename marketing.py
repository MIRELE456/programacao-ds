def calcular_engajamento():
    print("Calculadora de Engajamento em Redes Sociais")
    
    curtidas = int(input("Digite o número de curtidas: "))
    comentarios = int(input("Digite o número de comentários: "))
    compartilhamentos = int(input("Digite o número de compartilhamentos: "))
    
    seguidores = int(input("Digite o número de seguidores: "))
    alcance = int(input("Digite o alcance da publicação: "))
    impressoes = int(input("Digite o número de impressões da publicação: "))

    # Cálculo das métricas de engajamento
    engajamento_seguidores = (curtidas + comentarios + compartilhamentos) / seguidores * 100 if seguidores != 0 else 0
    engajamento_alcance = (curtidas + comentarios + compartilhamentos) / alcance * 100 if alcance != 0 else 0
    engajamento_impressoes = (curtidas + comentarios + compartilhamentos) / impressoes * 100 if impressoes != 0 else 0

    # Exibindo os resultados
    print("\nResultados do Engajamento:")
    print(f"Engajamento por seguidores: {engajamento_seguidores:.2f}%")
    print(f"Engajamento por alcance: {engajamento_alcance:.2f}%")
    print(f"Engajamento por impressões: {engajamento_impressoes:.2f}%")

# Executa o programa
calcular_engajamento()
