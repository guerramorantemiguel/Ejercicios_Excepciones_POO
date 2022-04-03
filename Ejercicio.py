import re

class Email():
  def __init__(self,correo):
    self.correo = correo
  def __str__(self):
    return self.correo
try:
  correo = input(str('Introduzca el correo electrónico'))
  c = correo