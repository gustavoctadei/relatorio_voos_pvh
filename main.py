import requests
import json
import datetime_util as DateTimeUtil

url = "https://www.portovelho-airport.com.br/pt-br/api/flights"

payload_partidas = "voo_type=departure"
payload_chegadas = "voo_type=arrivals"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "pt-BR,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.portovelho-airport.com.br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.portovelho-airport.com.br/",
    "Cookie": "__goc_session__=scozvaoblvcngohqcelbyemlpceuruqq; has_js=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0"
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