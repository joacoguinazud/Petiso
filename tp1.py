#Importando las ecuaciones creadas en el otro archivo
from petiso import secuencia_petisa
from petiso import es_petiso
from petiso import solo_petisos
from petiso import cantidad_petisos
from petiso import densidad_petisa

print("""Funciones disponibles
---------------------
A. Secuencia petisa [x]
B. Es petiso [x]
C. Solo petisos [xs]
D. Cantidad petisos [xs]
E. Densidad petisos [xs]
F. Finalizar
""")
opcion = input('Seleccione una opción: ').upper().strip()
#Mientras la opción no sea F, vamos a seguir queriendo ver el menu. Si el
#usuario elige F, el while loop no funciona y se termina la ejecución
while opcion != 'F':
    if opcion == 'A':
        palabra = input('Ingrese x: ')
        secuencia = secuencia_petisa(palabra)
        if secuencia == "":
            print(palabra + " no tiene una secuencia petisa.")
        else:
            print("La secuencia petisa de " + palabra + " es " + secuencia + ".")
    elif opcion == 'B':
        palabra = input('Ingrese x: ')
        petiso = es_petiso(palabra)
        if petiso:
            print(palabra + " es petiso.")
        else:
            print(palabra + " no es petiso.")
    elif opcion == 'C':
        palabra = input('Ingrese xs: ')
        cant = solo_petisos(palabra.split(", "))
        if cant == []:
             print("Aquí no hay petisos.")
        elif len(cant) == 1:
            print("Aquí hay un petiso: " + cant[0] + ".")
        else:
            out = ''
            #Iteramos el vector donde están todas las palabras petisas y las vamos
            #añadiendo a un string
            for j in cant[:-1]:
                out = out + j + ', '
            print("Aquí hay varios petisos: " + out + cant[-1] + ".")
    elif opcion == 'D':
        palabra = input('Ingrese xs: ')
        out = cantidad_petisos(palabra.split(", "))
        if out == 0:
            print('Aquí hay 0 petisos.')
        elif out == 1:
            print('Aquí hay un petiso.')
        else:
            print('Aquí hay ' + str(out) + ' petisos.')
    elif opcion == 'E':
        palabra = input('Ingrese xs: ')
        density = densidad_petisa(palabra.split(", "))
        print('La densidad petisa es ' + str(density))
    else:
        print('Opción inválida. Seleccione de nuevo.')
    input("""
Presione ENTER para continuar.""")
    print("""
Funciones disponibles
---------------------
A. Secuencia petisa [x]
B. Es petiso [x]
C. Solo petisos [xs]
D. Cantidad petisos [xs]
E. Densidad petisos [xs]
F. Finalizar
""")
    opcion = input('Seleccione una opción: ').upper().strip()
  