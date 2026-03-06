# Endividamento Brasil

Análise do endividamento das famílias brasileiras nos últimos 10 anos, utilizando dados do Banco Central (endividamento, inadimplência e taxa Selic).  
O projeto implementa um pipeline de ETL em Python para tratar os dados e gerar visualizações analíticas.

---
## 📂 Estrutura do Projeto

endividamento-brasil/ │ ├── data/ │   ├── raw/          # Dados originais baixados │   ├── clean/        # Dados tratados (parquet) │   └── analytics/    # Dataset analítico consolidado │ ├── src/ │   ├── transform.py  # Tratamento e padronização dos dados │   ├── analytics.py  # Consolidação em dataset analítico │   ├── analysis.py   # Exploração inicial (gráficos e estatísticas) │   └── dashboard.py  # Dashboard interativo (Streamlit) │ └── README.md

---

## 🚀 Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/dhayane/endividamento-brasil.git
   cd endividamento-brasil


- Crie e ative o ambiente virtual:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
- Instale as dependências:
pip install -r requirements.txt


- Execute as etapas:
- Transformar dados brutos
python src/transform.py
- Construir dataset analítico
python src/analytics.py
- Rodar análise exploratória
python src/analysis.py
- Abrir dashboard interativo
streamlit run src/dashboard.py



# 📊 Indicadores analisados
- Endividamento das famílias (% da renda)
- Inadimplência pessoas físicas (%)
- Inadimplência total (%)
- Taxa Selic (% ao ano)

📌 Próximos passos
- Melhorar visualizações no dashboard (gráficos comparativos e interativos).
- Adicionar análises estatísticas de correlação entre Selic e endividamento.
- Documentar fontes dos dados (Banco Central do Brasil).

✨ Autor
Projeto desenvolvido por Dhayane como estudo de dados econômicos e prática de ETL + análise exploratória em Python.
