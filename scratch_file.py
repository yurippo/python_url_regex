

def foo(valor):
    if valor:
        print("Valor e verdadeiro")
    else:
        print("Valor e falso")    

foo("")
foo(None)

print(bool(""))

print(bool("abcdefgh"))


#se precisarmos saber os metodos presentes na classe str podermos usar o metodo dir para isso

print(dir(str))

#que nos retornara
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#Inclusive, se soubermos o nome do método que estamos procurando, podemos verificar se ele está nessa lista utilizando o operador in:
#Verifica se o método __len__ existe na classe str
print('__len__' in dir(str))  
#que no caso retorna True

#todo o objeto do Python implementa o metodo
#__str__ esse e o metodo que eh chamado quando agente da print em um objeto

print(1 == True) #printando abaixo podemos ver que o 1 e o True nao estao no mesmo endereco de memoria mas pq retorna True entao?

print(id(1))
print(id(True))

#para podermos identificar se a identidade do objeto e a mesma devemos utilizar is True
#se eles estao no mesmo endereco de memoria

print(1 is True) #agora podemos ver que o resultado retornou False
#pq eles nao sao exatamente a mesma coisa eles nao tem a mesma identidade

#todos os metodos especiais funcionam da mesma maneira sao metodos que sao chamados indiretamente
#no Python podemos dizer que 2 objetos sao iguais mas nao necessariamente identicos
#para isso podemos utilizar o metodo id() para verificar o endereco de memoria daquele objeto
# ou o is tbm pra verificar se 2 objetos sao realmente identicos e nao apenas iguais

#is vs ==

# Luciano, querendo reforçar o que aprendeu sobre a diferença
# entre os operadores is e ==, abriu o Python Console de sua IDE
# e testou diversas comparações. As alternativas abaixo contêm os
# testes que Luciano fez, selecione todas cuja expressão retorne True:

print("Printando Exercicio is vs ==")

print(0 == False) #retorna True
# No Python, 0 e False são considerados valores iguais (não idênticos, logo, 0 is False retornaria False).

print(1 == True) #retorna True
# No Python, 1 e True são considerados valores iguais (não idênticos, logo, 1 is True retornaria False).

print(bool("")is False) #retorna True
# O retorno de bool(“”) é False (pois ”” é considerado um valor falso). Assim, False is False retorna True.

print(None == False) #retorna False
# Apesar de None ser considerado um valor falso (em um if, por exemplo), None não é igual a False.

print("" == False) #retorna False
# Apesar de a string vazia (””) ser considerada um valor falso (em um if, por exemplo), ”” não é igual a False.

# O instrutor Yan escreveu um artigo no blog da Alura falando um pouco mais sobre a diferença entre utilizar o
# operador is (identidade) e o operador == (igualdade) no Python. Se você quiser aprender ainda mais sobre esse
# assunto, vale a pena conferir!
# https://www.alura.com.br/artigos/qual-a-diferenca-entre-e-is-no-python