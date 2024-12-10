#!/usr/bin/env python3

from datetime import datetime
import os
from validar_data import validar_data  # Importa a função de validar_data.py
from rotula_config import menu_configuracoes  # Importa o menu de configurações

configuracoes = {
    "velocidade": 10,  # valor padrão para a velocidade
    "aceleracao": 15,   # valor padrão para aceleração
    "desaceleracao": 15, # valor padrão para desaceleração
    "largura_etiqueta": 50,  # valor padrão para a largura da etiqueta
    "altura_etiqueta": 70,   # valor padrão para a altura da etiqueta
    "eixo_logo_x": 0,    # valor inicial para eixo logo X
    "eixo_logo_y": 0,    # valor inicial para eixo logo Y
    "eixo_saborita_x": 0,  # valor inicial para eixo saborita X
    "eixo_saborita_y": 0,  # valor inicial para eixo saborita Y
    "eixo_data_x": 0,    # valor inicial para eixo data X
    "eixo_data_y": 0     # valor inicial para eixo data Y
}

# Exibe o menu inicial
os.system('clear')
print("="*37)
print("***** Seja bem-vindo ao Rotula! *****")
print("="*37)

# Função para obter a data de fabricação
def obter_data_fabricacao():
    data_hoje = datetime.now().strftime("%d%m%y")
    data_formatada = datetime.now().strftime("%d/%m/%Y")  # Para exibição no prompt

    while True:
        data_usuario = input(f"Digite a data de fabricação DDMMAA - [ENTER] para hoje ({data_formatada}): ").strip()
        if not data_usuario:
            data_usuario = data_hoje

        data_validada = validar_data(data_usuario)
        if data_validada is None:  # Aborto explícito
            exit()  # Encerra o programa ou retorna ao menu principal
        elif data_validada:  # Data validada e confirmada
            return data_validada  # Já está formatada na função validar_data
        
# Loop principal
while True:
    escolha = input("Quer imprimir ou entrar nas configurações? (I)mprimir, (C)onfigurações ou (A)bortar: ").strip().upper()

    if escolha == 'A':
        print("Abortando impressão. Saindo...")
        break  # Sai do loop caso o usuário escolha "A"

    elif escolha == 'I':
        # Menu de Saborita
        print("\nQual rótulo você quer imprimir?")
        print("1. Firenze")
        print("2. Lisboa")
        print("3. Lima")
        print("4. Vancouver")
        print("5. Amontada")
        print("6. Xangai")
        print("7. Barcelona")

        while True:
            saborita = input("\nSua escolha: ").strip()

            if saborita in ['1', '2', '3', '4', '5', '6', '7']:
                nomes = ["Firenze", "Lisboa", "Lima", "Vancouver", "Amontada", "Xangai", "Barcelona"]
                saborita_nome = nomes[int(saborita) - 1]
                print(f"\nVocê escolheu imprimir o rótulo da Saborita {saborita_nome}.")
                break
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 7.")

        # Chama a função de obter data de fabricação
        data_fabricacao = obter_data_fabricacao()
        print(f"Data de fabricação escolhida: {data_fabricacao}")
        
        # Continuar com o processo de impressão aqui

        break  # Sai do loop caso o usuário tenha feito a escolha da Saborita

    elif escolha == 'C':
        configuracoes = menu_configuracoes(configuracoes)
        print("Configurações atualizadas:", configuracoes)

    else:
        print("Opção inválida. Por favor, escolha (I), (C) ou (A).")