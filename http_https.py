# HTTP: Entendendo a web por baixo dos panos

# O que e HTTP?

# Esse curso focará nesse protocolo tão presente no dia a dia do usuário e do desenvolvedor.

# Iremos abordar tópicos como o HTTPS, que é a web segura, entendendo que o HTTP trafega texto puro,
# já o HTTPS trafega o texto criptografado, e como isso tudo funciona por baixo dos panos.

# Veremos também sobre endereços, incluindo domínios, recursos e portas.

# Além disso, estudaremos sobre sessão, cookie e o modelo de requisição e resposta do HTTP,
# mais ainda os parâmetros que são enviados na requisição, seja no seu corpo ou na URL.

# Comentaremos também sobre os serviços REST, já que o HTTP não roda somente no browser,
# ele também roda no seu aplicativo mobile. Veremos como implementar essa comunicação, que tipo de verbo o HTTP utiliza.

# Por último, veremos sobre a nova versão do HTTP, o HTTP2, e o que ele adicionou de melhorias e otimizações que ele realiza para nós.

# Focaremos nas regras de comunicação da web.

# Quando se fala em HTTP, o primeiro pensamento que vem a nossa mente é sobre a utilização da internet,
# é o cenário onde vemos realmente na prática a utilização do HTTP. Nós acessamos sites em que seus endereços
# iniciam com http:// e por isso precisamos conhecer o que realmente está acontecendo ao fazer isso.

# No momento em que acessou este curso, esta aula, entre o navegador e a Alura aconteceu uma comunicação,
# e esta comunicação tem duas partes bem conhecidas que chamamos de Client-Server ou em português Cliente-Servidor.
# Este é um modelo arquitetural, ou seja, a internet inteira é baseada nesta arquitetura onde há um cliente que solicita
# e um servidor que responde.

# Em qualquer comunicação é preciso existir algumas regras para que as duas partes consigam se entender com sucesso.
# Pensando na comunicação do seu navegador entre a Alura ou algum outro site esse conjunto de regras é basicamente um
# protocolo, onde neste cenário é o HTTP.

# Os protocolos são definidos, especificados e disponibilizados para implementação em ambas as partes, para consultar
# a especificação do HTTP - Hypertext Transfer Protocol, você pode utilizar o seguinte endereço: https://tools.ietf.org/html/rfc2616

# Resumindo: O HTTP é um protocolo que define as regras de comunicação entre cliente e servidor na internet
# Na internet sempre tem um cliente e um servidor
# Entre o cliente e o servidor precisam haver regras de comunicação
# As regras são definidas dentro de um protocolo
# HTTP é o protocolo mais importante na internet

# Peer-To-Peer

# Você já usou torrent para baixar algum arquivo na internet?
# Caso sim, aproveitou um outro modelo de comunicação, o P2P ou Peer-To-Peer!

# O modelo Cliente-Servidor não é o único modelo de comunicação na rede,
# nem sempre o mais adequado. Por exemplo, imagine que precisemos contar as
# letras de 20 palavras. No caso do modelo Cliente-Servidor, quem fará esse trabalho
# é o servidor, certo? E se precisar contar as letras de 1 milhão de palavras? Muito trabalhoso para o servidor, não?

# O modelo Cliente-Servidor tenta centralizar o trabalho no servidor, mas isso também pode gerar gargalos.
# Se cada Cliente pudesse ajudar no trabalho, ou seja, assumir um pouco da responsabilidade do servidor, seria
# muito mais rápido. Essa é a ideia do P2P! Não há mais uma clara divisão entre Cliente-Servidor, cada cliente
# também é servidor e vice-versa!

# Isto é útil quando você precisa distribuir um trabalho ou necessita baixar algo de vários lugares diferentes. Faz sentido?

# Usando algum aplicativo de Torrent, o protocolo utilizado não é o HTTP, e sim o protocolo P2P, como BitTorrent ou Gnutella.

# Arquitetura da Alura

# Agora já sabemos que existe um cliente, o navegador, como Chrome e Firefox, e um servidor, a Alura.
# Para definir as regras de comunicação entre cliente e servidor, existe o protocolo HTTP.

# Também já sabemos que o servidor usa alguma plataforma, como PHP, Java, .Net ou outros.
# Qual plataforma realmente é utilizada? Não é tão fácil de descobrir, pois o HTTP, de propósito,
# não está focado em alguma plataforma específica e esconde isso de nós. Bom, eu não vou esconder
# nada e vou contar para vocês que a Alura usa a plataforma Java e o servidor concreto se chama Tomcat.

# Também já falamos que o SQL é uma linguagem para consultar o banco de dados. Alura usa SQL para acessar
# o banco de dados MySQL.

# Com essas informações já temos uma breve ideia da arquitetura da Alura!

#Cliente  <--- HTTP ---> Servidor Java  <--- SQL ---> Banco de dados

#O que você aprendeu nesse capítulo?

# A arquitetura Cliente-Servidor
# Um protocolo é um conjunto de regras
# HTTP é um protocolo que define as regras de comunicação entre cliente e servidor na internet.
# HTTP é o protocolo mais importante da Internet

# HTTPS - A versão segura do HTTP