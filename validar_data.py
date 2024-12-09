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

    # Data de hoje e limites
    hoje = datetime.now()
    max_dias_futuro = hoje + timedelta(days=5)

    # Verifica se a data é no futuro além de 5 dias
    if data_fabricacao > max_dias_futuro:
        print("Data inválida: a data de fabricação não pode ser superior a 5 dias a partir de hoje.")
        return False

    # Alerta para datas futuras dentro do intervalo permitido
    if data_fabricacao > hoje:
        print("Aviso: a data fornecida está no futuro. A Saborita não pode ter sido fabricada nessa data ainda.")

    return True
