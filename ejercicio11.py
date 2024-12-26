# Función numeros_pares usando lambdas y filter :
# Descripción del ejercicio: Crea una función lambda que filtre los números pares de una lista dada.
# Caso de uso: lista_numeros = [24, 56, 23, 19,-1, 0]

lista_numeros = [24, 56, 23, 19,-1, 0]

numeros_pares = list(filter(lambda x : x % 2 == 0, lista_numeros))
print(numeros_pares)