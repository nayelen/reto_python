# No te vayas por las ramas :
# Explicación del ejercicio:
# Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
  def __init__(self, altura_tronco = 1):
    """
    Inicializa un árbol genérico.
    param altura_tronco: Altura inicial del tronco (en metros).
    """
    self.altura_tronco = altura_tronco
    self.ramas = []
  def crecer_tronco(self):
    """
    Incrementa la longitud del tronco en una unidad.
    """
    self.altura_tronco += 1
  def nueva_rama(self):
    """
    Agrega una nueva rama de longitud 1 a la lista de ramas.
    """
    self.ramas.append(1)
  def crecer_ramas(self):
    """
    Incrementa en una unidad la longitud de todas las ramas existentes.
    """
    self.ramas = [rama + 1 for rama in  self.ramas]
    
  def quitar_rama(self,posicion):
    """
    Eliminar una rama en una posición específica
    """
    if 0 <= posicion < len(self.ramas):
      self.ramas.pop(posicion)
    else:
      print("Posición inválida, no se puede eliminar la rama")
  def info_arbol(self):
    """
    Devuelve información sobre el árbol, incluyendo altura del tronco y el numero de ramas y sus longitudes.
    """
    info = f"Longitud del tronco: {self.altura_tronco}\n"
    info += f"Número de ramas: {len(self.ramas)}\n"
    info += f"Longitudes de las ramas: {', '.join(map(str, self.ramas)) if self.ramas else 'No hay ramas'}"
    return info

# Ejemplo de uso
arbol = Arbol()

# Inicializar y manipular el árbol según los métodos
arbol.crecer_tronco()
arbol.crecer_tronco()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.crecer_ramas()
arbol.quitar_rama(1)

# Información del árbol
print(arbol.info_arbol())