# Qualidade de Dados (Data Quality)

## 1. Objetivo da Etapa

A etapa de **Qualidade de Dados** tem como objetivo garantir que os dados utilizados nas análises sejam **confiáveis, consistentes e adequados ao uso analítico**.

Foram definidas regras de validação aplicadas principalmente nas camadas **BRONZE e SILVER**, assegurando que apenas dados de boa qualidade avancem para a modelagem dimensional na camada GOLD.

---

## 2. Dimensões de Qualidade Avaliadas

As verificações de qualidade foram baseadas nas seguintes dimensões:

- **Completude**: verificação de valores nulos
- **Consistência**: coerência entre colunas relacionadas
- **Unicidade**: garantia de chaves únicas
- **Validade**: valores dentro de domínios esperados
- **Acurácia temporal**: consistência entre datas do processo

---

## 3. Regras de Qualidade Definidas

### 3.1 Regras de Chave Primária

| Tabela              | Regra                                      |
|---------------------|--------------------------------------------|
| CUSTOMERS           | `customer_id` não pode ser nulo            |
| ORDERS              | `order_id` não pode ser nulo               |
| ORDER_ITEMS         | (`order_id`, `order_item_id`) únicos       |
| PRODUCTS            | `product_id` não pode ser nulo             |
| SELLERS             | `seller_id` não pode ser nulo              |

---

### 3.2 Regras de Completude

| Coluna                         | Regra                              |
|--------------------------------|------------------------------------|
| customer_state                 | Não pode ser nulo                  |
| seller_state                   | Não pode ser nulo                  |
| order_purchase_timestamp       | Não pode ser nulo                  |
| price                           | Não pode ser nulo                  |
| freight_value                  | Não pode ser nulo                  |

---

### 3.3 Regras de Consistência Temporal

| Regra                                                                 |
|------------------------------------------------------------------------|
| order_approved_at >= order_purchase_timestamp                          |
| order_delivered_customer_date >= order_approved_at (quando aplicável) |
| order_estimated_delivery_date >= order_purchase_timestamp              |

---

### 3.4 Regras de Validade de Domínio

| Coluna         | Regra                                                        |
|----------------|--------------------------------------------------------------|
| order_status   | Valores permitidos: delivered, shipped, canceled, unavailable |
| price          | Deve ser maior ou igual a zero                               |
| freight_value  | Deve ser maior ou igual a zero                               |

---

## 4. Tratamento de Anomalias

As seguintes estratégias foram adotadas:

- Registros com chaves nulas foram descartados
- Datas inconsistentes foram mantidas para análise, mas sinalizadas
- Valores monetários negativos não foram encontrados no dataset
- Valores ausentes esperados (ex.: datas de entrega para pedidos cancelados) foram mantidos

---

## 5. Exemplos de Consultas de Validação

```sql
-- Verificação de chaves nulas
SELECT COUNT(*) 
FROM silver_orders
WHERE order_id IS NULL;

-- Verificação de datas inconsistentes
SELECT *
FROM silver_orders
WHERE order_delivered_customer_date < order_approved_at;
