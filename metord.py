import random
def bubblesort(lista):
    for i in range(0,len(lista)-1):
        hubointercambios=False
        for j in range (0,len(lista)-1-i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                hubointercambios=True
        if not hubointercambios:
            return

def Quicksortord(A,p,r):
    def intercambia(A,x,y):
        tmp=A[x]
        A[x]=A[y]
        A[y]=tmp

    def Particionar(A,p,r):
        x=A[p]
        i=p
        for j in range (p+1,r+1):
            if(A[j]<=x):
                i=i+1
                intercambia(A,i,j)
        intercambia(A,i,p)
        return i

    def Quicksort(A,p,r):
        if(p<r):
            q=Particionar(A,p,r)
            Quicksort(A,p,q-1)
            Quicksort(A,q+1,r)
    Quicksort(A,p,r)

def mergesortord(lista):
    def mergesort(lista):
        if len(lista) <= 1: 
            return lista
        mitad = len(lista) // 2
        izq = mergesort(lista[:mitad])
        der = mergesort(lista[mitad:])
        return merge(izq, der)

    def merge(izq, der):
        indiceizq,indiceder = 0, 0
        result = []
        while indiceizq < len(izq) and indiceder < len(der):
            if izq[indiceizq] < der[indiceder]:
                result.append(izq[indiceizq])
                indiceizq += 1
            else:
                result.append(der[indiceder])
                indiceder += 1
        result += izq[indiceizq:]
        result += der[indiceder:]
        return result
    lista=mergesort(lista)
    return lista

def insertionsort(arr):
    for i in range(1,len(arr)):
        val=arr[i]
        j=i-1
        while arr[j]>val and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=val

def counting_sort(arr):
    n=max(arr)
    count=[0]*(n+1)
    temp=arr[:]
    for i in arr:
        count[i]+=1
    count[0]-=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    for i in range(len(arr)-1,-1,-1):
        value=temp[i]
        index=count[value]
        arr[index]=value
        count[value]-=1

def radixSortord(arr):
    def countingSort(arr, exp1): 
        n = len(arr)  
        salida = [0] * (n) 
        count = [0] * (10) 
        for i in range(0, n): 
            idx = (arr[i]/exp1) 
            count[ int((idx)%10) ] += 1

        for i in range(1,10): 
            count[i] += count[i-1] 

        i = n-1
        while i>=0: 
            idx = (arr[i]/exp1) 
            salida[ count[ int((idx)%10) ] - 1] = arr[i] 
            count[ int((idx)%10) ] -= 1
            i -= 1

        i = 0
        for i in range(0,len(arr)): 
            arr[i] = salida[i] 
    
    def radixSort(arr): 
        max1 = max(arr) 
        exp = 1
        while max1/exp > 0: 
            countingSort(arr,exp) 
            exp *= 10
    radixSort(arr)

def listaAleatorios(n):
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(0, 100)
    return lista