# 📊 Análise de Dados e Visualização

## 1. Introdução

Nesta etapa do projeto, os dados já integrados, catalogados, validados e modelados foram utilizados para **gerar valor analítico ao negócio**, por meio da criação de **dashboards e análises exploratórias** utilizando o módulo de **Visualização da Dadosfera (Metabase)**.

O foco desta fase é demonstrar como a Plataforma de Dados permite:
- Análises descritivas
- Identificação de padrões
- Apoio à tomada de decisão
- Monitoramento de indicadores-chave do e-commerce

---

## 2. Objetivos da Análise

Os principais objetivos das análises desenvolvidas foram:
- Entender o comportamento de vendas ao longo do tempo
- Avaliar a performance das categorias de produtos
- Identificar gargalos logísticos
- Monitorar a experiência do cliente
- Disponibilizar informações de forma clara e acessível

---

## 3. Coleção de Dashboards

Foi criada uma **Coleção no módulo de Visualização da Dadosfera** com o seguinte padrão de nomenclatura:

Sérgio Miranda Junior - 01_2026


Essa coleção centraliza todos os dashboards e consultas SQL criados neste projeto.

---

## 4. Visualizações Criadas

Foram desenvolvidas **5 visualizações**, utilizando **5 tipos diferentes de gráficos**, conforme exigido no case.

---

### 4.1 Evolução de Vendas no Tempo (Série Temporal)

**Tipo de visualização:** Linha  

**Objetivo:**  
Analisar a evolução do volume de vendas e da receita ao longo do tempo.

**Métricas:**
- Quantidade de pedidos
- Receita total

**Dimensão temporal:** Mês / Ano

**Insights esperados:**
- Sazonalidade
- Crescimento ou queda de vendas
- Impacto de períodos específicos (datas comemorativas)

---

### 4.2 Receita por Categoria de Produto

**Tipo de visualização:** Barras  

**Objetivo:**  
Identificar as categorias com maior contribuição de receita.

**Métricas:**
- Receita total
- Ticket médio

**Insights esperados:**
- Categorias estratégicas
- Possibilidades de foco comercial
- Comparação entre volume e valor

---

### 4.3 Distribuição Geográfica de Entregas

**Tipo de visualização:** Mapa  

**Objetivo:**  
Visualizar a distribuição de pedidos e atrasos por região.

**Métricas:**
- Quantidade de pedidos
- Percentual de atrasos

**Dimensões:**
- Estado (UF)
- Cidade

**Insights esperados:**
- Regiões com maior demanda
- Regiões com gargalos logísticos

---

### 4.4 Funil de Status dos Pedidos

**Tipo de visualização:** Funil / Pizza  

**Objetivo:**  
Analisar a conversão dos pedidos ao longo do seu ciclo de vida.

**Status analisados:**
- Criado
- Aprovado
- Enviado
- Entregue
- Cancelado

**Insights esperados:**
- Perdas no processo
- Eficiência operacional
- Taxa de cancelamento

---

### 4.5 Atraso Logístico por Categoria

**Tipo de visualização:** Heatmap  

**Objetivo:**  
Identificar categorias com maior incidência de atrasos.

**Métricas:**
- Média de dias de atraso
- Percentual de pedidos atrasados

**Insights esperados:**
- Correlação entre tipo de produto e atraso
- Oportunidades de melhoria logística

---

## 5. Consultas SQL Utilizadas

As análises foram construídas utilizando **consultas SQL** sobre as tabelas modeladas (fatos e dimensões).

### Exemplo – Receita por Categoria

```sql
SELECT
  p.category_name,
  SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_product p
  ON f.product_id = p.product_id
GROUP BY p.category_name
ORDER BY total_revenue DESC;
```

## 6. Boas Práticas Aplicadas

Durante a criação das análises, foram adotadas as seguintes boas práticas:

Uso de tabelas modeladas (DW)

Métricas claramente definidas

Visualizações adequadas ao tipo de dado

Padronização de nomenclatura

Foco em clareza e interpretação

## 7. Bônus – Alertas e Notificações

Como recurso adicional, foram exploradas funcionalidades de alertas do Metabase, como:

Notificação de aumento de atrasos logísticos

Queda significativa de receita em determinado período

Esses alertas reforçam o uso da plataforma como ferramenta ativa de gestão.

## 8. Benefícios para o Negócio

As análises desenvolvidas permitem:

Monitoramento contínuo de KPIs

Identificação rápida de problemas

Apoio a decisões comerciais e operacionais

Democratização do acesso à informação

## 9. Considerações Finais

A etapa de Análise de Dados demonstra como a Plataforma Dadosfera viabiliza a transformação de dados em insights acionáveis, integrando modelagem, qualidade e visualização em um único ecossistema.

Essas análises servem como base para decisões estratégicas, melhorias operacionais e evolução para análises prescritivas e aplicações de IA.
