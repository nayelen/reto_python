# Función procesar_texto :
# Explicación del ejercicio:
# Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
# contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras
# funciones que tenemos que definir primero y llamar dentro de la función procesar texto.


def contar_palabras(texto):
    palabras = texto.split()
    contador_palabras = {}
    for palabra in palabras:
      palabra = palabra.lower()
      if palabra in contador_palabras:
        contador_palabras[palabra] += 1
      else:
        contador_palabras[palabra] = 1
    return contador_palabras
# print(contar_palabras(texto))

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)
# print(reemplazar_palabras(texto, "palabras", "palabritas" ))

def eliminar_palabra(texto, palabra_eliminar):
  palabras = texto.split()
  for palabra in palabras:
    if palabra.lower() == palabra_eliminar.lower():
      palabras.remove(palabra)
  return " ".join(palabras)

# print(eliminar_palabra(texto, "palabras"))
  
def procesar_texto(texto,opcion, *args):
  if opcion == "contar":
    return contar_palabras(texto)
  elif opcion == "reemplazar":
    palabra_original, palabra_nueva = args
    return reemplazar_palabras(texto, palabra_original, palabra_nueva)
  elif opcion == "eliminar":
    palabra_eliminar = args[0]
    return eliminar_palabra(texto, palabra_eliminar)
  else:
    return ValueError("Opción inválida. Usa 'contar', 'reemplazar' o 'eliminar'.")
  
  
texto = "Este es un ejemplo de texto, este texto contiene palabras repetidas."
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "texto", "relato"))
print(procesar_texto(texto, "eliminar", "ejemplo"))