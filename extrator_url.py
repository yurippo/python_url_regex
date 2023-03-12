import re

class ExtratorURL:

    def __init__(self,url):        
        self.url = self.sanitiza_url(url)
        self.valida_url()
        

#main method e atributos da nossa class ExtratorURL
#os metodos que comecam com __ como o __init__ sao metodos especiais do python
# nos devs nao chamamos eles diretamente o init eh chamado pelo proprio python
# no inicio do programa para inicializar os valores da instancia da nossa classe

#criamos nosso primeiro metodo que faz a sanitizacao da URL
    def sanitiza_url(self,url):
        if type(url) == str: #por baixo dos panos o python chama o metodo __eq__
         return url.strip()
        else:
           return ""

#Agora criamos o metodo que faz a validacao da URL se ela esta vazia, nao comeca com https:// ou termina com /cambio
#raise ValueError throw exceptions definidas por mim abaixo
# if not bool(self.url) forma pythonica de verificar se uma URL esta vazia ou nao
#Metodo def valida_url() antes das mudancas
    # def valida_url(self):
    #     if not bool(self.url):
    #         raise ValueError ("The URL is empty :(")
    #     elif not (self.url.startswith("https://")):
    #         raise ValueError (f"The URL {self.url} doesn't start with https:// so it is not valid :(")
    #     elif not (self.url.endswith("/cambio")):
    #         raise ValueError (f"The URL {self.url} doesn't end with /cambio so it is not valid :(")

    def valida_url(self):
      if not bool(self.url):
        raise ValueError ("The URL is empty :(")
      padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")

#com o padrao construido o proximo passo e verificar e ver se ele combina com String
# agora eu quero verificar se a String e exatamente o padrao e pra isso vou usar
#o metodo match

      match = padrao_url.match(url)

      if not match:
        raise ValueError("The URL is not valid :(")

    print("The URL is valid :)")           

#Codigo que separa extrai a base e os parametros    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros
    
#codigo que faz a extracao do valor de um parametro daquela URL
    def get_valor_parametro(self,parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&',indice_valor)
        if indice_e_comercial == -1:
          valor = self.get_url_parametros()[indice_valor:]
        else:
           valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    #def get_start_url(self,inicio_url):
        #return self.get_url_base().startswith(inicio_url)
    
    #def get_end_url(self,termina_url):
        #return self.get_url_base().endswith(termina_url)

    #implementamos o metodo def __len__ na nossa classe para podermos imprimir o len do nosso objeto
    def __len__(self):
       return len(self.url)
    
    #agora vamos implementar outro metodo especial o __str__ que e chamado toda vez que damos um print em um objeto
    def __str__(self):
       return self.url +"\n" + "Parametros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()
    
    #aqui nos vamos sobrescrever o metodo __eq__ que diferente dos outro recebe um outro atributo
    #no caso other que seria o objeto a direita da minha comparacao
    #aqui basta retornar se sel.url == other.url ai executo meu programa e ele me retorna True funcionou
    def __eq__(self,other):
       return self.url == other.url
    

 #Agora vamos trabalhar na parte do nosso novo desafio 

# Agora que conseguimos extrair valores da nossa URL como moeda de origem,
# moeda de destino e quantidade de moeda, proponho a você o desafio de realizar essa conversão.

# Modifique o nosso projeto, levando em conta o valor do dólar em real (por exemplo: DOLAR = 5.50),
# para, sabendo o valor do dólar em real (por exemplo: DOLAR = 5.50), ler da URL os 3 parâmetros (origem, destino e quantidade)
# e imprimir na tela o valor da conversão.

# Observação: pode assumir que a moeda de origem e destino será sempre “real” ou “dolar”, ou seja, só faremos a conversão de dólar
# para real e vice-versa.
# Vou deixar algumas linhas de código de exemplo para você começar.

# print("Codigo desafio Conversor def __init__():") #Primeiro codigo que escrevi para o desafio
#agora vou escrever uma funcao para ele

# VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais

# moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
# moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
# quantidade = extrator_url.get_valor_parametro("quantidade")
# valor_convertido = (float(quantidade) * 5.50)

# print("O valor atual 1"+" "+ moeda_origem+" = "+ str(VALOR_DOLAR)+" "+ moeda_destino)
# print("Moeda origem "+moeda_origem) 

# print("Moeda destino "+ moeda_destino)

# print("Quantidade de moeda origem " + quantidade +" "+ moeda_origem)

#print("Valor convertido "+ str(valor_convertido))


# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

    def conversor(self, moeda_origem, moeda_destino,quantidade):
       if (moeda_origem == "real" and moeda_destino == "dolar" and quantidade > 0):
          return quantidade / VALOR_DOLAR
       elif (moeda_origem == "dolar" and moeda_destino == "real" and quantidade > 0):
          return quantidade * VALOR_DOLAR 
       else:
          raise ValueError("Parametros invalidos")       
       
#url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar/cambio"

#extrator_url = ExtratorURL(url)

url ="bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"

extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)

