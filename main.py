from src.extract import load_settings, fetch_all_bacen_series
from src.transform import transform_json_to_parquet
from src.analytics import build_analytics_dataset

def main():
    print('Iniciando pipeline...')

    # Carrega as configs
    settings = load_settings()

    # Executa a extração 
    data = fetch_all_bacen_series(settings)

    print("Extração finalizada com sucesso.")

    transform_json_to_parquet()

    print(f"Transformação finalizada.")

    # Criar dataset analítico
    build_analytics_dataset()

    print(f"Dataset analítico criado com sucesso")

if __name__ == "__main__":
    main()