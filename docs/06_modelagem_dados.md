# 🧱 Modelagem de Dados

## 1. Introdução

Esta etapa descreve a **modelagem de dados adotada no projeto**, considerando o cenário de um grande **e-commerce**, os objetivos analíticos do negócio e as melhores práticas de **Data Warehousing**.

A modelagem é um dos pilares para garantir:
- Escalabilidade
- Performance analítica
- Facilidade de uso por ferramentas de BI
- Consistência semântica
- Suporte a análises avançadas e IA

---

## 2. Abordagem de Modelagem Escolhida

Foi adotada a **modelagem dimensional (Kimball)** como padrão principal do projeto.

### 2.1 Justificativa da Escolha (Kimball)

A escolha pela modelagem Kimball se justifica por:
- Forte orientação a BI e analytics
- Simplicidade de entendimento para usuários de negócio
- Excelente integração com ferramentas como Metabase
- Flexibilidade para criação de múltiplas visões analíticas
- Boa performance em consultas agregadas

Essa abordagem é especialmente adequada para o contexto de **e-commerce**, onde análises por tempo, categoria, cliente e logística são frequentes.

---

## 3. Visões Analíticas Definidas

Foram definidas **duas visões finais principais**, alinhadas às necessidades do cliente:

1. **Visão Comercial (Vendas)**
2. **Visão Operacional (Logística e SLA)**

Essas visões são independentes, mas compartilham dimensões comuns, garantindo consistência analítica.

---

## 4. Visão 1 – Comercial (Vendas)

### 4.1 Tabela Fato – `fact_sales`

**Granularidade:**  
1 linha por **item de pedido** (order_item)

**Métricas Principais:**
- `price`
- `freight_value`
- `payment_value`
- `quantity`
- `revenue` (derivada)

---

### 4.2 Dimensões Associadas

| Dimensão | Descrição |
|---|---|
| `dim_date` | Datas de pedido |
| `dim_product` | Informações do produto |
| `dim_customer` | Dados do cliente |
| `dim_seller` | Dados do vendedor |
| `dim_geography` | Localização |
| `dim_payment_type` | Forma de pagamento |

---

### 4.3 Exemplo de Estrutura – `fact_sales`

| Campo | Tipo | Descrição |
|---|---|---|
| order_id | string | Identificador do pedido |
| product_id | string | Identificador do produto |
| customer_id | string | Identificador do cliente |
| seller_id | string | Identificador do vendedor |
| date_key | int | Chave da dimensão data |
| price | numeric | Valor do produto |
| freight_value | numeric | Valor do frete |
| quantity | int | Quantidade |
| revenue | numeric | Receita total |

---

## 5. Visão 2 – Operacional (Logística)

### 5.1 Tabela Fato – `fact_delivery`

**Granularidade:**  
1 linha por **pedido**

**Métricas Principais:**
- `delivery_days`
- `estimated_delivery_days`
- `delivery_delay_days`
- `is_late` (flag)

---

### 5.2 Dimensões Associadas

| Dimensão | Descrição |
|---|---|
| `dim_date` | Datas do pedido e entrega |
| `dim_customer` | Cliente |
| `dim_seller` | Vendedor |
| `dim_origin_geo` | Origem do envio |
| `dim_destination_geo` | Destino do cliente |

---

### 5.3 Exemplo de Estrutura – `fact_delivery`

| Campo | Tipo | Descrição |
|---|---|---|
| order_id | string | Identificador do pedido |
| order_date | date | Data da compra |
| delivered_date | date | Data da entrega |
| estimated_date | date | Data estimada |
| delivery_days | int | Dias até entrega |
| delivery_delay_days | int | Dias de atraso |
| is_late | boolean | Indicador de atraso |

---

## 6. Dimensão de Produto Enriquecida com IA

A dimensão de produto (`dim_product`) foi **enriquecida com features extraídas por LLM**, provenientes do catálogo desestruturado.

### Exemplos de Atributos Enriquecidos
- Categoria normalizada
- Material
- Compatibilidade
- Atributos técnicos
- Claims de marketing

Essas features permitem análises mais ricas e suportam:
- Recomendação de produtos
- Similaridade
- Segmentação avançada

---

## 7. Camadas do Data Warehouse

O Data Warehouse segue uma organização lógica em camadas:

- **STAGING:** dados tratados e normalizados
- **DW:** fatos e dimensões
- **MART:** visões específicas para BI e Data Apps

Essa separação facilita manutenção, evolução e governança.

---

## 8. Benefícios da Modelagem Proposta

A modelagem adotada oferece:
- Alta performance analítica
- Facilidade de criação de dashboards
- Clareza semântica
- Base sólida para IA e Data Apps
- Escalabilidade futura

---

## 9. Considerações Finais

A modelagem dimensional baseada em Kimball atende plenamente aos requisitos do case, proporcionando uma estrutura clara, eficiente e preparada para análises estratégicas, operacionais e uso avançado de Inteligência Artificial dentro da Plataforma Dadosfera.

