# ⚡ SmartEnergy Analytics

Plataforma de **Data Analytics para interrupções de energia**, construída em **Python + PostgreSQL + Power BI**.

Este projeto foi desenvolvido como estudo prático** em empresas do setor elétrico**.

---

## 🎯 Objetivo

Transformar dados de interrupções de energia em **insights operacionais** e **dashboards executivos**, respondendo perguntas como:

- Quais regiões têm mais interrupções?
- Qual o impacto em quantidade de clientes afetados?
- Quais causas mais contribuem para o tempo total de indisponibilidade?
- Como está a duração média das interrupções por região, causa e status?

---

## 🧰 Stack Tecnológica

- **Python 3.9**
  - `pandas` para tratamento e análise de dados
  - `sqlalchemy` + `psycopg2-binary` para integração com **PostgreSQL**
  - `matplotlib` para visualizações
- **PostgreSQL**
  - Armazenamento estruturado dos dados de interrupções
  - Consultas em SQL para análises rápidas
- **Jupyter Notebooks**
  - Exploração de dados e análises passo a passo
- **Power BI (planejado)**
  - Criação de dashboards operacionais e executivos

---

## 📂 Estrutura do Projeto

```bash
smartenergy-analytics/
├─ data/
│  ├─ raw/          # Dados brutos de entrada (CSV, Excel etc.)
│  └─ processed/    # Dados tratados prontos para análise
├─ notebooks/       # Notebooks Jupyter de exploração e dashboards
├─ src/             # Código-fonte em Python (ETL, modelos, integrações)
├─ .gitignore       # Arquivos e pastas ignorados no controle de versão
├─ requirements.txt # Dependências do projeto
└─ README.md
