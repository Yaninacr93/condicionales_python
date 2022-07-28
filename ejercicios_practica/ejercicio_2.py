# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('{} es mayor alfabeticamente que {}'.format(texto_1,texto_2))
else:
    print('{} es mayor alfabeticamente que {}'.format(texto_2,texto_1))

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1)>len(texto_2):
    print ('{} contiene mayor cantidad de letras que {}'.format(texto_1,texto_2))
elif len(texto_1)<len(texto_2):
    print ('{} contiene mayor cantidad de letras que {}'.format(texto_2,texto_1))
else:
    print ('{} contiene la misma cantidad de letras que {}'.format(texto_2,texto_1))


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

primera_letra_texto_1 = texto_1 [0]
primera_letra_texto_2 = texto_2 [0]

if primera_letra_texto_1 > primera_letra_texto_2:
    print('La primera letra de la primera pablara ({}) es mayor que la primera letra de la segunda palabra ({})'.format(primera_letra_texto_1,primera_letra_texto_2))
elif primera_letra_texto_1 < primera_letra_texto_2:
    print('La primera letra de la segunda pablara ({}) es mayor que la primera letra de la primera palabra ({})'.format(primera_letra_texto_2,primera_letra_texto_1))
else:
    print('La primera letra de ambas palabras son iguales alfabeticamente')


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if  texto_1 == copia_texto_1:
    print('{} es igual a {}'.format(texto_1,copia_texto_1))
if  texto_2 != copia_texto_1:
    print('{} es distinto a {}'.format(texto_2,copia_texto_1))
 
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
