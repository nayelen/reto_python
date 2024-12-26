#Función calcular_promedio :
#Descripción: Crea una función que calcule el promedio de una lista de números


lista = [1, 2, 3, 4, 5, 6, 7]
def calcular_promedio(lista):
  promedio = sum(lista) / len(lista)
  return promedio
print(calcular_promedio(lista))
