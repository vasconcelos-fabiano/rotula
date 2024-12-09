import os

# Carregar configurações padrões
configuracoes = {
    "velocidade": 2,
    "aceleracao": 10,
    "desaceleracao": 2,
    "largura_etiqueta": 104,
    "altura_etiqueta": 70,
    "eixo_logo_x": 417,
    "eixo_logo_y": 7,
    "eixo_saborita_x": 5,
    "eixo_saborita_y": 17,
    "eixo_data_x": 5,
    "eixo_data_y": 25,
}

def menu_configuracoes():
    """
    Exibe o menu de configurações e permite ao usuário alterar valores.
    """
    while True:
        os.system('clear')
        print("=" * 37)
        print("***** Menu de Configurações *****")
        print("=" * 37)
        print()
        print("O que você quer configurar?")
        print("0. Velocidade de impressão/Aceleração do motor")
        print("1. Largura/Altura da etiqueta")
        print("2. Eixo X da logo")
        print("3. Eixo Y da logo")
        print("4. Eixo X da saborita_info")
        print("5. Eixo Y da saborita_info")
        print("6. Eixo X da data de fabricação")
        print("7. Eixo Y da data de fabricação")
        print("A. Abortar")

        escolha = input("\nSua escolha: ").strip().upper()
        if escolha == 'A':
            print("Abortando configurações. Retornando...")
            break
        elif escolha == '0':
            configuracoes["velocidade"] = int(input("Defina a velocidade da impressão (1 a 14) [ENTER] para padrão 2: ") or 2)
            configuracoes["aceleracao"] = int(input("Defina a aceleração do motor (1 a 30) [ENTER] para padrão 10: ") or 10)
            configuracoes["desaceleracao"] = int(input("Defina a desaceleração do motor (1 a 30) [ENTER] para padrão 2: ") or 2)
        elif escolha == '1':
            largura = input("Defina a largura da etiqueta em mm (ENTER para 104): ")
            altura = input("Defina a altura da etiqueta em mm (ENTER para 70): ")
            configuracoes["largura_etiqueta"] = int(largura) if largura else configuracoes["largura_etiqueta"]
            configuracoes["altura_etiqueta"] = int(altura) if altura else configuracoes["altura_etiqueta"]
        elif escolha in ['2', '3', '4', '5', '6', '7']:
            eixo = "logo" if opcao in ['4', '5'] else "saborita" if opcao in ['6', '7'] else "data"
            eixo_campo = f"eixo_{eixo}_x" if opcao in ['4', '6', '8'] else f"eixo_{eixo}_y"
            valor = input(f"Defina o valor do {eixo_campo.replace('_', ' ')} (ENTER para {configuracoes[eixo_campo]}): ")
            configuracoes[eixo_campo] = int(valor) if valor else configuracoes[eixo_campo]
        else:
            print("Opção inválida. Tente novamente.")

    return configuracoes
