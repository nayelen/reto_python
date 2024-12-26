# Función encontrar_puesto_empleado
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

empleados = [
  {
   'nombre': "Juan", 
   'apellido': "García", 
   'puesto': "Secretario"
   },
  {
   'nombre': "Mabel", 
   'apellido': "García", 
   'puesto': "Product Manager"
   },
  {
    'nombre': "Isabel", 
    'apellido': "Martín", 
    'puesto': "CEO"
  }]

def encontrar_puesto_empleado(nombre_completo, lista):
  """Busca un empleado en la lista de diccionarios y devuelve su puesto.

  Args:
      nombre_completo (str): El nombre completo del empleado a buscar.
      lista (list): Lista de diccionarios con 'nombre', 'apellido' y 'puesto'.

  Returns:
        str: El puesto del empleado si está en la lista, o un mensaje indicando que no trabaja aquí.
  """
  nombre_completo = " ".join(nombre_completo.strip().lower().split())
  
  for empleado in lista:
    #se construye el nombre completo del empleado desde el diccionario
    nombre_empleado = f"{empleado['nombre'].strip()} {empleado['apellido'].strip()}".lower() #unimos el nombre con el apellido del empleado quitando espacios y pasandolo a minusculas
    if nombre_completo == nombre_empleado:
      #comparamos los nombres completos y si coinciden se devuelve el nombre con el puesto que ocupa
      return f"{nombre_completo.title()} trabaja aqui como {empleado['puesto']}"
  return f"{nombre_completo.title()} no trabaja aquí"

buscar_nombre = input("Ingrese el nombre del empleado a buscar: ")
print(encontrar_puesto_empleado(buscar_nombre, empleados))

