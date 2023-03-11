import re

url = "bytebank.com/cambio"

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")

match = padrao_url.match(url)

if not match:
    raise ValueError("The URL "+url+" is not valid :(")

print("The URL "+url+" is valid :)")

#Problem: Juliana terminou de assistir à aula sobre expressões regulares e
# escreveu o seguinte padrão para validar uma URL:
# “(http(s)?://)?(www.)?bytebank.com(.br)?/cambio”
# Em seguida, testou diversas URLs para ver quais seriam 
# válidas ou não de acordo com o padrão.

#Apos testar URLs temos:

#Validas :)

#https://www.bytebank.com.br/cambio

# Essa URL está de acordo com o formato mais extenso do padrão,
# ou seja, possui todos os grupos que foram declarados como opcionais,
# por exemplo, https, www e .br

#bytebank.com/cambio

# Iniciar com “https://www…” é opcional para o padrão fornecido.

#Nao Validas :(

#bytebank.com.br?/cambio
#https://www.bytebank.com


# Expressões Regulares é um tópico muito extenso na área de computação e muito importante.
# Praticamente toda linguagem de programação possui um conjunto de ferramentas para trabalhar com Expressões Regulares.

# O mais interessante é que, apesar de serem linguagens diferentes, o modo de utilizar vai ser muito parecido com o que vimos:
# estabelecer um padrão (RegEx) e aplicar esse padrão a um texto, ora para extrair o valor que esteja de acordo com o padrão
# fornecido (search), ora para verificar se o texto está de acordo com o padrão (match).

# Se você se interessou pelo assunto e quer se aprofundar ainda mais, a documentação oficial do Python
# tem uma seção de HOWTO (“como fazer”) voltada especificamente em como trabalhar com expressões regulares.
# Ela pode ser acessada através do link: https://docs.python.org/pt-br/3/howto/regex.html#regex-howto

# Como construir e utilizar expressões regulares, ou RegEx utilizando o módulo re do Python.
# Qual a diferença entre search e match.
# O que são quantificadores e intervalos em RegEx.
# A diferença entre parênteses (..) colchetes [...] na construção de padrões.
# Como utilizar expressões regulares para fazer validações complexas.