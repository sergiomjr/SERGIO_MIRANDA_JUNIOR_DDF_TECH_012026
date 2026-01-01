# 📋 Planejamento do Projeto – Abordagem PMBOK

## 1. Visão Geral do Planejamento

Este documento descreve o **planejamento do projeto de implementação da Plataforma de Dados com a Dadosfera**, seguindo boas práticas do **PMBOK (Project Management Body of Knowledge)**.

O objetivo do planejamento é garantir:
- Clareza de escopo
- Entregas incrementais
- Controle de riscos
- Alocação eficiente de recursos
- Previsibilidade de custos e prazos

O projeto é estruturado como uma **Prova de Conceito (PoC)** com foco em geração rápida de valor para um grande e-commerce.

---

## 2. Estrutura do Projeto (Fases PMBOK)

### 2.1 Iniciação
- Kickoff com stakeholders
- Entendimento do problema de negócio
- Definição de objetivos e KPIs
- Escolha da base de dados (Olist + Catálogo Sintético)

**Entregáveis:**
- Escopo inicial
- Definição do case técnico

---

### 2.2 Planejamento
- Definição da arquitetura de dados
- Planejamento da ingestão e catalogação
- Estratégia de Data Quality
- Definição da modelagem de dados
- Planejamento do uso de GenAI
- Definição dos dashboards e Data App

**Entregáveis:**
- Arquitetura alvo
- Plano de qualidade de dados
- Backlog de atividades

---

### 2.3 Execução
- Ingestão dos dados na Dadosfera
- Catalogação e exploração
- Implementação de regras de qualidade
- Feature engineering com LLM
- Modelagem dimensional
- Criação de dashboards
- Desenvolvimento do Data App

**Entregáveis:**
- Datasets catalogados
- Relatórios de Data Quality
- Features geradas por IA
- Dashboards e Data App

---

### 2.4 Monitoramento e Controle
- Validação de dados e métricas
- Monitoramento da qualidade
- Ajustes de escopo e performance
- Revisões técnicas

**Entregáveis:**
- Evidências (prints)
- Ajustes documentados

---

### 2.5 Encerramento
- Consolidação da documentação
- Gravação do vídeo de apresentação
- Revisão final do repositório GitHub

**Entregáveis:**
- Repositório final
- Vídeo unlisted no YouTube

---

## 3. Cronograma de Alto Nível

| Fase | Atividades Principais | Duração Estimada |
|---|---|---|
| Iniciação | Kickoff e definição do escopo | 1 dia |
| Planejamento | Arquitetura, backlog e DQ | 2 dias |
| Execução | Ingestão, IA, BI, App | 5 dias |
| Monitoramento | Validação e ajustes | 1 dia |
| Encerramento | Documentação e vídeo | 1 dia |

⏱️ **Duração total estimada:** 10 dias

---

## 4. Alocação de Recursos

| Recurso | Responsabilidade |
|---|---|
| Data Engineer | Ingestão, pipelines, modelagem |
| Analytics Engineer | BI, métricas, dashboards |
| Data Scientist | Feature engineering com LLM |
| Plataforma Dadosfera | Integração, governança, visualização |

*(No contexto do case, todas as funções são desempenhadas pelo autor do projeto.)*

---

## 5. Estimativa de Custos (Alto Nível)

| Item | Descrição |
|---|---|
| Plataforma de Dados | Uso da Dadosfera (SaaS) |
| Processamento | Pipelines e queries |
| GenAI | Uso de LLM em batch |
| BI e Data Apps | Metabase + Streamlit |

💡 **Observação:**  
A centralização das etapas na Dadosfera reduz custos operacionais quando comparado a arquiteturas fragmentadas (ETL + DW + BI + ML separados).

---

## 6. Análise de Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Dados incompletos | Média | Alto | Regras de Data Quality |
| Inconsistência de dados | Média | Alto | Catalogação e CDM |
| Custo elevado de IA | Baixa | Médio | Processamento em batch |
| Escopo excessivo | Média | Médio | MVP orientado a valor |
| Atrasos | Baixa | Médio | Planejamento incremental |

---

## 7. Dependências e Pontos Críticos

### Dependências
- Acesso ao ambiente de Treinamento da Dadosfera
- Acesso à Internet
- Disponibilidade do Google Colab
- Dataset Olist e geração do catálogo sintético

### Pontos Críticos
- Qualidade dos dados impacta diretamente BI e IA
- Features geradas por LLM precisam de validação
- Modelagem correta é essencial para escalabilidade

---

## 8. Critérios de Sucesso do Projeto

- Dados integrados e catalogados com sucesso
- Relatórios de Data Quality implementados
- Features de IA geradas a partir de dados desestruturados
- Dashboards funcionais e informativos
- Data App operacional
- Documentação clara e reprodutível

---

## 9. Conclusão

Este planejamento garante uma execução estruturada, alinhada às boas práticas do PMBOK, demonstrando como a **Dadosfera atua como aceleradora do ciclo de vida dos dados**, reduzindo complexidade e aumentando a geração de valor para o negócio.

