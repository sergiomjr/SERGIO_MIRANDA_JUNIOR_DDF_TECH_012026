# Modelagem de Dados

## 1. Objetivo da Etapa

Esta etapa tem como objetivo estruturar os dados para **consumo analítico**, aplicando conceitos de **Data Warehouse** e **modelagem dimensional**, seguindo as boas práticas propostas por **Ralph Kimball**.

A modelagem foi realizada na **camada GOLD**, utilizando dados previamente tratados e validados nas camadas BRONZE e SILVER.

---

## 2. Abordagem de Modelagem

Foi adotado o **modelo dimensional (Star Schema)**, composto por:
- **Tabelas Dimensão (DIM)**: atributos descritivos
- **Tabelas Fato (FACT)**: métricas e eventos de negócio

Essa abordagem facilita:
- Consultas analíticas
- Integração com ferramentas de BI
- Escalabilidade do modelo
- Performance de consultas

---

## 3. Granularidade da Tabela Fato

📌 **Grão definido para a tabela fato (FACT_SALES):**

> Cada linha representa **um item vendido dentro de um pedido**, identificado pela combinação  
> `order_id` + `order_item_id`.

Essa granularidade permite:
- Agregações corretas por produto, cliente, vendedor e tempo
- Flexibilidade para análises detalhadas e consolidadas

---

## 4. Dimensões do Modelo

### 4.1 DIM_CUSTOMER
- Fonte: SILVER_CUSTOMERS
- Granularidade: 1 registro por cliente
- Principais atributos: cidade, estado, CEP prefixo
- Tipo de chave: **Natural Key**
- Preparada para evolução com SCD

---

### 4.2 DIM_PRODUCT
- Fonte: SILVER_PRODUCTS
- Granularidade: 1 registro por produto
- Principais atributos: categoria, peso, dimensões
- Tipo de chave: **Natural Key**
- Suporte a análises logísticas e de portfólio

---

### 4.3 DIM_SELLER
- Fonte: SILVER_SELLERS
- Granularidade: 1 registro por vendedor
- Principais atributos: cidade, estado, CEP prefixo
- Tipo de chave: **Natural Key**
- Permite análises regionais de performance

---

### 4.4 DIM_DATE
- Dimensão de calendário
- Granularidade: 1 registro por dia
- Principais atributos: dia, mês, ano, dia da semana
- Utilizada para análises temporais

---

## 5. Tabela Fato

### FACT_SALES
- Fonte: SILVER_ORDERS + SILVER_ORDER_ITEMS
- Granularidade: item do pedido
- Métricas principais:
  - price
  - freight_value
  - total_item_value
- Relacionamentos:
  - DIM_CUSTOMER
  - DIM_PRODUCT
  - DIM_SELLER
  - DIM_DATE

---

## 6. Relacionamentos do Modelo

O modelo segue o padrão **estrela**, onde:
- A tabela fato se conecta diretamente a todas as dimensões
- Não há relacionamentos diretos entre dimensões

Isso garante simplicidade e performance.

---

## 7. Considerações sobre Chaves

Neste projeto, foram utilizadas **chaves naturais** provenientes do sistema de origem (ex.: `customer_id`, `product_id`, `seller_id`) para fins de simplicidade.

Em um ambiente produtivo, recomenda-se o uso de **Surrogate Keys**, visando:
- Melhor performance em joins
- Independência das chaves de origem
- Suporte a controle de histórico (SCD)

---

## 8. Benefícios do Modelo Adotado

- Facilidade de entendimento
- Flexibilidade analítica
- Compatibilidade com ferramentas de BI
- Aderência a boas práticas de Data Warehouse

---

## 9. Conclusão

A modelagem dimensional implementada na camada GOLD fornece uma base sólida e escalável para análises de negócio, atendendo aos requisitos do projeto e refletindo padrões utilizados em ambientes corporativos.
