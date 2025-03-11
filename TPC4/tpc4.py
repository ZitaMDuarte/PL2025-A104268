import re


PALAVRAS_CHAVE = {"SELECT", "WHERE", "LIMIT"}


VARIAVEL_REGEX = re.compile(r'\?[a-zA-Z_][a-zA-Z0-9_]*')
PREFIXO_URI_REGEX = re.compile(r'[a-zA-Z]+:[a-zA-Z_][a-zA-Z0-9_]*')
LITERAL_REGEX = re.compile(r'"([^"\\]*(\\.[^"\\]*)*)"(?:@[a-zA-Z]+)?')
NUMERO_REGEX = re.compile(r'\d+')
OPERADOR_RDF_REGEX = re.compile(r'\ba\b')  # "a" como operador RDF
IDENTIFICADOR_REGEX = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')

def tokenize(query):
    
    tokens = []
    linhas = query.splitlines()
    linha_atual = 0

    for linha in linhas:
        linha_atual += 1
        linha = linha.strip()

    
        if linha.startswith("#") or linha == "":
            continue
        
        i = 0
        while i < len(linha):
            char = linha[i]

    
            if char.isspace():
                i += 1
                continue

    
            if char in "{}":
                tokens.append(("DELIMITADOR", char))
                i += 1
                continue

      
            if char == ".":
                tokens.append(("PONTO", char))
                i += 1
                continue

            match = VARIAVEL_REGEX.match(linha[i:])
            if match:
                tokens.append(("VARIAVEL", match.group()))
                i += len(match.group())
                continue


            match = PREFIXO_URI_REGEX.match(linha[i:])
            if match:
                tokens.append(("PREFIXO_URI", match.group()))
                i += len(match.group())
                continue

            match = LITERAL_REGEX.match(linha[i:])
            if match:
                tokens.append(("LITERAL", match.group()))
                i += len(match.group())
                continue


            match = NUMERO_REGEX.match(linha[i:])
            if match:
                tokens.append(("NUMERO", match.group()))
                i += len(match.group())
                continue


            match = OPERADOR_RDF_REGEX.match(linha[i:])
            if match:
                tokens.append(("OPERADOR_RDF", match.group()))
                i += len(match.group())
                continue


            match = IDENTIFICADOR_REGEX.match(linha[i:])
            if match:
                valor = match.group()
                tipo = "PALAVRA_CHAVE" if valor.upper() in PALAVRAS_CHAVE else "IDENTIFICADOR"
                tokens.append((tipo, valor))
                i += len(valor)
                continue


            print(f"Erro: caractere inesperado '{char}' na linha {linha_atual}")
            i += 1  

    return tokens


query = ''' 
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
'''

tokens = tokenize(query)

print("Tokens reconhecidos:")
for token in tokens:
    print(token)
