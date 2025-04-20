import requests
import pandas as pd
import time

# === CONFIGURAÇÕES ===
USERNAME = 'ArthurM0tta'         # Seu e-mail usado no Octoparse
PASSWORD = '0405tuco'              # Senha criada nas configurações da conta
TASK_ID = '128368a9-e041-80f0-659f-1988f747de4f'            # ID da tarefa no Octoparse
START_TASK = True                       # Define se você quer iniciar a tarefa antes de buscar os dados
WAIT_TIME = 60                          # Tempo (segundos) para esperar os dados serem coletados após iniciar a tarefa

# === 1. AUTENTICAÇÃO ===
def obter_token(username, password):
    url = 'https://dataapi.octoparse.com/token'
    payload = {
        'username': username,
        'password': password
    }
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        print("Erro ao autenticar:")
        print("Status:", res.status_code)
        print("Resposta:", res.text)
        raise Exception("Falha na autenticação")

    return res.json()['token']

# === 2. INICIAR A TAREFA (opcional) ===
def iniciar_tarefa(task_id, token):
    url = f'https://dataapi.octoparse.com/api/task/start/{task_id}'
    headers = {'Authorization': f'bearer {token}'}
    res = requests.post(url, headers=headers)
    res.raise_for_status()
    print("Tarefa iniciada com sucesso.")

# === 3. BUSCAR DADOS DA TAREFA ===
def buscar_dados(task_id, token, page=1, page_size=100):
    url = f'https://dataapi.octoparse.com/api/alldata/{task_id}?pageIndex={page}&pageSize={page_size}'
    headers = {'Authorization': f'bearer {token}'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()['data']

# === 4. CONVERTER PARA DATAFRAME ===
def dados_para_dataframe(dados):
    return pd.json_normalize(dados)

# === FLUXO COMPLETO ===
def coletar_dados_octoparse():
    print("Autenticando...")
    token = obter_token(USERNAME, PASSWORD)

    if START_TASK:
        print("Iniciando tarefa...")
        iniciar_tarefa(TASK_ID, token)
        print(f"Aguardando {WAIT_TIME} segundos para coleta dos dados...")
        time.sleep(WAIT_TIME)

    print("Buscando dados...")
    dados = buscar_dados(TASK_ID, token)
    df = dados_para_dataframe(dados)
    return df

# === EXECUÇÃO ===
if __name__ == "__main__":
    df = coletar_dados_octoparse()
    print("Dados coletados com sucesso!\n")
    print(df.head())  # Mostra as primeiras linhas
