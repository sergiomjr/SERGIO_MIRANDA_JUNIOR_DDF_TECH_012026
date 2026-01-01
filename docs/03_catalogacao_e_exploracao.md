# 🔍 Catalogação e Exploração dos Dados

## 1. Introdução

Este documento descreve o processo de **catalogação, organização e exploração dos dados** integrados na Plataforma Dadosfera, seguindo boas práticas de **governança de dados**, **Data Lake** e **Data Catalog**.

O objetivo desta etapa é:
- Garantir entendimento do domínio dos dados
- Facilitar o reuso por diferentes áreas
- Assegurar governança, rastreabilidade e qualidade
- Preparar os dados para análises e uso por IA

---

## 2. Organização dos Dados no Data Lake

Os dados foram organizados conforme um **modelo lógico de Data Lake**, amplamente adotado em arquiteturas modernas e compatível com a abordagem da Dadosfera.

### 2.1 Zonas do Data Lake

| Zona | Descrição | Objetivo |
|---|---|---|
| RAW (Bronze) | Dados brutos, sem transformação | Preservar a origem |
| STAGING (Silver) | Dados tratados e padronizados | Qualidade e consistência |
| CURATED (Gold) | Dados analíticos e modelados | Consumo por BI e IA |

---

### 2.2 Zona RAW (Bronze)

Nesta zona encontram-se os dados **exatamente como foram ingeridos**, sem alterações estruturais ou semânticas.

**Exemplos de datasets:**
- `olist_orders_raw`
- `olist_order_items_raw`
- `olist_products_raw`
- `product_catalog_json_raw`

**Características:**
- Formato original (CSV / JSON)
- Sem tipagem forçada
- Sem deduplicação
- Referência histórica e auditoria

---

### 2.3 Zona STAGING (Silver)

A zona STAGING contém dados **limpos, padronizados e validados**, prontos para uso analítico.

**Transformações aplicadas:**
- Padronização de nomes de colunas
- Conversão de tipos (datas, números)
- Normalização de status
- Remoção de duplicidades
- Criação de chaves técnicas
- Tratamento de valores nulos

**Exemplos de datasets:**
- `olist_orders_stg`
- `olist_order_items_stg`
- `olist_products_stg`
- `product_catalog_stg`

---

### 2.4 Zona CURATED (Gold)

A zona CURATED concentra os **datasets finais**, otimizados para consumo por ferramentas de BI, pipelines de IA e Data Apps.

**Características:**
- Granularidade bem definida
- Regras de negócio aplicadas
- Métricas consolidadas
- Relacionamentos claros

**Exemplos de datasets:**
- `fact_sales`
- `fact_delivery`
- `dim_product`
- `dim_customer`
- `dim_seller`
- `dim_date`
- `product_features_llm`

---

## 3. Processo de Catalogação na Dadosfera

Após a ingestão e organização, todos os datasets foram **catalogados na Dadosfera**, utilizando o módulo de **Exploração e Catálogo**.

### 3.1 Metadados Documentados

Para cada dataset, foram registrados os seguintes metadados:

- Nome do dataset
- Descrição funcional
- Domínio de negócio
- Granularidade
- Zona do Data Lake
- Responsável pelo dado
- Data de atualização
- Sensibilidade do dado

Esse processo facilita a descoberta e o uso dos dados por diferentes áreas da empresa.

---

### 3.2 Dicionário de Dados

Foi construído um **Dicionário de Dados**, documentando os principais campos de cada tabela.

#### Exemplo – `fact_sales`

| Campo | Tipo | Descrição |
|---|---|---|
| order_id | string | Identificador do pedido |
| product_id | string | Identificador do produto |
| seller_id | string | Identificador do seller |
| customer_id | string | Identificador do cliente |
| order_date | date | Data do pedido |
| price | numeric | Valor do produto |
| freight_value | numeric | Valor do frete |
| quantity | integer | Quantidade vendida |

---

## 4. Exploração dos Dados (Análise Inicial)

A etapa de exploração teve como objetivo **validar a consistência dos dados** e **identificar padrões relevantes** antes das análises finais.

### 4.1 Análises Realizadas

- Distribuição temporal de pedidos
- Volume de vendas por categoria
- Frequência de atrasos logísticos
- Distribuição de avaliações (reviews)
- Volume de produtos por categoria

Essas análises permitiram identificar:
- Sazonalidades
- Categorias mais relevantes
- Gargalos logísticos
- Outliers e inconsistências

---

### 4.2 Validação de Relacionamentos

Foram validados os principais relacionamentos entre datasets, como:
- Orders ↔ Order Items
- Products ↔ Order Items
- Products ↔ Product Features (LLM)
- Customers ↔ Orders
- Sellers ↔ Orders

Essa validação garantiu a integridade dos dados antes da modelagem dimensional.

---

## 5. Boas Práticas de Governança Aplicadas

Durante a catalogação e exploração, foram adotadas as seguintes boas práticas:

- Separação clara por zonas do Data Lake
- Documentação acessível e padronizada
- Uso de nomes descritivos
- Definição de ownership dos dados
- Preparação para controle de qualidade contínuo

Essas práticas são fundamentais para escalar a plataforma de dados ao longo do tempo.

---

## 6. Benefícios para o Negócio

A correta catalogação e exploração dos dados proporciona:

- Redução do tempo de descoberta de dados
- Maior confiança nos dados utilizados
- Facilidade de integração entre áreas
- Base sólida para análises avançadas e IA
- Governança desde a ingestão até o consumo

---

## 7. Considerações Finais

A etapa de **Catalogação e Exploração** consolida a base de dados do projeto, garantindo que os ativos criados na Dadosfera sejam **compreensíveis, reutilizáveis e governáveis**.

Essa fase é essencial para sustentar as próximas etapas do ciclo de vida dos dados, como **Data Quality**, **Modelagem**, **Análise** e **Data Apps**, reforçando a Dadosfera como uma plataforma central de dados corporativos.

