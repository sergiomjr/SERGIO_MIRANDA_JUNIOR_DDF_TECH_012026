# Planejamento do Projeto – Abordagem PMBOK

## 1. Visão Geral do Projeto

Este projeto foi desenvolvido como parte do **Desafio Técnico da Dadosfera**, com o objetivo de construir um **pipeline de dados completo (end-to-end)**, cobrindo desde a ingestão até a camada analítica final, utilizando boas práticas de **Data Engineering, Data Governance e Analytics**.

O projeto simula um cenário real de dados corporativos, adotando conceitos amplamente utilizados no mercado, como:
- Arquitetura em camadas (BRONZE, SILVER e GOLD)
- Catálogo de dados
- Qualidade de dados
- Modelagem dimensional
- Análise exploratória e geração de insights

---

## 2. Objetivos do Projeto

### 2.1 Objetivo Geral
Construir um pipeline de dados estruturado e documentado, demonstrando domínio técnico em ingestão, transformação, catalogação, qualidade e análise de dados.

### 2.2 Objetivos Específicos
- Ingerir dados brutos (raw) provenientes do dataset Olist
- Organizar os dados em camadas BRONZE, SILVER e GOLD
- Catalogar todos os ativos de dados na plataforma Dadosfera
- Aplicar regras de qualidade de dados
- Modelar os dados em esquema dimensional (Star Schema)
- Realizar análises exploratórias e gerar indicadores de negócio
- Documentar todas as etapas do processo

---

## 3. Escopo do Projeto

### 3.1 Dentro do Escopo
- Ingestão de dados do dataset Olist (Kaggle)
- Criação de tabelas nas camadas BRONZE, SILVER e GOLD
- Catalogação dos datasets
- Aplicação de regras de Data Quality
- Modelagem dimensional (Dimensões e Fato)
- Análises exploratórias e métricas de negócio
- Documentação técnica completa

### 3.2 Fora do Escopo
- Implementação de pipelines em produção (CI/CD)
- Orquestração com ferramentas externas (ex: Airflow)
- Machine Learning ou modelos preditivos
- Integração com APIs externas

---

## 4. Stakeholders

| Stakeholder           | Papel no Projeto                          |
|----------------------|-------------------------------------------|
| Avaliador Técnico    | Avaliação da arquitetura e boas práticas  |
| Dadosfera            | Plataforma de dados e catalogação         |
| Desenvolvedor (Autor)| Implementação e documentação do projeto   |

---

## 5. Entregáveis

- Pipeline de dados organizado por camadas
- Catálogo de dados documentado
- Regras de qualidade de dados aplicadas
- Modelo dimensional na camada GOLD
- Análises exploratórias
- Documentação técnica no GitHub

---

## 6. Cronograma de Alto Nível

| Etapa                          | Status |
|--------------------------------|--------|
| Planejamento                   | ✔️     |
| Ingestão de Dados              | ✔️     |
| Integração e Transformações    | ✔️     |
| Catalogação e Exploração       | ✔️     |
| Qualidade de Dados             | ✔️     |
| Modelagem Dimensional          | ✔️     |
| Análise de Dados               | ✔️     |
| Apresentação do Case           | ✔️     |

---

## 7. Metodologia Utilizada

A abordagem do **PMBOK** foi utilizada para estruturar o projeto, com foco em:
- Planejamento claro
- Definição de escopo
- Entregáveis bem definidos
- Rastreabilidade das etapas
- Documentação como ativo do projeto

---

## 8. Riscos Identificados

| Risco                              | Mitigação                                 |
|-----------------------------------|-------------------------------------------|
| Inconsistência nos dados de origem| Validações e regras de Data Quality       |
| Dados faltantes                   | Tratamento na camada SILVER               |
| Falta de documentação             | Documentação contínua no GitHub           |

---

## 9. Considerações Finais

Este planejamento garante que o projeto seja executado de forma organizada, rastreável e alinhada às boas práticas de engenharia de dados, refletindo cenários reais enfrentados em ambientes corporativos.
