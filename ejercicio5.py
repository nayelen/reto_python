#Función es_anagrama :
#Descripción: Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def es_anagrama(palabra1, palabra2):
  palabra1 = palabra1.replace(" ","").lower()
  palabra2 = palabra2.replace(" ","").lower()
  #se elimina los espacios y se convierten en minusculas
  
  #comparar las letras ordenadas
  return sorted(palabra1) == sorted(palabra2)

print(es_anagrama("amor", "roma"))  # True
print(es_anagrama("hola", "adios"))  #False

