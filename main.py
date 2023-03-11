url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

#url = " "

#Sanitizacao da URL
#dentro do replace agente vai colocar primeiro o que agente vai procurar no caso a string vazia que tem um caracter
#e no segundo parametro por que queremos substituir a string que seria sem caracter
#url = url.replace(" ","")
#ou ainda mais facil

url = url.strip()


#Validacao da URL
if url == "":
    raise ValueError ("The URL is empty :(")


#Separa base e parametro

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)



#Busca o valor de um parametro

parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&',indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
