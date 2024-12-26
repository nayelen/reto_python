# Función numeros_suma usando lambdas y map :
# Descripción del ejercicio: Crea una función lambda que sume 3 a cada número de una lista dada.
# Caso de uso: lista_numeros = [24, 56, 23, 19,-1, 0]

lista_numeros = [24, 56, 23, 19,-1, 0]
numeros_suma = list(map(lambda x : x + 3, lista_numeros))
print(numeros_suma)