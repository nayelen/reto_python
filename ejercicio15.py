#  Clase UsuarioBanco :
# Explicación del ejercicio:
# Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

class UsuarioBanco:
  def __init__(self, nombre, saldo, cuenta_corriente):
    """
    Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
    """
    self.nombre = nombre
    self.saldo = saldo
    self.cuenta_corriente = cuenta_corriente
    
  def __str__(self):
    return(f"Usuario {self.nombre}, saldo {self.saldo}€, Cuenta corriente:{'Sí' if self.cuenta_corriente else 'No'} ")
  def retirar_dinero(self, monto):
    """
    Retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    Args:
        monto (float): monto a retirar
    """
    if monto <= 0:
      raise ValueError("El monto a retirar debe ser mayor que 0")
    elif monto > self.saldo:
      raise ValueError("No hay suficiente saldo en la cuenta corriente")
    else:
      self.saldo -= monto
      print(f"{self.nombre} ha retirado {monto}€. Saldo restante {self.saldo}€")
  def transferir_dinero(self,otro_usuario, monto):
    """
    Transferir dinero desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
    Args:
        otro_usuario (UsuarioBanco): usuario al que se transferirá el dinero
        monto (float): monto a transferir
    """
    if monto <= 0:
      raise ValueError("El importe a transferir debe ser mayor que 0€")
    elif monto > otro_usuario.saldo:
      raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo en su cuenta corriente")
    else:
      otro_usuario.saldo -= monto
      self.saldo += monto
      print(f"{otro_usuario.nombre} ha transferido {monto:.2f}€ a {self.nombre}")
      print(f"El saldo restante de {otro_usuario.nombre} es {otro_usuario.saldo:.2f}€")
      print(f"{self.nombre} tiene ahora {self.saldo:.2f}€ en su cuenta corriente")
    
  def agregar_dinero(self, monto):
    """
    Agregar dinero al saldo del usuario.
    Args:
        monto (float): monto a agregar
    """
    if monto <= 0:
      raise ValueError("El importe a agregar debe ser mayor que cero")
    else:
     self.saldo += monto
     print(f"{self.nombre} ha agregado {monto}€ a su cuenta corriente. Saldo actual {self.saldo:.2f}€")
     

# Prueba del código
usuario1 =UsuarioBanco("Alicia", 100, True)
usuario2 =UsuarioBanco ("Bob", 50, True)

print(usuario1)
print(usuario2)

usuario1.agregar_dinero(50)
usuario1.transferir_dinero(usuario2, 8)
usuario1.retirar_dinero(50)