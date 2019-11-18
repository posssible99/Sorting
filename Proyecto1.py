import metord,os.path
from datetime import datetime
if __name__ == "__main__":
    import random
    import time
    import sys
    sys.setrecursionlimit(15000000)
    lista=[]
    if os.path.isfile("input234.eda"):
        try:
            file2=open("input.eda","r")
            lista=file2.readlines()
            file2.close()
            lista = [int(i) for i in lista] 
            print("---Se tomaron los numeros del archivo---")
        except Exception as err:
            print("Error",err)
        finally:
            if file2:
                file2.close()
    else:
        print("Archivo invalido")
        lista=metord.listaAleatorios(10000)
        print("---Se generaron aleatoriamente los numeros---")
    lista1=lista[:]
    lista2=lista[:]
    lista3=lista[:]
    lista4=lista[:]
    lista5=lista[:]
    lista6=lista[:]
    t1=time.time()
    metord.bubblesort(lista1)
    t2=time.time()
    tbubble=t2-t1
    t3=time.time()
    metord.insertionsort(lista2)
    t4=time.time()
    tinser=t4-t3
    t5=time.time()
    metord.counting_sort(lista3)
    t6=time.time()
    tcounting=t6-t5
    t7=time.time()
    metord.radixSortord(lista4)
    t8=time.time()
    tradix=t8-t7
    t9=time.time()
    metord.Quicksortord(lista5,0,len(lista5)-1)
    t10=time.time()
    tquick=t10-t9
    t11=time.time()
    lista6=metord.mergesortord(lista6)
    t12=time.time()
    tmerge=t12-t11
    dic={tbubble:"Tiempo del bubble sort",tinser:"Tiempo del insertion sort",tcounting:"Tiempo del counting sort",tradix:"Tiempo del radix sort",tquick:"Tiempo del Quick sort",tmerge:"Tiempo del merge sort"}
    listad=sorted(dic.keys())
    for i in reversed(listad):
        print(dic[i],i)
    try:
        file1=open("resultados.eda","a")
        file1.write(str(datetime.now())+"\n")
        file1.write("Tamaño de la coleccion:"+str(len(lista))+"\n")
        for i in reversed(listad):
            file1.write(str(dic[i])+":"+str(i)+"\n")
    except Exception as err:
        print("Error",err)
    finally:
        if file1:
            file1.close()
    
    
    
    
    