VALOR_DOLAR = 5.50

moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

conversao = extrator_url.conversor(moeda_origem, moeda_destino,float(quantidade))

#print(conversao)

print("Quantidade de moeda: {:.2f} ({})\nValor convertido {:.2f} ({})".format(float(quantidade), moeda_origem, conversao, moeda_destino))

#um metodo especial muito comum de ser utilizado eh o metodo __len__()
#que serve para dizer o tamanho de uma String exemplo

#print(len(url)) #e por debaixo dos panos o python faz url.__len__()

#mas nos queremos imprimir o len do nosso objeto


#Exercicio quem ta certo

# extrator_url_dri = ExtratorURL(url)

# print(id(extrator_url_dri))

# extrator_url_re = ExtratorURL(url)

# print(id(extrator_url_re))

# print("Resultado exercicio Dri ", extrator_url_dri == extrator_url_re)

# print("Resultado exercicio Re",extrator_url_dri.__eq__(extrator_url_re))

# Tanto o código do Renato quanto da Adriana funcionam. 
# Um método especial pode ser chamado como qualquer outro método.
# Por exemplo, fazer obj1 == obj2 é exatamente a mesma coisa que obj1.__eq__(obj2).
# Mas realmente é mais comum deixarmos o interpretador do Python cuidar disso.

print("O tamanho da nossa URL: ", len(extrator_url))
#com  isso aprendemos um pouco mais dos metodos especiais do python __init__ e __len__
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

print(extrator_url)

#Mas o Python me diz que eles nao sao iguais
#E isso acontece pq quando fazemos extrator_url == extrator_url2
# o Python na verdade faz extrator_url.__eq__(extrator_url2) que e tbm metodo especial do Python e abreviacao de equality
# e ele compara o endereco de memoria desses 2 objetos que realmente nao sao iguais
# nos queremos sobreescrever esse metodo de forma que se esses 2 objetos tiverem o mesmo atributo
# no nosso caso a mesma url eu gostaria que eles fossem considerados iguais
# pra isso vamos seguir a mesma estrategia do len e do str 
print(extrator_url == extrator_url2)

#extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

#Isso daqui e o que agente chama de interface da nossa classe 
#quais sao os metodos, como eles sao, o que eles recebem
#pra gente conseguir trabalhar com ela

#print(type(None))

#extrator_url = ExtratorURL(None)

#extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)

#nesse projeto agente melhorou muito a nossa validacao de URL e agente aprendeu que
#pode usar regex pra isso e aprendeu dentro de regex utilizar () ao invez de [] para
#quando quero definir o padrao exato de caracteres e tbm aprendemos o novo objeto
#do metdo pattern que e o match ele vai verificar se a minha String bate exatamente
#com aquele padrao
#logo usamos o metodo search quando queremos buscar um padrao em uma String inteira
#e o match para verificar se uma String inteira bate com aquele padrao

#o metodo id do Python nos permite imprimIr o endereco de memoria do objeto
# print(id(extrator_url))
# print(id(extrator_url2))
# ao fazermos o print(id()) vemos que os objetos tem posicoes diferentes em memoria
#2766541570000
#2766541572704
#e por isso sao objetos diferentes e com enderecos diferentes
#No Python os objetos podem ser iguais mas nao identicos

# Neste projeto, aprendemos:
#O formato de URLS e seus formatos na internet
#Pq que nosso objetivo era justamente extrair os parametros de uma URL para a nossa pagina
#de conversao de moedas
#Agente aprendeu um pouco tbm sobre o fatiamento de URLs e como eles geram uma nova URL sem modificar
#a String original e com isso agente aprendeu mais tabem sobre a imutabilidade de Strings do Python
#Tambem vimos que a classe String oferece diversos metodos e que agente pode consultar a documentacao
#Ou inspecionar a propria classe usando um editor de texto como o PyCharm ou o VS Code pra saber
#quais sao estes metodos e o que eles fazem
#tbm pegamos o nosso codigo que estava nao muito estruturado e extraimos ele e construimos uma classe
#com a responsabilidade de extrair os valores de uma URL utilizando boas praticas de orientacao a objetos
#Tambem aprendemos sobre expressoes regulares our Regex pra verificar se uma String tem um determinado
#padrao dentro dela ou se uma String esta de acordo com certo padrao
#e agente utilizou isso pra melhorar a nossa validacao de URL
#por fim aprendemos mais sobre metodos especiais do Python e como eles funcionam por baixo dos panos
#metodos que comecam com dois __ e terminam com __
#como o __init__ o __eq__ e tbm o metodo __len__ por exemplo
#e muito importante fazer todos os exercicios e challenges do curso
#e usar o forum pra perguntar e responder perguntas pra fortalecer meu conhecimento



# Métodos especiais são chamados pelo próprio interpretador Python de acordo com alguma instrução
# Como implementar métodos especiais em nossas classes para criar comportamentos customizados
# A diferença entre igualdade (==) e identidade (is)


     




   

