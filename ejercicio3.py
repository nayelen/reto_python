#Función encontrar_duplicado :
#Descripción:Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

lista = [1, 3, 4, 2, 5, 3, 4, 5]
def encontrar_duplicado(lista):
  """Parámetros:
    lista (list): Lista de elementos a evaluar.

    Retorna:
    Elemento duplicado si existe, o None si no hay duplicados.
    """
  for i in range(len(lista)):
    #compara el elemento actual con el anterio en la lista
    if lista[i] in lista[:i]:
      return lista[i]
  return None  # No hay duplicados en la lista
      
      
print(encontrar_duplicado(lista))

