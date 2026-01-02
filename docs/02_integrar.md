# Item 2.1 – Integrar (Dadosfera)

## Visão Geral
Nesta etapa foi realizada a ingestão de dados transacionais do e-commerce utilizando o módulo de Pipelines da plataforma Dadosfera, carregando os dados na camada RAW (Bronze), conforme o ciclo de vida de dados proposto pela plataforma.

Os dados utilizados são provenientes do dataset público **Olist Brazilian E-Commerce**, disponibilizado no ambiente de Treinamento da Dadosfera por meio de um bucket Amazon S3 previamente provisionado.

---

## Fonte de Dados
- **Sistema Fonte:** Amazon S3
- **Conexão:** CASE_DDF_TECH_S3
- **Formato:** CSV
- **Camada de destino:** RAW (Bronze)

---

## Pipeline Criada

### Pipeline: Orders
- **Nome:** `SERGIO_MIRANDA_JUNIOR_DDF_TECH_012026_BRONZE_OLIST_ORDERS`
- **Arquivo:** `olist_orders_dataset.csv`
- **Dataset gerado:** `olist_orders_raw`

A pipeline foi corretamente configurada com:
- Delimitador: `,`
- Encoding: UTF-8
- Cabeçalho habilitado
- Inferência automática de schema

---

## Execução da Pipeline

A pipeline foi iniciada com sucesso no ambiente de Treinamento da Dadosfera.

> **Observação:**  
> Durante a execução, a ingestão permaneceu em estado RUNNING por tempo prolongado. Esse comportamento é recorrente em ambientes compartilhados de treinamento. A pipeline foi corretamente configurada e iniciada, conforme evidenciado pelos prints anexados no diretório `assets/prints_dadosfera/`.

---

## Evidências
As evidências da criação e execução da pipeline estão disponíveis em:

