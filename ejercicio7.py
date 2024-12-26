# Función fibonacci :
#Crea una función que calcule el término n de la serie de Fibonacci utilizando recursión.
# Ejemplo para los primeros 5 términos de la función de Fibonacci: [0, 1, 1, 2, 3]
# Primer término: 0 (0)
# Segundo término: 1 (1)
# Tercer término: 1 (0 + 1)
# Cuarto término: 2 (1 + 1)
# Quinto término: 3 (1 + 2)

def fibonacci(n):
  if n < 0:
    raise ValueError("El número debe ser un entero positivo")
  elif n == 0:
    return 0  # primer término de la serie de Fibonacci es 0
  elif n == 1 or n ==2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
  
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))