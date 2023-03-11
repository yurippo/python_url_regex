# O nosso primeiro passo é conseguir extrair os valores das variáveis url_base
#  e url_parametros dinamicamente, utilizando o método find para encontrar o índice
#  do caractere ?

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

# Em seguida, temos que definir qual parâmetro vai ter o seu valor extraído.
# Por exemplo, para utilizarmos o parâmetro quantidade precisamos encontrar
# o índice desse parâmetro na string url_parametros e, a partir desse índice,
# somar o tamanho do parâmetro + 1 (por causa do sinal de =):

parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1


# Se nossa URL tivesse apenas 1 parâmetro, poderíamos fatiar a partir daí,
#  mas vimos que para o caso de múltiplos parâmetros separados por “&” 
# (diz-se: “e comercial”), precisamos verificar se tem um “&” depois ou não:

indice_e_comercial = url_parametros.find("&",indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

# Uma string é uma cadeia de caracteres onde cada caractere tem sua própria posição ou índice.
# Podemos omitir o primeiro ou o segundo argumento do operador de fatiamento para fatiar uma string do início até um certo índice, ou a partir de um índice até o final. Exemplo: str[a:] ou str[:b].
# Podemos utilizar o método str.find(palavra, inicio) para buscar o índice de palavra a partir de inicio.
# Caso palavra não seja encontrada, o método find retorna -1.
# O método len(string) retorna o tamanho (ou seja, a quantidade de caracteres) da nossa string.
# Dica: o caractere que representa espaço em branco (“ “) também conta! Por exemplo: len(" ") retorna 1.