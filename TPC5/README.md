# 📌 Máquina de Vending - Analisador de Stock

## 📅 Data
13/03/2025

## 👤 Autor
- **Nome:** Zita Magalhães Duarte
- **Número de Aluno:** A104268

![Zita Duarte](../zitaduarte.jpeg)

## 📖 Resumo
Este projeto implementa um simulador de uma máquina de vending que aceita moedas, permite selecionar produtos e devolve o troco, gerindo o stock dos produtos através de um ficheiro JSON.

### 🔹 Funcionamento:
1. O stock dos produtos é carregado a partir de um ficheiro JSON (`stock.json`).
2. O utilizador pode inserir moedas, selecionar produtos e retirar troco.
3. A máquina mantém um saldo interno e atualiza o stock quando um produto é comprado.
4. O saldo é apresentado de forma formatada, por exemplo: `1e30c` em vez de `130c`.
5. Ao sair do programa, o stock atualizado é guardado no ficheiro JSON.

---

## 🔧 Comandos Disponíveis

- `LISTAR` → Lista todos os produtos disponíveis na máquina, com código, nome, quantidade e preço.
- `MOEDA <valores>` → Insere moedas na máquina (moedas aceites: `1e, 50c, 20c, 10c, 5c, 2c, 1c`).
- `SELECIONAR <código>` → Escolhe um produto pelo código (`A23`, `B45`, etc.).
- `SAIR` → Devolve o troco e termina o programa.

---

## 🛠️ Execução do Programa

1. Criar um ficheiro `stock.json` com o stock.
2. Executamos usando o comando:
`python3 tpc5.py stock.json`



