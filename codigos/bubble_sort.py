import time

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):

        print("Iteracion: ",i+1)

        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista,"\nMovimiento:",j+1)
                time.sleep(2)
        print("Iteracion: ",i+1)
# Ejemplo de uso

if __name__ == "__main__":
    # Lista de números desordenados
    numeros = [1,5,6,3,8,2,9,7,4,10]

    print("Lista desordenada", numeros)

    # Llama a la función de ordenamiento de burbuja
    bubble_sort(numeros)

    # Imprime la lista ordenada
    print("Lista ordenada:", numeros)
