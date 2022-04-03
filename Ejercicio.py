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
    print("El correo es válido, acceso permitido.")
  else:
    print("El correo no es válido, acceso denegado")
  try:
    re.search(".*@.*\..*", c)
    if re.search(".*@.*\..*", correo):
    print("El correo es válido, acceso permitido.")  
    
  