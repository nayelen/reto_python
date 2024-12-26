#Función enmascarado_datos :
#Descripción: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarado_datos(variable):
  """Parámetros:
    variable (str): Cadena de texto a enmascarar.

  Retorna:
    Cadena de texto enmascarada.
  """
  cadena = str(variable)
  if len(cadena) <= 4:
    return cadena  # Si la cadena tiene menos de 4 caracteres, no hay nada que enmascarar
      
  # Enmascarar todos los caracteres excepto los últimos cuatro
  return '#' * (len(cadena) - 4) + cadena[-4:]


  
  
variable = 436854367854
print(enmascarado_datos(variable))