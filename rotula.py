#!/usr/bin/env python3

from datetime import datetime
import os
from validar_data import validar_data  # Importa a função de validar_data.py

# Exibe o menu inicial
os.system('clear')
print("="*37)
print("***** Seja bem-vindo ao Rotula! *****")
print("="*37)

# Função para obter a data de fabricação
def obter_data_fabricacao():
    # Obtém a data de hoje formatada como DDMMAA
    data_hoje = datetime.now().strftime("%d%m%y")
    data_formatada = datetime.now().strftime("%d/%m/%Y")  # Para exibição no prompt

    while True:
        # Mostra a data padrão no prompt
        data_usuario = input(f"Digite a data de fabricação DDMMAA - [ENTER] para hoje ({data_formatada}): ").strip()

        # Se o usuário não digitar nada, usamos a data de hoje
        if not data_usuario:
            data_usuario = data_hoje

        # Valida a data fornecida
        if validar_data(data_usuario):
            # Retorna a data válida formatada no padrão DD/MM/AA
            return f"{data_usuario[:2]}/{data_usuario[2:4]}/{data_usuario[4:6]}"


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
        print("Você escolheu configurações. Função a ser implementada...")
        break  # Sai do loop caso o usuário escolha "C"
    
    else:
        print("Opção inválida. Por favor, escolha (I), (C) ou (A).")