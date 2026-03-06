import requests
import yaml
import os 
import json

def load_settings(path="config/settings.yaml"): 
    with open(path, "r") as file:
        return yaml.safe_load(file)

def fetch_bacen_series(base_url, series_id, start_date=None, end_date=None, timeout=60):
    """
    Busca uma série específica do SGS (BANCO CENTRAL).
    """

    # Monta a URL dinâmicamente com o ID
    url = f"{base_url}.{series_id}/dados"

    # Parâmetros da API
    params = {
        "formato": "json"
    }

    headers = {
        "Accept": "application/json"
    }
    if start_date:
        params["dataInicial"] = start_date
    if end_date:
        params["dataFinal"] = end_date

    response = requests.get(url, params=params, headers=headers, timeout=timeout)
    response.raise_for_status() #lança o erro se falhar

    # Verifica se veio conteúdo
    if not response.text:
        print(f"Resposta vazia para série {series_id}")
        return []
    
    try:
        return response.json()
    except Exception as e: 
        print(f"Erro ao converter JSON da série {series_id}")
        print(response.text)
        return []

def fetch_all_bacen_series(settings):
    """
    Percorre todas as séries configuradas no settings.yaml
    e retorna um dicionário com os dados.
    """

    base_url = settings["api"]["base_url"]
    timeout = settings["api"]["timeout"]

    start_date = settings["analysis"]["start_date"]
    end_date = settings["analysis"]["end_date"]

    raw_path = settings["paths"]["raw_data"]
    save_raw = settings["features"]["save_raw"]

    series = settings["bacen_series"]

    all_data = {}

    for name, series_id in series.items():
        print(f"Buscando série: {name} ({series_id})")

        data = fetch_bacen_series(
            base_url=base_url,
            series_id=series_id,
            start_date=start_date,
            end_date=end_date,
            timeout=timeout,
        )
        if not data:
            print(f"Nenhum dado retornado para {name}")
            continue

        all_data[name] = data

        if save_raw:
            save_raw_data(data, name, raw_path)

    return all_data

def save_raw_data(data, series_name, raw_path):
    """
    Salva os dados brutos em JSON dentro da pasta data/raw/
    """
    os.makedirs(raw_path, exist_ok=True)

    file_path = os.path.join(raw_path, f"{series_name}.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Arquivo salvo em: {file_path}")
