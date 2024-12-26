#  Función contar_caracteres :
# Descripción: Crea una función que cuente el número de caracteres en una cadena de texto dada.

cadena= "Esta es una prueba de caracteres"
def contar_caracteres(cadena):
  caracteres = len(cadena)
  return caracteres
print(contar_caracteres(cadena))
   
def contar_caracteres_sin_espacios(cadena):
  palabras = cadena.split() #elimina los espacios de la cadena
  caracteres = "".join(palabras) #une los caracteres para poder contabilizarlos
  return len(caracteres)
print(contar_caracteres_sin_espacios(cadena))
