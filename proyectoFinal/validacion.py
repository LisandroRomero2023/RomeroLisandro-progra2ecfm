import re



def scan(string):
    retorno= string
    patron = re.compile(r'(?:[-+]?\d*\.\d+|[-+]?\d+|if|else|for|while)', re.IGNORECASE)
    matches = patron.findall(string)
    
    textoResaltado = retorno
    for match in set(matches):
            textoResaltado = re.sub(re.escape(match), '|{pal}|'.format(pal=match), textoResaltado)
    return print(textoResaltado)

cadena = ''

while cadena != 'quit()':
    cadena=input('Introduzca la cadena que quiere analizar, para detener el programa escriba quit()\n')
    scan(cadena)
