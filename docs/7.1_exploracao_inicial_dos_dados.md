# Análise de Dados

## 1. Objetivo da Etapa

Esta etapa tem como objetivo realizar **análises exploratórias e analíticas** a partir dos dados modelados na **camada GOLD**, transformando dados em **informação e insights de negócio**.

As análises foram conduzidas com base na **FACT_SALES** e suas dimensões associadas, utilizando consultas SQL e agregações analíticas.

---

## 2. Fonte dos Dados Analíticos

As análises utilizam as seguintes tabelas da camada GOLD:

- GOLD_FACT_SALES
- GOLD_DIM_CUSTOMER
- GOLD_DIM_PRODUCT
- GOLD_DIM_SELLER
- GOLD_DIM_DATE
- GOLD_SELLERS_POR_ESTADO

Essas tabelas estão estruturadas em modelo dimensional (Star Schema), otimizadas para consultas analíticas.

---

## 3. Indicadores e Análises Realizadas

### 3.1 Volume de Vendas ao Longo do Tempo

Análise da evolução do volume de vendas por período (ano e mês), permitindo identificar tendências e sazonalidade.

Exemplo de métrica:
- Quantidade de itens vendidos
- Valor total de vendas

```sql
SELECT
  d.year,
  d.month,
  COUNT(*) AS qtd_itens_vendidos,
  SUM(f.total_item_value) AS valor_total_vendas
FROM gold_fact_sales f
JOIN gold_dim_date d
  ON f.date_key = d.date_key
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
````
3.2 Análise de Vendas por Estado do Cliente

Avaliação da distribuição das vendas por estado, identificando regiões com maior participação no faturamento.

Métricas analisadas:

Quantidade de vendas

Valor total vendido

3.3 Performance de Vendedores

Análise de performance dos vendedores, considerando:

Quantidade de itens vendidos

Receita total gerada

Distribuição geográfica

Essa análise permite identificar sellers com maior impacto no negócio.

3.4 Análise por Categoria de Produto

Avaliação das categorias de produtos mais vendidas, considerando:

Volume de vendas

Faturamento

Participação percentual no total

3.5 Distribuição Geográfica de Sellers

Utilização da tabela GOLD_SELLERS_POR_ESTADO para analisar a concentração de vendedores por UF, facilitando análises regionais e visualizações em mapas.

4. Principais Insights

O volume de vendas apresenta variação significativa ao longo do tempo, indicando sazonalidade.

Estados com maior concentração de clientes tendem a gerar maior faturamento.

Um subconjunto reduzido de vendedores concentra grande parte das vendas.

Determinadas categorias de produtos possuem maior representatividade no faturamento total.

5. Possíveis Visualizações

As análises realizadas permitem a criação de visualizações como:

Séries temporais de vendas

Mapas geográficos por estado

Rankings de vendedores e produtos

Dashboards executivos de performance

Essas visualizações podem ser consumidas em ferramentas de BI como Power BI, Tableau ou similares.

6. Limitações

O dataset é histórico e não reflete dados em tempo real.

Algumas análises podem ser impactadas por dados faltantes esperados (ex.: pedidos cancelados).

Não foram aplicados modelos preditivos.

7. Conclusão

A etapa de análise de dados demonstra como uma arquitetura bem estruturada permite gerar insights relevantes de negócio, reforçando a importância da modelagem dimensional e da qualidade dos dados para análises confiáveis.
