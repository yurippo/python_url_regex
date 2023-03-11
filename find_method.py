url = "https://www.alura.com.br/curso?curso=python"
print(url)
indice_curso = url.find("curso")
print(indice_curso)

indice_valor = indice_curso + len("curso") + 1
print(indice_curso)
valor = url[indice_valor:]
print(valor)

# Mas O programa da Mariana tem um bug,
# ela esqueceu de considerar que a palavra "curso"
# aparece duas vezes na URL

#Resolvendo o bug

indice_curso = url.find('=')
indice_valor = indice_curso + len('=')
valor = url[indice_valor:]

print(valor)

#Ou

# url = "https://www.alura.com.br/curso?curso=python"

# indice_curso = url.find('python')
# indice_valor = indice_curso + len('curso') +1

# if indice_valor == -1:
#     valor = url[indice_valor:]
# else:
#     valor = url[indice_curso:indice_valor]

#     print(valor)