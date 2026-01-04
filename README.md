## SERGIO_MIRANDA_JUNIOR_DDF_TECH_012026 

# 🚀 Data Pipeline End-to-End – Olist E-commerce (Dadosfera Case)

Este repositório contém a implementação de um **pipeline de dados completo (end-to-end)** desenvolvido como parte do **Desafio Técnico da Dadosfera**.

O projeto simula um cenário real de **engenharia de dados**, cobrindo desde a ingestão de dados brutos até a modelagem dimensional e geração de insights analíticos, aplicando boas práticas de **Data Engineering, Data Governance e Analytics**.

---

## 🎯 Objetivo do Projeto

Construir uma solução de dados organizada, governável e analítica, demonstrando:

- Arquitetura em camadas (BRONZE, SILVER, GOLD)
- Catalogação e governança de dados
- Qualidade de dados
- Modelagem dimensional (Kimball)
- Análise exploratória e geração de insights
- Documentação técnica completa

---

## 🧱 Arquitetura da Solução

A arquitetura segue o padrão clássico de **Data Lake + Data Warehouse**, organizada em três camadas:

### 🟤 BRONZE – Ingestão
- Dados brutos carregados diretamente do dataset Olist (Kaggle)
- Estrutura original preservada
- Inclusão de colunas técnicas para rastreabilidade

### ⚪ SILVER – Tratamento
- Padronização de tipos e valores
- Aplicação de regras de qualidade de dados
- Preparação para consumo analítico

### 🟡 GOLD – Análise
- Modelagem dimensional (Star Schema)
- Dimensões e tabela fato
- Data marts agregados
- Dados prontos para BI e analytics

---

## 📊 Modelo Dimensional (Camada GOLD)

### Dimensões
- `DIM_CUSTOMER`
- `DIM_PRODUCT`
- `DIM_SELLER`
- `DIM_DATE`

### Fato
- `FACT_SALES`  
  - Granularidade: **item de pedido**
  - Métricas: preço, frete, valor total do item

### Data Mart
- `SELLERS_POR_ESTADO`

O modelo segue as boas práticas propostas por **Ralph Kimball**, permitindo análises flexíveis e performáticas.

---

## 🧪 Qualidade de Dados

Foram aplicadas regras de Data Quality considerando:

- Completude
- Consistência
- Validade
- Unicidade
- Coerência temporal

As validações garantem que apenas dados confiáveis avancem para a camada analítica.

---

## 🔎 Análises Realizadas

A partir dos dados da camada GOLD, foram realizadas análises como:

- Evolução das vendas ao longo do tempo
- Distribuição geográfica de clientes e vendedores
- Performance de vendedores
- Análise por categoria de produto

Essas análises demonstram como dados bem modelados suportam decisões de negócio.

---

## 🗂️ Estrutura do Repositório

- SERGIO_MIRANDA_JUNIOR_DDF_TECH_012026/
- │
- ├── docs/
- │ ├── 00_planejamento_pmbok.md
- │ ├── 01_base_de_dados.md
- │ ├── 02_integrar.md
- │ ├── 03_catalogacao_e_exploracao.md
- │ ├── 04_data_quality.md
- │ ├── 06_modelagem_dados.md
- │ ├── 07_analise_dados.md
- │ └── 10_apresentacao_case.md
- │
- └── README.md


---

## 🛠️ Tecnologias Utilizadas

- **Dadosfera** – ingestão, catalogação e governança
- **SQL** – transformações e análises
- **Amazon S3** – armazenamento da camada BRONZE
- **PostgreSQL** – persistência das camadas SILVER e GOLD
- **GitHub** – versionamento e documentação

---

## ⭐ Diferenciais do Projeto

- Pipeline completo e bem estruturado
- Governança e catalogação de dados
- Aplicação prática de Data Quality
- Modelagem dimensional correta
- Documentação técnica detalhada
- Foco em consumo analítico

---

## 🚧 Próximos Passos (Evolução)

Em um ambiente produtivo, o projeto poderia evoluir com:
- Orquestração de pipelines (ex.: Airflow)
- Testes automatizados de qualidade
- Dashboards em ferramentas de BI
- Monitoramento e alertas
- Ingestão incremental / near real-time

---

## 👤 Autor

**Sérgio Miranda Junior**  
Projeto desenvolvido como parte do desafio técnico da Dadosfera.

---

## 🏁 Conclusão

Este projeto demonstra a capacidade de planejar, implementar e documentar uma solução de dados completa, alinhada às melhores práticas do mercado e pronta para uso analítico.
