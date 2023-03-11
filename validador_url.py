import re

url = "www.bytebank.com.br/cambio"


#quando eu uso [] eu digo pro Python que pode conter alguns desses caracteres
#quando eu uso () como nesse caso to dizendo pro Python que os caracteres tem que ser exatamente esses
#usamos depois a ? pq sabemos que https:// e opcional isso quer dizer que pode comecar com https:// ou nao
#colocamos novamente um ponto de ? pq sabemos que o www. pode aparecer ou nao e se aparecer tem que ser exatamente isso
#ai vamos ter o bytebank.com que tem que ter e o (.br) opcional por isso entre parenteses
#ae seguimos com a / que e a barra pra minha pagina escrito cambio
#e por fim famos colocar o s entre parenteses http(s)? e um ponto de interrogacao pq pode ser http ou https

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")

#com o padrao construido o proximo passo e verificar e ver se ele combina com String
# agora eu quero verificar se a String e exatamente o padrao e pra isso vou usar
#o metodo match

match = padrao_url.match(url)

if not match:
    raise ValueError("The URL "+url+" is not valid :(")

print("The URL "+url+" is valid :)")


#perfeito o codigo esta funcionando bem agora o que temos que fazer
#e leva-lo para o metodo def valida_url() da nossa classe ExtratorURL

# Exemplos de URLs válidas:

# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio
# https://www.bytebank.com.br/cambio

# Exemplos de URLs inválidas:

# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio