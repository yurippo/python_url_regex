empty_url = (len(""))

print(empty_url)

space_url = (len(" "))

print(space_url)

if empty_url == space_url:
    print("TRUE")
else:
    print("FALSE")

#novo teste utilizando function replace da String Class to remove all the spaces from the string

texto = "          a    "

print(texto)

texto_clean = texto.replace(" ","")

print(texto_clean)

#novo teste utilizando function strip da String Class to remove all the spaces from the string

texto_to_strip ="       a           "
print(texto_to_strip)

texto_to_strip_ready = texto_to_strip.strip()
print(texto_to_strip_ready)

#novo teste stripping URL

url = "\twww.alura.com"
print(url)