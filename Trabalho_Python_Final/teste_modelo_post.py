
import json
import requests

# URL da rota que recebe os dados para previsão de radiação solar
url = "http://127.0.0.1:5000/solar"

# Abre o arquivo JSON e lê seu conteúdo
with open('./dataset_solar.json', 'r', encoding='utf-8') as json_file:
    # Carrega os dados do arquivo JSON
    json_body = json.load(json_file.read())

# Define os cabeçalhos para a requisição HTTP
headers = {'Content-Type': 'application/json'}

try:
    # Envia uma requisição POST para a rota '/solar' com os dados do arquivo JSON
    response = requests.post(url, json=json_body, headers=headers, timeout=3)

    # Verifica o código de status da resposta
    if response.status_code == 200:
        # Se a resposta for bem-sucedida (código 200), extrai os dados da resposta JSON
        data = response.json()
        print(data)
    else:
        # Se houver um erro no lado do servidor, imprime o código de status
        print("Error", response.status_code)
except requests.exceptions.RequestException as e:
    # Trata exceções relacionadas a erros de requisição
    print("Request error:", e)
