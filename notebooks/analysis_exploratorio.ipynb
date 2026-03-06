import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_parquet("data/analytics/endividamento_10anos.parquet")

    #print(df.head())
    print(df.info())
    print(df.describe())

    # Gráficos simples do endividamento
    df.plot(x="data", y="endividamento", title="Endividamento das Famílias")
    plt.show()

    # Comparação de todas as séries 
    df.plot(x="data", y=["endividamento", "selic", "inadimplencia_pf", "inadimplencia_total"],
        title="Indicadores econômicos - últimos 10 anos")
    plt.show()

    # Estatistica por período 
    print("\nMédias por perído:")
    print(df.groupby("periodo")[["endividamento", "selic", "inadimplencia_pf","inadimplencia_total"]].mean())

    # Relação Selic vs Endividamento 
    df.plot(x="selic", y="endividamento", kind="scatter",
        title="Correlação Selic x Endividamento")
    plt.show()

if __name__ == "__main__":
    main()