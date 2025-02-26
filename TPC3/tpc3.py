import re

def markdown_para_html(texto):
    linhas = texto.split("\n")
    html = []
    dentro_lista_ordenada = False

    for linha in linhas:
        linha = linha.strip()

        # Cabeçalhos
        if linha.startswith("###"):
            linha = f"<h3>{linha[3:].strip()}</h3>"
        elif linha.startswith("##"):
            linha = f"<h2>{linha[2:].strip()}</h2>"
        elif linha.startswith("#"):
            linha = f"<h1>{linha[1:].strip()}</h1>"

        # Lista ordenada 
        elif re.match(r"^\d+\.\s+.+", linha):
            if not dentro_lista_ordenada:
                html.append("<ol>")
                dentro_lista_ordenada = True
            linha = re.sub(r"^\d+\.\s+", "<li>", linha) + "</li>"

       
        elif dentro_lista_ordenada:
            html.append("</ol>")
            dentro_lista_ordenada = False

        # Bold (**) e Itálico (*)
        linha = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", linha)  # **texto** -> <b>texto</b>
        linha = re.sub(r"\*(.*?)\*", r"<i>\1</i>", linha)  # *texto* -> <i>texto</i>

        # Imagens
        linha = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', linha)
        
        # Links
        linha = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', linha)

        

        html.append(linha)

   
    if dentro_lista_ordenada:
        html.append("</ol>")

    return "\n".join(html)


md_texto = """# Título Principal
## Subtítulo
### Subsubtítulo
Texto normal

Este é um **exemplo** de texto com *itálico* e **negrito**.

1. primeiro item
2. segundo item
3. terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt).

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com).
"""

html_resultado = markdown_para_html(md_texto)
print(html_resultado)
