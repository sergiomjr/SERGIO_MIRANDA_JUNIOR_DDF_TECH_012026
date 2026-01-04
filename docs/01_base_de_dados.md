# Base de Dados Utilizada

## 1. Visão Geral do Dataset

A base de dados utilizada neste projeto é o **Brazilian E-Commerce Public Dataset by Olist**, disponível publicamente na plataforma Kaggle.

Este dataset representa transações reais de um marketplace brasileiro, contendo informações sobre:
- Clientes
- Vendedores
- Pedidos
- Itens de pedidos
- Produtos
- Datas e status logísticos

Fonte oficial:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## 2. Contexto de Negócio

A Olist conecta pequenos e médios lojistas a grandes marketplaces, atuando como intermediária entre vendedores e consumidores finais.

Os dados refletem todo o ciclo de compra:
- Cadastro do cliente
- Realização do pedido
- Aprovação do pagamento
- Logística e entrega
- Avaliação e status final do pedido

Esse contexto permite análises como:
- Volume de vendas por período
- Distribuição geográfica de clientes e vendedores
- Performance logística
- Análise de faturamento e frete

---

## 3. Estrutura dos Dados Originais

Os dados são disponibilizados em formato **CSV**, com tabelas normalizadas, entre as principais:

| Tabela               | Descrição                                      |
|----------------------|-----------------------------------------------|
| customers            | Dados cadastrais dos clientes                 |
| sellers              | Dados cadastrais dos vendedores               |
| orders               | Informações gerais dos pedidos                |
| order_items          | Detalhes dos itens vendidos por pedido        |
| products             | Informações dos produtos                      |
| product_category     | Tradução das categorias de produtos           |

---

## 4. Características dos Dados

- Dados reais anonimizados
- Volume aproximado de:
  - ~100 mil pedidos
  - ~100 mil clientes
  - ~3 mil vendedores
  - ~33 mil produtos
- Período coberto: **2016 a 2018**
- Presença de dados faltantes e inconsistências reais de produção

---

## 5. Justificativa da Escolha do Dataset

A escolha deste dataset se deve a:
- Alta aderência a cenários reais de negócio
- Complexidade adequada para avaliação técnica
- Diversidade de entidades (clientes, produtos, vendas, tempo)
- Possibilidade de modelagem dimensional
- Excelente base para análise exploratória e indicadores

---

## 6. Considerações sobre Governança

Apesar de ser um dataset público, o projeto trata os dados com boas práticas de governança, incluindo:
- Padronização de nomes
- Controle de qualidade
- Catalogação dos ativos
- Documentação técnica detalhada

---

## 7. Conclusão

O dataset Olist fornece uma base sólida para construção de pipelines de dados completos, permitindo demonstrar competências técnicas em engenharia, governança e análise de dados.
