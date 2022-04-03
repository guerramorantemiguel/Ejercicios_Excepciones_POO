# Ejercicios_Excepciones_POO
Este es el link del [repositorio]:https://github.com/guerramorantemiguel/Ejercicios_Excepciones_POO.git

# Ejercicio:

```
import re

class Email():
  def __init__(self,correo):
    self.correo = correo
  def __str__(self):
    return self.correo
try:
  correo = input(str('Introduzca el correo electrónico'))
  c = correo
  re.search(".*@.*\..*", c)
  if re.search(".*@.*\..*", correo):
    print("El correo es válido, acceso permitido. ¡Bienvenido Vicente!")
  else:
    print("El correo no es válido, acceso denegado")
  try:
    correo = input(str('Introduzca el correo electrónico'))
    c = correo
    re.search(".*@.*\..*", c)
    if re.search(".*@.*\..*", correo):
      print("El correo es válido, acceso permitido. ¡Bienvenido Vicente!")
    else: 
      print("La dirección de correo debe tener el siguiente formato: xxx@xxx.xx")
  elif: 
    correo = input(str('Introduzca el correo electrónico'))
    c = correo
    re.search(".*@.*\..*", c)
    if re.search(".*@.*\..*", correo):
      print("El correo es válido, acceso permitido. ¡Bienvenido Vicente!")
    else: 
      print("Cuenta bloqueada, posible caso de ataque")
```

# Main:
```

```
