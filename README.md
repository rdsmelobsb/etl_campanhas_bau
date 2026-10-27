# Processador e Filtro de Campanhas (ETL de Taxonomia BAU) 📊

Script em Python desenvolvido para automatizar a extração, transformação e carga (ETL) de relatórios consolidados de gestão de campanhas de marketing em formato `.csv`, aplicando filtros de datas e palavras-chave e exportando o resultado final para uma planilha Excel (`.xlsx`).

---

## 🚀 O que este script faz

1. **Ingestão de Dados:** Lê o arquivo original de taxonomia delimitado por ponto e vírgula (`;`) com codificação `utf-8`.
2. **Seleção de Colunas:** Remove a primeira coluna (índice original não utilizado) e seleciona as 13 colunas relevantes seguintes (intervalo `1:14`).
3. **Filtro Temporal:** Localiza e mantém apenas os registros correspondentes aos meses de **outubro de 2025** (`10/2025`) ou **outubro de 2026** (`10/2026`).
4. **Filtro por Segmento:** Filtra apenas as linhas onde a coluna **Campanhas** contenha o termo `"beleza"` (não diferenciando maiúsculas de minúsculas).
5. **Exportação Formatada:** Grava os dados tratados diretamente em um arquivo Excel (`campanhas.xlsx`) sem incluir o índice numérico do DataFrame.

---

## 📋 Pré-requisitos

* **Python 3.8+**
* Bibliotecas necessárias:
  * `pandas` (leitura, manipulação e filtragem dos dados)
  * `openpyxl` (mecanismo necessário para escrita e geração de arquivos `.xlsx`)

---

## 🛠️ Instalação

1. Clone ou baixe os arquivos para o seu computador.
2. Instale as dependências executando no terminal:

```bash
pip install pandas openpyxl
```

---

## 📂 Estrutura de Arquivos

Certifique-se de que o arquivo `.csv` de entrada esteja localizado na mesma pasta do script `etl_csv.py`:

```text
├── etl_csv.py                                                    # Script principal de ETL
├── V2 - GESTAO DE CAMPANHAS - VERSAO FINAL(Taxonomia BAU) (3).csv # Arquivo de dados bruto
├── campanhas.xlsx                                                # Planilha gerada após a execução
└── README.md                                                     # Documentação do projeto
```

---

## ▶️ Como Executar

Execute o script diretamente pelo terminal ou prompt de comando na pasta do projeto:

```bash
python etl_csv.py
```

Assim que a execução for finalizada, será exibida a mensagem:

```text
Tarefa concluída!
```

O arquivo `campanhas.xlsx` estará gerado e disponível para consulta na mesma pasta.

---

## 💡 Customizações e Ajustes Rápidos

Caso precise adaptar os critérios de pesquisa no script:

* **Para alterar os períodos analisados:**  
  Edite as datas na linha de verificação temporal:
  ```python
  df = df[df['Data'].str.contains('10/2025', na=False) | df['Data'].str.contains('10/2026', na=False)]
  ```

* **Para alterar a categoria ou campanha:**  
  Substitua o termo `'beleza'` pelo segmento desejado (ex.: `'tecnologia'`, `'moda'`):
  ```python
  df = df[df['Campanhas'].str.contains('beleza', case=False, na=False)]
  ```
