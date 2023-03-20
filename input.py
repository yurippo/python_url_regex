usuario = input("Insira seu login: ")
print(f"Ola, {usuario}")

# A função raw_input() no Python 2
# No Python 2, em vez da função input(), utilizamos a função raw_input() para pegar a entrada do
# usuário como string, veja exemplo Python 2:

# usuario = raw_input(‘Insira seu login: ‘)
# print(‘Olá, ‘ + usuario)

# No Python 3, a função raw_input() foi simplesmente renomeada para input()

# O que fazer a respeito da diferença de versões?
# Como você deve ter percebido, há uma inconsistência aqui - se quisermos capturar
# uma entrada do usuário como string, não há um código único que simplesmente satisfaça 
# ambas as versões 2 e 3 do Python.

# Nesse momento, nós, como programadores, devemos tomar uma decisão 
# pensando nos benefícios de cada versão do Python e, principalmente, na maioria de nossos usuários.

# "Mas e se eu precisar que o meu programa funcione em qualquer das duas versões?"

# Se quisermos dar uma volta nessa incompatibilidade, é possível checar a versão do
# Python através do atributo version_info.major do módulo sys, o que nos dá a possibilidade de criar
# uma condição if e ficar em cima do muro, como no exemplo:

# import sys

# if sys.version_info.major == 2:
#     usuario = raw_input(‘Insira seu login: ‘)
# elif sys.version_info.major == 3:
#     usuario = input(‘Insira seu login: ‘)
                    
# O perigo de executar uma entrada do usuário
# É importantíssimo notar o quão perigosas são as
# funções input() no Python 2 e eval() em ambas as versões!

# Executar algo digitado pelo usuário abre uma tremenda brecha na segurança
#  do programa e até do computador em que o programa está sendo utilizado.

# Veja nesse artigo de Ned Batchelder um pouco mais dos perigos do eval(). Um simples exemplo:

# eval("os.system(‘ls /’)")
# Isso listaria os arquivos no diretório raiz de nosso computador.

# E se, em vez de listar, usássemos o comando de deletar? Todos os arquivos e
#  diretórios de nosso computador seriam apagados, sem mais nem menos!

# Por isso, sempre devemos lembrar de tomar cuidado ao executar uma entrada do usuário.

# Conclusão
# Nesse post, aprendemos as diferenças entre as funções raw_input() e input(), como isso
#  muda do Python 2 para o Python 3 e até um pouco sobre eval() e seus perigos!