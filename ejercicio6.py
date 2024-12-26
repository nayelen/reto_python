# Función buscar_nombre :
# Descripción: Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
# Caso de uso: Incorpora los siguientes nombres a la lista y comprueba que la función
# funciona correctamente: " Jaime", "Silvia" y "Ana".

def buscar_nombre(nombres):
  """
  Busca un nombre de la lista proporcionada

  Args:
      nombres (list): lista de nombres

  Raises:
      ValueError: devuelve error si el nombre a buscar no está en la lista
  """
  nombre_buscado = input("Ingrese el nombre a buscar: ").strip().lower() #quitamos los espacios y pasamos todo a minúsculas
  if nombre_buscado in [n.lower() for n in nombres]:
    #convertimos la lista original a minusculas para que sea ino haya errores con las mayusculas o minusculas
    print(f"El nombre {nombre_buscado} está en la lista")
  else:
    raise ValueError(f"El nombre {nombre_buscado} no está en la lista")

nombres = ["Jaime", "Silvia", "Ana","pedro"]
buscar_nombre(nombres)