import random
def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                

# Ejemplo de uso
if __name__ == "__main__":
    #  caso 1 Lista  pequeña de números desordenados 
    numeros = [64, 34, 25, 12, 22, 11, 90]
    #caso 2 numeros invertidos
    numero_invertidos =  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #caso 3 lista de gran volumen de datos
    datos_desordenados = list(range(1, 130000001))

    # Llama a la función de ordenamiento de burbuja
    bubble_sort(numeros)

    # Imprime la lista ordenada
    print("Lista ordenada:", datos_desordenados)
