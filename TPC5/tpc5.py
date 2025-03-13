import json
import datetime
import re

FICHEIRO_STOCK = "stock.json"
MOEDAS_VALIDAS = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}


def carregar_stock():
    try:
        with open(FICHEIRO_STOCK, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_stock(stock):
    with open(FICHEIRO_STOCK, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)


def listar_produtos(stock):
    print("maq:\n cod    |  nome      |  quantidade  |  preço ")
    print("---------------------------------")
    for produto in stock:
        print(f"{produto['cod']:6}  {produto['nome']:12}  {produto['quant']:5}        {produto['preco']}e")


def processar_moedas(entrada):
    moedas = entrada.replace(",", "").replace(".", "").split()  
    saldo = 0
    for moeda in moedas[1:]:  
        moeda = moeda.lower()  
        if moeda in MOEDAS_VALIDAS:
            saldo += MOEDAS_VALIDAS[moeda]
        else:
            print(f"maq: Moeda inválida: {moeda}")
    return saldo

def formatar_saldo(saldo):
    euros = saldo // 100
    centimos = saldo % 100

    if euros > 0 and centimos > 0:
        return f"{euros}e{centimos}c"
    elif euros > 0:
        return f"{euros}e"
    else:
        return f"{centimos}c"


def selecionar_produto(codigo, saldo, stock):
    for produto in stock:
        if produto['cod'] == codigo:
            if produto['quant'] > 0:
                preco = int(produto['preco'] * 100)
                if saldo >= preco:
                    produto['quant'] -= 1
                    saldo -= preco
                    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                    return saldo
                else:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {saldo}c; Pedido = {preco}c")
                    return saldo
            else:
                print(f"maq: Produto esgotado")
                return saldo
    print(f"maq: Produto não encontrado")
    return saldo


def calcular_troco(saldo):
    troco = {}
    for moeda, valor in sorted(MOEDAS_VALIDAS.items(), key=lambda x: -x[1]):
        while saldo >= valor:
            saldo -= valor
            troco[moeda] = troco.get(moeda, 0) + 1
    return troco

def main():
    stock = carregar_stock()
    saldo = 0
    print(f"maq: {datetime.date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        comando = input(">> ").strip().upper()
        
        if comando == "LISTAR":
            listar_produtos(stock)
        elif comando.startswith("MOEDA"):
            saldo += processar_moedas(comando)
            print(f"maq: Saldo = {formatar_saldo(saldo)}")
        elif comando.startswith("SELECIONAR"):
            partes = comando.split()
            if len(partes) == 2:
                saldo = selecionar_produto(partes[1], saldo, stock)
            print(f"maq: Saldo = {saldo}c")
        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            if troco:
                troco_str = ", ".join([f"{v}x {k}" for k, v in troco.items()])
                print(f"maq: Pode retirar o troco: {troco_str}.")
            print("maq: Até à próxima")
            guardar_stock(stock)
            break
        else:
            print("maq: Comando inválido")

if __name__ == "__main__":
    main()
