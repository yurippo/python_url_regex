import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

#codigo antigo padrao muito longo
#padrao = re.compile ("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
#eu uso o ponto de interrogacao pra dizer que o caracter e opcional

#Novo codigo ao invez de escrever [0123456789] 5 vezes e depois da interrogacao [0123456789] e vezes  
#eu simplesmente escrevo [0123456789]{5} e [0123456789]{3}

#padrao = re.compile ("[0123456789]{5}[-]?[0123456789]{3}")

#E ainda uma forma ainda mais simplicada de escrever meu codigo seria ao invez de escrever [0123456789] escrever [0-9] o conjunto poderia ser letra tbm
#exemplo [a-z]
#perceba que agora o nosso esta muito mais simples e parecido com a forma que falamos ele no dia a dia

#padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

#E por fim posso tambem ao invez de utilizar ? para o traco colocar um intervalo tambem e o nosso codigo ficara da seguinte forma e continua funcionando

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)

#e isso aqui no Python vai retornar o objeto match tipo especifico que diz se encontrou aquela combinacao

#e esse metodo search pode retornar duas coisas ou o objeto Match ou ele retorna None caso o padrao nao seja encontrado
if busca == True:
 cep = busca.group() #o metodo group vai retornar exatamente a String que foi encontrada no Match
 print(cep)

else:
 print(busca)



# Regular Expression --RegEx
#Modulo do Python pra trabalhar com expressoes regulares
# 5 digitos + hifen (opcional) + 3 digitos
#pra gente conseguir validar um texto que possui um certo padrao 
#precisamos utilizar expressoes regulares agora vamos trabalhar com
#uma aplicacao de cadastro de usuario onde agente quer so buscar o cep
#de um usuario em um endereco fornecido vamos extrair o cep daquele usuario

#Agora vamos usar o metodo compile() do modulo re e vamos passar o nosso padrao da seguinte maneira fazemos desse jeito para criar um padrao
#No Python

#com o nosso padrao criado agora o proximo passo e buscar em uma String ou um texto se esse padrao foi encontrado
# para isso vamos criar uma variavel busca e vou utilizar o metodo do proprio objeto pattern (objeto retornado pelo compile) para 
# ou seja o metodo search que vai buscar em uma String o padrao

#Geralmente agente vai seguir esses 3 passos:
#-A compilacao de um padrao
#-A busca por esse certo padrao em uma String
#-Caso essa busca retorne alguma coisa agente extrai da busca do objeto Match aquela String que bateu