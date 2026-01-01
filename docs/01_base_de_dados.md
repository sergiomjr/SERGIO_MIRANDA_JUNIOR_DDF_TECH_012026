# 🗃️ Base de Dados do Case

## 1. Introdução

Este documento descreve as **bases de dados utilizadas neste case técnico**, alinhadas ao cenário proposto de uma **grande empresa de e-commerce** que busca construir uma **Plataforma de Dados centralizada**, com foco em **análises descritivas, prescritivas e uso de Inteligência Artificial**.

A escolha das bases foi orientada por três critérios principais:
- Aderência ao domínio de e-commerce
- Volume mínimo exigido (**≥ 100.000 registros**)
- Capacidade de sustentar análises analíticas e de IA ponta a ponta

---

## 2. Visão Geral das Bases Utilizadas

O case utiliza **duas bases principais**, complementares entre si:

| Tipo | Base | Finalidade |
|---|---|---|
| Transacional (estruturada) | Olist E-commerce Dataset | Análises operacionais, comerciais e logísticas |
| Desestruturada (texto) | Catálogo de Produtos Sintético (JSON) | Feature engineering com GenAI |

Essa abordagem reflete um cenário real de e-commerce, onde dados transacionais convivem com grandes volumes de dados textuais de anúncios e descrições de produtos.

---

## 3. Base Transacional – Olist E-commerce Dataset

### 3.1 Descrição Geral

A base transacional utilizada é o **Brazilian E-Commerce Public Dataset by Olist**, amplamente utilizado em estudos de dados e analytics.

Ela representa transações reais de um marketplace brasileiro, contendo informações sobre:
- Pedidos
- Itens vendidos
- Produtos
- Clientes
- Sellers
- Pagamentos
- Avaliações
- Geolocalização

### 3.2 Volume de Dados

A base contém **centenas de milhares de registros**, distribuídos em múltiplas tabelas, atendendo integralmente o requisito mínimo do case.

Exemplos de volume:
- `orders`: ~100.000 registros
- `order_items`: ~110.000 registros
- `order_payments`: ~100.000 registros
- `order_reviews`: ~100.000 registros

---

### 3.3 Principais Tabelas Utilizadas

| Tabela | Descrição |
|---|---|
| `orders` | Informações gerais dos pedidos |
| `order_items` | Detalhes dos itens vendidos |
| `products` | Cadastro de produtos |
| `customers` | Dados dos clientes |
| `sellers` | Dados dos vendedores |
| `order_payments` | Formas e valores de pagamento |
| `order_reviews` | Avaliações dos clientes |
| `geolocation` | Dados geográficos |

---

### 3.4 Casos de Uso Atendidos

A base Olist permite análises como:
- Evolução temporal de pedidos e receita
- Análise de categorias de produtos
- Performance de sellers
- Análise de SLA e atraso logístico
- Avaliação da experiência do cliente (reviews)

---

## 4. Base Desestruturada – Catálogo de Produtos Sintético

### 4.1 Motivação

Embora a base Olist contenha informações de produtos, ela **não possui descrições textuais ricas em grande volume**, comuns em plataformas de e-commerce modernas.

Para atender ao **Item 5 – Processar (GenAI & LLMs)**, foi criada uma **base desestruturada sintética**, simulando um **catálogo real de produtos** com títulos e descrições extensas.

---

### 4.2 Estrutura do Dataset

O catálogo foi gerado no formato **JSON**, com a seguinte estrutura:

```json
{
  "product_id": "string",
  "title": "string",
  "description": "string"
}
````
## 4.3 Geração dos Dados Sintéticos

A geração do catálogo foi realizada via script em Python, disponível em:

/synthetic_data/generate_product_catalog.py


Características do processo:

Uso das categorias reais do Olist como base

Variação de atributos por categoria

Textos longos e semiestruturados

Volume final: 100.000+ registros

Esse processo garante realismo sem comprometer privacidade ou dados sensíveis.

## 4.4 Casos de Uso Atendidos

A base desestruturada possibilita:

Extração de atributos via LLM

Classificação automática de produtos

Similaridade entre produtos

Enriquecimento do catálogo

Apoio a mecanismos de recomendação

## 5. Relacionamento entre as Bases

O relacionamento entre as bases ocorre por meio do campo:

product_id


Esse identificador permite:

Associar features extraídas por IA aos dados transacionais

Análises combinadas entre vendas e atributos de produto

Uso das features em BI e Data Apps

## 6. Justificativa da Escolha das Bases

A combinação de:

Dados transacionais reais

Dados desestruturados sintéticos em larga escala

permite demonstrar, de forma prática:

Integração de múltiplas fontes

Governança e qualidade de dados

Processamento de texto com GenAI

Modelagem analítica

Geração de valor para o negócio

Essa abordagem reflete um cenário realista e escalável, alinhado aos desafios enfrentados por grandes empresas de e-commerce.

## 7. Considerações Finais

As bases selecionadas atendem integralmente os requisitos do case técnico da Dadosfera e fornecem uma base sólida para:

Análises descritivas e prescritivas

Desenvolvimento de modelos de IA

Criação de dashboards e Data Apps

Demonstração do ciclo de vida completo dos dados


---
