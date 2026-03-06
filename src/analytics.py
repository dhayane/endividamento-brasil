import pandas as pd
from pathlib import Path

CLEAN_PATH = Path("data/clean")
ANALYTICS_PATH = Path("data/analytics")

def build_analytics_dataset():
    print("Construindo dataset analítico...")
    
    ANALYTICS_PATH.mkdir(parents=True, exist_ok=True)

    # Ler os datasets 
    endividamento = pd.read_parquet(CLEAN_PATH / "endividamento_familias.parquet")
    inad_pf = pd.read_parquet(CLEAN_PATH / "inadimplencia_pf.parquet")
    inad_total = pd.read_parquet(CLEAN_PATH / "inadimplencia_total.parquet")
    selic = pd.read_parquet(CLEAN_PATH / "selic.parquet")

    # Renomear coluna valor para cada série 
    endividamento = endividamento.rename(columns={"valor": "endividamento"})
    inad_pf = inad_pf.rename(columns={"valor": "inadimplencia_pf"})
    inad_total = inad_total.rename(columns={"valor": "inadimplencia_total"})
    selic = selic.rename(columns={"valor": "selic"})

    # Merge das séries pela data
    df = endividamento.merge(inad_pf, on="data", how="left")
    df = df.merge(inad_total, on="data", how="left")
    df = df.merge(selic, on="data", how="left")

    # Criar coluna ano 
    df["ano"] = df["data"].dt.year

    # Classificar perído da pandemia 
    def classificar_periodo(ano):
        if ano < 2020:
            return "pre_pandemia"
        elif 2020 <= ano <= 2021:
            return "pandemia"
        else: 
            return "pos_pandemia"

    df["periodo"] = df["ano"].apply(classificar_periodo)

    # Ordenar 
    df = df.sort_values("data")

    # Salvar dataset final 
    output = ANALYTICS_PATH / "endividamento_10anos.parquet"
    df.to_parquet(output, index=False)

    print(f"Dataset analítico salvo em: {output}")