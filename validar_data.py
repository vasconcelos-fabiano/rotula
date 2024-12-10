from datetime import datetime, timedelta

def validar_data(data):
    # Verifica se a data tem exatamente 6 caracteres numéricos
    if not data.isdigit() or len(data) != 6:
        print("Data inválida: a data deve estar no formato DDMMAA e conter apenas números.")
        return False

    try:
        dia = int(data[:2])
        mes = int(data[2:4])
        ano = int(data[4:6]) + 2000  # Considera apenas anos de 2000 a 2099

        # Tenta criar um objeto de data para validar sua existência
        data_fabricacao = datetime(year=ano, month=mes, day=dia)
    except ValueError:
        print("Data inválida: a data fornecida não existe.")
        return False

    # Verifica restrições específicas de mês e ano
    if ano < 2024 or (ano == 2024 and mes < 12):
        print("Data inválida: a data deve ser igual ou posterior a dezembro de 2024.")
        return False

    # Data de hoje e limites
    hoje = datetime.now()
    max_dias_futuro = hoje + timedelta(days=5)

    # Verifica se a data é no futuro além de 5 dias
    if data_fabricacao > max_dias_futuro:
        print("Data inválida: a data de fabricação não pode ser superior a 5 dias a partir de hoje.")
        return False

    # Alerta para datas futuras dentro do intervalo permitido
    if data_fabricacao > hoje:
        while True:
            print("\n######################### A V I S O #########################\n")
            print("A data fornecida está NO FUTURO!")
            print("A Saborita não pode ter sido fabricada nessa data ainda!")
            escolha = input(f"Você errou a data e deseja corrigir? (A)bortar | (E)rrei a data | (C)onfirmar essa data mesmo ({data_fabricacao.strftime('%d/%m/%Y')}): ").strip().upper()
            
            if escolha == "E":
                print("Por favor, insira a data novamente.")
                return False
            elif escolha == "C":
                print("Data confirmada mesmo com o aviso.")
                break
            elif escolha == "A":
                print("Abortando a impressão! Saindo...")
                return None  # Indica um aborto explícito
            else:
                print("Opção inválida. Escolha 'E', 'C' ou 'A'.")

    return data_fabricacao.strftime('%d/%m/%y')  # Retorna a data válida
