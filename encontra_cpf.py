import re

# Depois de assistir ao vídeo sobre extração do CEP de um endereço, 
# Rafaela teve a ideia de fazer uma pequena aplicação que extraísse
# o CPF do usuário a partir de um texto. O texto é o seguinte:

endereco = "Rafaela Brasil, CPF: 718.457.190-85"

#Primeira forma possivel de achar o CPF de Rafaela na String
# Apesar de ser redundante colocar o {1} após o grupo [.], 
# nossa expressão continua sendo válida. Além disso, também podemos
# optar por expressar [0-9] explicitamente como [0123456789], apesar de deixar nosso padrão menos legível nesse caso.
#padrao = re.compile("[0-9]{3}[.]{1}[0-9]{3}[.]{1}[0-9]{3}[-]{1}[0123456789]{2}")

#E eis a segunda forma possivel de achar o CPF de Rafaela na String
# Estamos utilizando os quantificadores ,{3} e {2}, e intervalos [0-9] 
# para simplificar o nosso padrão.

padrao = re.compile("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}")

busca = padrao.search(endereco)

if busca == True:
    cpf = busca.group()
    print(cpf)
else:
    print(busca)