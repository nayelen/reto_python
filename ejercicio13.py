#  Función sumar_listas usando lambdas:
# Descripción del ejercicio:
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# Caso de uso: lista_numeros_1 = [1, 4, 5, 6 , 7 , 7] ;
# lista_numeros_2 = [3, 11, 34, 56]

lista_numeros_1 = [1, 4, 5, 6 , 7 , 7]
lista_numeros_2 = [3, 11, 34, 56]

sumar_listas = lambda list1, list2 : sum(list1) + sum(list2)
print(sumar_listas(lista_numeros_1, lista_numeros_2))