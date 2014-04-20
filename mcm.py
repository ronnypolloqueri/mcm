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
        return "excep"
    else:
        return numero/math.pow(10,size)


def num2numeros_medios(numero, num_digitos_pedidos):
    cadena_split='error'
    size_numero = str(numero).__len__()

    str_num_cuadrado = str(numero*numero)
    p = (str(numero*numero).__len__() % 2 == 0)
    q = (num_digitos_pedidos % 2 == 0)
    # p <-> q
    #print "============="
    #print "P es: "+ str(p)
    #print "Q es: "+ str(q)
    #if ((not p) or q ) and ((not q) or p):
       # print "ok"
    #   pass
    #else:
    #print "numero de digitos p : %s" % num_digitos_pedidos
    dif =  (2*num_digitos_pedidos) - str(numero*numero).__len__()
    for i in range(dif):
        str_num_cuadrado = '0'+ str_num_cuadrado
    #print "cambio.. %s" % str_num_cuadrado
    marca = (str_num_cuadrado.__len__() - num_digitos_pedidos)/2
    #print "La marca: %s"%marca
    cadena_split = str_num_cuadrado[marca:-marca]

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


#prueba(123)
#prueba(999)
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
    num = semilla
    num_ant = 1001
    for i in range(cantidad):
        prueba2(num,size_x)
        num = int(num2numeros_medios(num,size_x))
        if verificar(num2numeros_medios(num_ant,size_x)) == "excep":
            break
        num_ant = num


print "*********************************"
metodo_cuadrados_medios(5735,10,4)
print "*********************************"
metodo_cuadrados_medios(1001,10,4)
print "*********************************"
metodo_cuadrados_medios(6634,10,4)
print "*********************************"
metodo_cuadrados_medios(66342,10,5)
metodo_cuadrados_medios(1000,10,5)

