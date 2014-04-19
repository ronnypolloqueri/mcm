# -*- encoding:utf-8 -*-
import math
#n = int(input("Cantidad de cifras: ")) # 2 por defecto
#x0 = int(input("Ingrese la semilla:")) #valor de inicio
#print "La semilla %s"%str(x0)

def num2numeros_medios(numero):
    cadena_split='error'
    size_x = str(numero).__len__()
    is_par = (numero%2==0)

    cadena = str(numero*numero)
    size_y = cadena.__len__()

    if is_par: # si xi es par
        if( size_y % 2 == 1): # yi es impar
            cadena = '0' + cadena
            cadena_split = cadena[((size_x/2)):-(size_x/2)]
        else: # yi es par
           # cadena_split = cadena[((size_x-1)/2):-((size_x-1)/2))]
            cadena_split = cadena[((size_x/2)+1):-(size_x/2)]


    else:   # si xi es impar
        if( size_y % 2 == 0): # yi es par
            cadena = '0' + cadena
            print numero
        #    cadena_split = cadena[2:-2]

        else: # yi es impar
            cadena_split = cadena[((size_x-1)/2):-((size_x-1)/2)]
            
    return cadena_split

def prueba(num):
    print "%s\t%s\t\t\%s"%(num,
                        num*num,
                        num2numeros_medios(num))
prueba(123)
prueba(999)
prueba(1234)
prueba(9999)


