# -*- encoding:utf-8 -*-
import math
#n = int(input("Cantidad de cifras: ")) # 2 por defecto
#x0 = int(input("Ingrese la semilla:")) #valor de inicio
#print "La semilla %s"%str(x0)

def verificar(str_num_mc):
    numero = int(str_num_mc)
    size = str_num_mc.__len__()
    i = 0
    while(i < size and str_num_mc[i]=='0'):
        i+=1
        
    if i == size:
        return 'caso exceptional'
    else:
        return numero/math.pow(10,size)


def num2numeros_medios(numero, size_x):
    cadena_split='error'
    #size_x = str(numero).__len__()
    x_size_is_par = (size_x%2==0)

    cadena = str(numero*numero)
    size_y = cadena.__len__()

    if x_size_is_par: # si size_x es par
        if( size_y % 2 == 1): # yi es impar
            cadena = '0' + cadena
            cadena_split = cadena[((size_x/2)):-(size_x/2)]
        else: # yi es par
           # cadena_split = cadena[((size_x-1)/2):-((size_x-1)/2))]
            cadena_split = cadena[((size_x/2)):-(size_x/2)]


    else:   # si size_x es impar
        if( size_y % 2 == 0): # si size y es par
            cadena = '0' + cadena
            cadena_split = cadena[((size_x+1)/2):-((size_x+1)/2)]

        else: # yi es impar
            cadena_split = cadena[((size_x-1)/2):-((size_x-1)/2)]

    return cadena_split



def prueba(num):
    print "%s\t%-10s\t\%s\t%s"%(num,
                        num*num,
                        num2numeros_medios(num,str(num).__len__()), 
                        verificar(num2numeros_medios(num,str(num).__len__())) )
   
def prueba2(num,size):
    print "%s\t%-10s\t\%s\t%s"%(num,
                        num*num,
                        num2numeros_medios(num,size), 
                        verificar(num2numeros_medios(num,size)) )
                        
   
prueba(123)
prueba(999)
prueba(1234)
prueba(9999)
prueba(11111)
prueba(99999)
prueba(111111)
prueba(999999)
prueba(2456)
prueba(10000)
prueba(5735)      
prueba2(319,4)    
#Metodo de los Cuadrados Medios

def metodo_cuadrados_medios(semilla, cantidad, size_x):
    x = range(1,cantidad+1)
    r = list()
    for i in range(1,cantidad):
        if i == 1:
            print int(num2numeros_medios(semilla, size_x))
           
            x[i] = int(num2numeros_medios(semilla, size_x))
            r.append( verificar(num2numeros_medios(semilla, size_x)) )

        else:
            print num2numeros_medios(x[i-1], size_x)
            x[i] = int(num2numeros_medios(x[i-1], size_x))
            r.append( verificar(num2numeros_medios(x[i-1], size_x)) )

        print "%s"%r
        
        
metodo_cuadrados_medios(5735,10,4)
