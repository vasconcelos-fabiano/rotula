import os

def menu_configuracoes(configuracoes):
    configuracoes  # Acesso à variável global configuracoes
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
            try:
                nova_velocidade = input(f"Defina a velocidade da impressão (1 a 14) [atual: {configuracoes['velocidade']}]: ")
                configuracoes["velocidade"] = int(nova_velocidade) if nova_velocidade else configuracoes["velocidade"]

                nova_aceleracao = input(f"Defina a aceleração do motor (1 a 30) [atual: {configuracoes['aceleracao']}]: ")
                configuracoes["aceleracao"] = int(nova_aceleracao) if nova_aceleracao else configuracoes["aceleracao"]

                nova_desaceleracao = input(f"Defina a desaceleração do motor (1 a 30) [atual: {configuracoes['desaceleracao']}]: ")
                configuracoes["desaceleracao"] = int(nova_desaceleracao) if nova_desaceleracao else configuracoes["desaceleracao"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif escolha == '1':
            try:
                nova_largura = input(f"Defina a largura da etiqueta em mm [atual: {configuracoes['largura_etiqueta']}]: ")
                configuracoes["largura_etiqueta"] = int(nova_largura) if nova_largura else configuracoes["largura_etiqueta"]

                nova_altura = input(f"Defina a altura da etiqueta em mm [atual: {configuracoes['altura_etiqueta']}]: ")
                configuracoes["altura_etiqueta"] = int(nova_altura) if nova_altura else configuracoes["altura_etiqueta"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif escolha == '2':
            try:
                nova_posicao_x_logo = input(f"Defina o eixo X da logo [atual: {configuracoes['eixo_logo_x']}]: ")
                configuracoes["eixo_logo_x"] = int(nova_posicao_x_logo) if nova_posicao_x_logo else configuracoes["eixo_logo_x"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif escolha == '3':
            try:
                nova_posicao_y_logo = input(f"Defina o eixo Y da logo [atual: {configuracoes['eixo_logo_y']}]: ")
                configuracoes["eixo_logo_y"] = int(nova_posicao_y_logo) if nova_posicao_y_logo else configuracoes["eixo_logo_y"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif escolha == '4':
            try:
                nova_posicao_x_saborita = input(f"Defina o eixo X da saborita_info [atual: {configuracoes['eixo_saborita_x']}]: ")
                configuracoes["eixo_saborita_x"] = int(nova_posicao_x_saborita) if nova_posicao_x_saborita else configuracoes["eixo_saborita_x"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif escolha == '5':
            try:
                nova_posicao_y_saborita = input(f"Defina o eixo Y da saborita_info [atual: {configuracoes['eixo_saborita_y']}]: ")
                configuracoes["eixo_saborita_y"] = int(nova_posicao_y_saborita) if nova_posicao_y_saborita else configuracoes["eixo_saborita_y"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif escolha == '6':
            try:
                nova_posicao_x_data = input(f"Defina o eixo X da data de fabricação [atual: {configuracoes['eixo_data_x']}]: ")
                configuracoes["eixo_data_x"] = int(nova_posicao_x_data) if nova_posicao_x_data else configuracoes["eixo_data_x"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif escolha == '7':
            try:
                nova_posicao_y_data = input(f"Defina o eixo Y da data de fabricação [atual: {configuracoes['eixo_data_y']}]: ")
                configuracoes["eixo_data_y"] = int(nova_posicao_y_data) if nova_posicao_y_data else configuracoes["eixo_data_y"]

            except ValueError:
                print("Entrada inválida. Use apenas números.")
        else:
            print("Opção inválida. Escolha entre 0, 1, 2, 3, 4, 5, 6, 7 ou A.")

    return configuracoes
