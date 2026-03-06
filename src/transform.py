import pandas as pd
import json 
from pathlib import Path 

RAW_PATH = Path("data/raw")
CLEAN_PATH = Path("data/clean")

def transform_json_to_parquet():
    CLEAN_PATH.mkdir(parents=True, exist_ok=True)
    files = RAW_PATH.glob("*.json")

    for file in files:

        name_serie = file.stem 
        print(f"Transformando: {name_serie}")

        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        df = pd.DataFrame(data)

        # Verifica colunas esperadas 
        if "data" not in df.columns or "valor" not in df.columns:
            print(f"Estrutura inesperada em {name_serie}")
            print(df.head())
            continue

        # Converter data
        df["data"] = pd.to_datetime(df["data"], dayfirst=True)

        # Converte valor 
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

        # Remover valores nulos 
        df = df.dropna()

        # Ordenar 
        df = df.sort_values("data")

        # Tratamento especial para SELIC (diária -> mensal)
        if name_serie == "selic":
            df["mes"] = df["data"].dt.to_period("M")

             # pega último valor do mês (taxa anual daquele mês)
            df = (
                df.groupby("mes")["valor"]
                .last()
                .reset_index()
            )

            # Converter a taxa anual -> taxa mensal equivalente
            df["valor"] = (1 + df["valor"] / 100) ** (1/12) - 1
            df["valor"] = df["valor"] * 100
        
            # Converte período para data
            df["data"] = df["mes"].dt.to_timestamp()
            
            # Mantém apenas colunas finais
            df = df[["data", "valor"]]

        output = CLEAN_PATH / f"{name_serie}.parquet"

        df.to_parquet(output, index=False)

        print(f"Salvo em: {output}")
        