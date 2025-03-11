# 📌 Analisador Léxico para Linguagem de Query

## 📅 Data
11/03/2025

## 👤 Autor
- **Nome:** Zita Magalhães Duarte
- **Número de Aluno:** A104268

![Zita Duarte](../zitaduarte.jpeg)

## 📖 Resumo
Este trabalho de casa consiste num analisador léxico implementado em Python.

### 🔹 Funcionamento
1. O analisador percorre a query linha por linha, ignorando comentários e espaços em branco.
2. Os diferentes tipos de tokens são identificados através de expressões regulares.
3. Os tokens reconhecidos incluem:
   - **Palavras-chave:** `SELECT`, `WHERE`, `LIMIT`
   - **Variáveis:** Identificadas por um prefixo `?` (ex: `?nome`, `?desc`)
   - **Prefixos URI:** Prefixos como `dbo:` ou `foaf:` seguidos de um identificador
   - **Literais:** Texto entre aspas duplas, possivelmente com uma tag de idioma (ex: `"Chuck Berry"@en`)
   - **Números:** Sequências numéricas usadas para limites (ex: `1000`)
   - **Operador RDF:** O identificador `a`, usado como operador RDF
   - **Delimitadores:** `{`, `}`
   - **Pontos:** `.`
4. Qualquer caractere inesperado gera um erro de parsing.

## 🛠️ Execução do Programa
O programa pode ser executado diretamente no terminal com o seguinte comando:

```bash
python tpc4.py
```
