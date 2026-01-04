# Integração de Dados

## 1. Objetivo da Etapa

A etapa de integração tem como objetivo realizar a ingestão dos dados brutos, garantindo que eles sejam carregados de forma íntegra, rastreável e organizada, respeitando boas práticas de arquitetura de dados.

Nesta fase, os dados ainda não sofrem transformações de negócio, apenas padronizações mínimas necessárias para armazenamento.

---

## 2. Arquitetura de Ingestão

A arquitetura adotada segue o padrão **Data Lake em camadas**, com separação clara de responsabilidades:

- **Camada Raw (Bronze)**: dados brutos, sem transformação
- **Camada Silver**: dados tratados e padronizados
- **Camada Gold**: dados modelados para análise

Os arquivos CSV originais do Kaggle são armazenados inicialmente na camada Raw.

---

## 3. Fonte e Origem dos Dados

- Origem: Kaggle (dataset Olist)
- Formato: CSV
- Frequência: carga única (dataset histórico)
- Volume aproximado: dezenas de milhares de registros por tabela

---

## 4. Processo de Ingestão (Camada Raw / Bronze)

Na ingestão inicial:
- Os arquivos CSV são carregados integralmente
- Nenhuma lógica de negócio é aplicada
- Os dados são armazenados com seus tipos originais
- Colunas técnicas são adicionadas para controle

### Colunas Técnicas Criadas
- `loaded_at`: timestamp de carga
- `ingestion_timestamp`: controle de ingestão (quando aplicável)

---

## 5. Padronizações Aplicadas

Mesmo na camada Raw, algumas padronizações mínimas são realizadas:
- Padronização de nomes de colunas (snake_case)
- Conversão básica de tipos (datas e numéricos)
- Garantia de encoding consistente (UTF-8)

---

## 6. Ferramentas Utilizadas

- **Dadosfera**: orquestração, ingestão e catalogação
- **Amazon S3**: armazenamento da camada Bronze
- **PostgreSQL**: persistência das camadas Silver e Gold
- **SQL**: manipulação e transformação dos dados

---

## 7. Controle e Observabilidade

Durante a ingestão:
- Cada tabela é validada quanto ao número de registros
- Os dados ingeridos são comparados com os arquivos de origem
- Erros de carga são monitorados via pipelines

---

## 8. Resultado da Integração

Ao final desta etapa:
- Todos os dados brutos estão disponíveis na camada Bronze
- As tabelas estão catalogadas na plataforma
- O pipeline está pronto para evoluir para tratamento e qualidade

---

## 9. Conclusão

A etapa de integração garante a base necessária para todo o fluxo analítico, assegurando rastreabilidade, governança e organização desde a origem dos dados.
