import requests
import json
import datetime_util as DateTimeUtil

url = "https://www.portovelho-airport.com.br/pt-br/api/flights"

payload_partidas = "voo_type=departure"
payload_chegadas = "voo_type=arrivals"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.portovelho-airport.com.br",
    "Connection": "keep-alive",
    "Referer": "https://www.portovelho-airport.com.br/",
}

response = requests.request("POST", url, data=payload_chegadas, headers=headers)
resp = json.loads(response.text)
chegadas = resp["data"]["voos"]["voo"]

response = requests.request("POST", url, data=payload_partidas, headers=headers)
resp = json.loads(response.text)
partidas = resp["data"]["voos"]["voo"]

voos = chegadas + partidas

relatorio = ""
data_hora = DateTimeUtil.data_hora()
relatorio = f"##### Consulta realizada em: {data_hora} #####\n\n"

for voo in voos:
    numero = voo["numero"]
    tipo = voo["tipo"]
    data_hora_prevista = voo["dataHoraPrevista"]
    data_hora_efetiva = voo["dataHoraEfetiva"]
    status = voo["observacao"]

    relatorio_voo = numero + " - " + tipo + " - Previsto: " + data_hora_prevista + " - Data Hora Efetiva: " + data_hora_efetiva + " - Status: " + status + "\n"

    relatorio = relatorio + relatorio_voo

relatorio = relatorio + "\n"

with open("relatorio.txt", 'a') as arquivo:
    arquivo.write(relatorio)