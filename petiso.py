#Secuencia petisa. Vamos a crear una función que devuelve la secuencia petisa 
#de una palabra. Si no tiene secuencia petisa sólo devuelve un string vacío.
def secuencia_petisa(x):
    #Creamos una lista vacía donde iremos añadiendo las letras B, A, J y O 
    #cuando aparezcan.
    letras = ""
    #Iteramos sobre cada letra en x.
    for letra in x:
        #Si la letra es una de las letras de BAJO, la agregamos a la cadena.
        if letra in "BAJO":
            letras = letras + letra
    if letras == '':
        return ""
        #Si out sigue siendo el empty string, se significa que no apareció 
        #ninguna de las letras necesarias para formar una secuencia petisa.
    else:
        return letras

#Para la función que evalúa si una palabra es petisa o no, nos importa que las 
#letras aparezcan en el orden B, A, J, y O. Si aparecen en este orden, la 
#palabra es petisa.
def es_petiso(x):
    #Creamos un string con la secuencia necesaria para que una palabra sea petisa.
    letras = "BAJO"
    #Inicializamos la posición para seguir el orden de las letras
    position = 0
    #Iteramos sobre cada letra en x.
    for letra in x:
        #Si la letra actual coincide con la letra esperada en el orden, 
        #incrementamos la posición para verificar la siguiente letra en el orden.
        if letra == letras[position]:
            position = position + 1
            #Si llegamos al final del orden, significa que encontramos todas 
            #las letras.
            if position == len(letras):
                return True
    #Si recorremos todas las letras en x y no encontramos el patrón completo, 
    #retornamos False
    return False

#Ahora definiendo la ecuación que te devuelve los strings que son petisos, vamos
#a utilizar la función es_petiso(x).
def solo_petisos(xs):
    #Creamos una lista vacia donde vamos a añadir cada palabra petisa.
    cant = []
    #Iteramos para cada palabra de la lista xs
    for i in xs:
        #La función es_petisa devuelve True si es petisa. Si es True, añadimos 
        #esa palabra a nuestra lista cant
        if es_petiso(i):
            cant.append(i)
    return cant               

#Similar a la función de arriba, ahora definimos una función que cuenta la 
#cantidad de petisos en una lista. Usamos la función solo_petisos(x) en esta función.
def cantidad_petisos(xs):
    return len(solo_petisos(xs))

#Acá queremos saber la densidad de petisos, así que sólo hay que dividir el 
#número de petisos sobre el número total de strings.
def densidad_petisa(xs):
    numerator = cantidad_petisos(xs) #Nos da el número de petisos
    denominator = len(xs) #Acá vemos la cantidad total de strings
    density = round(numerator/denominator, 2)
    return density