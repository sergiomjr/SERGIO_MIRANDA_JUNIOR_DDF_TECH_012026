# Catalogação e Exploração dos Dados

## 1. Objetivo da Etapa

Esta etapa tem como objetivo garantir a **governança e a descoberta dos dados**, por meio da catalogação completa dos ativos criados nas camadas BRONZE, SILVER e GOLD.

A catalogação permite que os dados sejam:
- Facilmente encontrados
- Compreendidos por outros usuários
- Utilizados com segurança em análises e relatórios

---

## 2. Ferramenta de Catalogação

A catalogação foi realizada utilizando o **Catálogo de Dados da plataforma Dadosfera**, onde cada tabela criada no projeto foi registrada como um ativo de dados.

Para cada ativo, foram definidos:
- Descrição do dataset
- Owner (responsável)
- Tags
- Documentação das colunas (dicionário de dados)
- Evidências visuais

---

## 3. Organização por Camadas

### 3.1 Camada BRONZE

A camada BRONZE contém dados brutos, estruturados, sem aplicação de regras de negócio.

**Tabelas catalogadas:**
- DDF_TECH_BRONZE_OLIST_CUSTOMERS  
- DDF_TECH_BRONZE_OLIST_ORDERS  
- DDF_TECH_BRONZE_OLIST_ORDER_ITEMS  
- DDF_TECH_BRONZE_OLIST_PRODUCTS  
- DDF_TECH_BRONZE_OLIST_SELLERS  

Para cada tabela foram documentados:
- Granularidade
- Origem
- Descrição das principais colunas
- Relacionamentos esperados

---

### 3.2 Camada SILVER

A camada SILVER contém dados tratados e padronizados, prontos para consumo analítico intermediário.

**Tabelas catalogadas:**
- SILVER_CUSTOMERS  
- SILVER_ORDERS  
- SILVER_ORDER_ITEMS  
- SILVER_PRODUCTS  
- SILVER_SELLERS  

Nesta camada, a catalogação enfatiza:
- Regras de tratamento aplicadas
- Campos técnicos de controle
- Prontidão para modelagem dimensional

---

### 3.3 Camada GOLD

A camada GOLD contém os dados finais para análise, seguindo modelo dimensional e data marts.

**Tabelas catalogadas:**
- GOLD_DIM_CUSTOMER  
- GOLD_DIM_PRODUCT  
- GOLD_DIM_SELLER  
- GOLD_DIM_DATE  
- GOLD_FACT_SALES  
- GOLD_SELLERS_POR_ESTADO  

Nesta camada, a catalogação foca em:
- Papel da tabela no modelo analítico
- Granularidade (grão)
- Métricas e dimensões
- Relacionamentos com outras tabelas

---

## 4. Documentação dos Ativos

Para cada tabela, foram registrados no catálogo:
- Descrição detalhada do dataset
- Dicionário de dados com explicação das colunas
- Tags temáticas (ex.: olist, ecommerce, bronze, silver, gold)
- Owner do ativo

Quando a plataforma não permitiu a edição individual de colunas, a documentação foi complementada neste repositório.

---

## 5. Evidências

Como evidência da catalogação, foram coletados:
- Prints da listagem de tabelas por camada
- Prints das páginas de documentação dos ativos
- Exemplos de tabelas com descrição e colunas documentadas

Essas evidências estão armazenadas neste repositório para fins de auditoria e avaliação do projeto.

---

## 6. Benefícios da Catalogação

A catalogação dos dados permite:
- Redução de ambiguidades
- Maior reutilização dos dados
- Facilidade de onboarding de novos usuários
- Aumento da confiança nos dados

---

## 7. Conclusão

A etapa de catalogação e exploração garante que os dados produzidos no projeto sejam governáveis, compreensíveis e prontos para uso analítico, alinhando-se às melhores práticas de Data Governance.
