# ✅ Data Quality – Garantia da Qualidade dos Dados

## 1. Introdução

A qualidade dos dados é um fator crítico para o sucesso de qualquer Plataforma de Dados, especialmente quando os dados são utilizados para **análises estratégicas, modelos de IA e Data Apps**.

Neste projeto, a etapa de **Data Quality** tem como objetivo:
- Identificar inconsistências e dados faltantes
- Garantir confiabilidade dos dados analíticos
- Minimizar riscos para modelos de IA
- Aumentar a confiança das áreas de negócio nos dados

Para isso, foram adotadas **boas práticas de Data Quality**, alinhadas às recomendações da Dadosfera, utilizando a biblioteca **Great Expectations**.

---

## 2. Abordagem de Qualidade de Dados

A estratégia de Data Quality foi aplicada principalmente sobre os dados das zonas:
- **STAGING (Silver)**
- **CURATED (Gold)**

Essa abordagem garante que:
- Dados brutos sejam preservados
- Dados consumidos por BI e IA estejam validados

---

## 3. Ferramenta Utilizada – Great Expectations

O **Great Expectations (GE)** foi utilizado para:
- Definir regras de qualidade
- Validar datasets automaticamente
- Gerar relatórios de qualidade
- Documentar expectativas e resultados

Os testes de qualidade foram executados antes da disponibilização dos dados finais para análise.

---

## 4. Regras de Data Quality Implementadas

As regras foram definidas considerando o domínio de e-commerce e os principais riscos de inconsistência.

### 4.1 Regras de Completude (NOT NULL)

Campos obrigatórios que não podem conter valores nulos:
- `order_id`
- `customer_id`
- `product_id`
- `seller_id`
- `order_purchase_timestamp`
- `price`
- `freight_value`

---

### 4.2 Regras de Unicidade

- `order_id` deve ser único na tabela de pedidos
- Combinação (`order_id`, `product_id`) deve ser única em itens do pedido

---

### 4.3 Regras de Validade de Domínio

Campos categóricos devem respeitar domínios conhecidos:
- `order_status` ∈ {created, approved, invoiced, shipped, delivered, canceled}
- `payment_type` ∈ {credit_card, boleto, voucher, debit_card}

---

### 4.4 Regras de Consistência Temporal

- `order_delivered_customer_date` ≥ `order_purchase_timestamp`
- `order_estimated_delivery_date` ≥ `order_purchase_timestamp`

---

### 4.5 Regras de Valores Numéricos

- `price` ≥ 0
- `freight_value` ≥ 0
- `payment_value` ≥ 0
- `review_score` entre 1 e 5

---

### 4.6 Regras de Integridade Referencial

- `order_items.order_id` deve existir em `orders.order_id`
- `order_items.product_id` deve existir em `products.product_id`
- `orders.customer_id` deve existir em `customers.customer_id`

---

## 5. Execução dos Testes de Qualidade

Os testes foram executados via notebooks em Python, integrados ao fluxo de dados da plataforma.

### Etapas:
1. Carregamento dos datasets STAGING
2. Definição das expectativas (GE)
3. Execução dos testes
4. Geração de relatório de qualidade
5. Persistência dos dados aprovados na zona CURATED

📄 **Relatórios de Data Quality** foram gerados automaticamente, evidenciando:
- Percentual de sucesso por regra
- Linhas inválidas
- Campos com problemas recorrentes

---

## 6. Tratamento de Inconsistências

As principais ações adotadas para tratamento de dados inválidos foram:

- Correção de tipos e formatos
- Padronização de valores categóricos
- Remoção ou correção de registros inconsistentes
- Isolamento de registros críticos para análise posterior

Essa abordagem evita impactos negativos nas análises finais e nos modelos de IA.

---

## 7. Common Data Model (BÔNUS)

Como bônus, foi definido um **Common Data Model (CDM)** para o domínio de e-commerce, padronizando entidades centrais:

- Customer
- Order
- Order Item
- Product
- Seller
- Payment
- Review
- Shipment

O CDM facilita:
- Integração entre áreas
- Evolução da plataforma
- Reuso de dados
- Consistência semântica

---

## 8. Benefícios da Estratégia de Data Quality

A implementação de Data Quality proporcionou:

- Maior confiabilidade dos dados analíticos
- Redução de erros em dashboards
- Melhor performance de modelos de IA
- Governança desde a ingestão
- Base sólida para escalabilidade futura

---

## 9. Considerações Finais

A etapa de **Data Quality** é fundamental para garantir que a Plataforma de Dados construída com a Dadosfera entregue **dados confiáveis, consistentes e prontos para gerar valor**.

A adoção de ferramentas como o Great Expectations, aliada a boas práticas de governança, reforça a Dadosfera como um ambiente robusto para projetos de dados corporativos.

