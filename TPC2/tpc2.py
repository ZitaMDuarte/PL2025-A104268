import re

def corrigir_csv(ficheiro):
    """Corrige o CSV removendo quebras de linha dentro de descrições entre aspas e retorna o conteúdo corrigido como lista de linhas."""
    
    with open(ficheiro, "r", encoding="utf-8") as f:
        conteudo = f.read()

    
    while True:
        conteudo_corrigido, num_substituicoes = re.subn(r'(".*?)(\r?\n\s+)(.*?")', r'\1 \3', conteudo, flags=re.DOTALL)
        if num_substituicoes == 0:
            break  
        conteudo = conteudo_corrigido  

    
    return conteudo_corrigido.split("\n")


def extrair_compositores(linhas_corrigidas):
    """Extrai corretamente os compositores do CSV e retorna uma lista ordenada alfabeticamente."""
    
    compositores = set()  

    for linha in linhas_corrigidas[1:]:  
        campos = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', linha.strip())  
        
        if len(campos) >= 5:  
            lista_compositores = campos[4].strip() 
            
            if lista_compositores: 
                compositores.add(lista_compositores)

    
    lista_ordenada = sorted(compositores)

    return lista_ordenada

def contar_obras_por_periodo(linhas_corrigidas):
    """Conta quantas obras existem por período e retorna um dicionário com a distribuição."""

    distribuicao = {}  

    for linha in linhas_corrigidas[1:]:  
        campos = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', linha.strip()) 

        if len(campos) > 3:  
            periodo = campos[3].strip()  

            if not periodo.isdigit():  
                if periodo not in distribuicao:
                    distribuicao[periodo] = 0  
                distribuicao[periodo] += 1

    return dict(sorted(distribuicao.items()))  

def obter_obras_por_periodo(linhas_corrigidas):
    """Cria um dicionário onde cada período está associado a uma lista alfabética das obras desse período."""
    
    obras_por_periodo = {} 

    for linha in linhas_corrigidas[1:]:  
        campos = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', linha.strip())  

        if len(campos) > 3:
            titulo = campos[0].strip()  
            periodo = campos[3].strip()  

            if titulo and periodo and not periodo.isdigit():  
                if periodo not in obras_por_periodo:
                    obras_por_periodo[periodo] = []  
                obras_por_periodo[periodo].append(titulo)

    
    return {periodo: sorted(obras) for periodo, obras in sorted(obras_por_periodo.items())}



ficheiro_csv = "obras.csv"
linhas_corrigidas = corrigir_csv(ficheiro_csv)


compositores_lista = extrair_compositores(linhas_corrigidas)
distribuicao_periodos = contar_obras_por_periodo(linhas_corrigidas)
obras_por_periodo = obter_obras_por_periodo(linhas_corrigidas)



print(f"Lista de Compositores:")
for compositor in compositores_lista:
    print(f"Compositor: {compositor}")

print(f"\n")

print(f"Número de obras em cada Período:")
for periodo, quantidade in sorted(distribuicao_periodos.items()):
    print(f"{periodo}: {quantidade}")

print(f"\n")

print(f"Lista das obras por período:")
for periodo, obras in obras_por_periodo.items():
    print(f"\n{periodo}:")
    for obra in obras:
        print(f"  - {obra}")
