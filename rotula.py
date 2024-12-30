#!/usr/bin/env python3

from datetime import datetime
import subprocess
import os
from validar_data import validar_data  # Importa a função de validar_data.py
from rotula_config import menu_configuracoes  # Importa o menu de configurações

# Dicionário de configurações padrão
configuracoes = {
    "velocidade": 10,
    "aceleracao": 15,
    "desaceleracao": 15,
    "largura_etiqueta": 50,
    "altura_etiqueta": 70,
    "eixo_logo_x": 0,
    "eixo_logo_y": 0,
    "eixo_saborita_x": 0,
    "eixo_saborita_y": 0,
    "eixo_data_x": 0,
    "eixo_data_y": 0,
}

# Exibe o menu inicial
os.system("clear")
print("\033[43m\033[30m\033[1m=" * 37)
print("***** Seja bem-vindo ao Rotula! *****")
print("=" * 37)
print("\033[0m")

import subprocess

def iniciar_cups():
    try:
        # Executa o comando para iniciar o serviço CUPS
        resultado = subprocess.run(
            ["sudo", "systemctl", "start", "cups"],
            check=True,  # Lança uma exceção se o comando falhar
            text=True,  # Trata entrada/saída como strings
        )
        print("\033[7m[ CUPS iniciado com sucesso! ]\033[0m\n")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o CUPS: {e}")

# Função para obter a data de fabricação
def obter_data_fabricacao():
    data_hoje = datetime.now().strftime("%d%m%y")
    data_formatada = datetime.now().strftime("%d/%m/%Y")  # Para exibição no prompt

    while True:
        data_usuario = input(
            f"Digite a data de fabricação DDMMAA - [ENTER] para hoje ({data_formatada}): "
        ).strip()
        if not data_usuario:
            data_usuario = data_hoje

        data_validada = validar_data(data_usuario)
        if data_validada is None:  # Aborto explícito
            exit()  # Encerra o programa ou retorna ao menu principal
        elif data_validada:  # Data validada e confirmada
            return data_validada  # Já está formatada na função validar_data

# Função para abortar
def aborta():
    print("Abortando operação. Saindo...")

# Função para imprimir
def imprime(repeticoes, label):
    label = label.lower()
    print(f"\nImprimindo {repeticoes} cópias do rótulo {label} escolhido...\n")
    for i in range(repeticoes):
        comando_shell = f"lp -d ZD220 -o raw label\\ {label}.gpl"
        subprocess.run(comando_shell, shell=True)

iniciar_cups()

# Loop principal
while True:
    escolha = (
        input(
            "Quer imprimir ou entrar nas configurações? (I)mprimir, (C)onfigurações ou (A)bortar: "
        )
        .strip()
        .upper()
    )

    if escolha == "A":
        aborta()
        break

    elif escolha == "I":
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
            if saborita in ["1", "2", "3", "4", "5", "6", "7"]:
                nomes = [
                    "Firenze",
                    "Lisboa",
                    "Lima",
                    "Vancouver",
                    "Amontada",
                    "Xangai",
                    "Barcelona",
                ]
                saborita_nome = nomes[int(saborita) - 1]
                print(f"\nVocê escolheu imprimir o rótulo da Saborita {saborita_nome}.")
                break
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 7.")

        # Pergunta o número de cópias
        while True:
            resposta = input(
                f"Quantas cópias você quer imprimir do rótulo da Saborita {saborita_nome}? "
            ).strip()
            if resposta.isdigit() and int(resposta) > 0:
                repeticoes = int(resposta)
                print(f"Você escolheu imprimir {repeticoes} cópias.")
                break
            else:
                print("Entrada inválida. Digite um número maior que zero.")

        # Chama a função de obter data de fabricação
        data_fabricacao = obter_data_fabricacao()
        print(f"Data de fabricação escolhida: {data_fabricacao}")

        imprime(repeticoes, saborita_nome)
        break  # Sai do loop caso o usuário tenha feito a escolha da Saborita

    elif escolha == "C":
        configuracoes = menu_configuracoes(configuracoes)
        salvar_configuracoes(configuracoes)
        print("Configurações atualizadas:", configuracoes)

    else:
        print("Opção inválida. Por favor, escolha (I), (C) ou (A).")
