# tenho uma lista de textos
#separo as palavras
# coloco em um dict
# faço a busca (textos onde ela aparece)

# ------ função que recebe uma lista de textos e devolve um dicionário----

def separator(textos):
    indice = {}

    count = 0
    for texto in textos:
        texto_separado = texto.split()
        count += 1
        if len(texto_separado) >= 1:
            for palavra in texto_separado:
                if palavra in indice:
                    indice[palavra].append(f'{count}')
                else:
                    indice[palavra] = [f"{count}"]
    return indice

    

        