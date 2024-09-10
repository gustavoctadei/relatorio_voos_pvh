from datetime import datetime

def data_hora():
    agora = datetime.now()
    data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
    return data_hora_formatada