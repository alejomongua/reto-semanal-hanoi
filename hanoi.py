#!/usr/bin/python3

import sys

LIMITE_SUPERIOR = 64

discos = 0

# Intente leer la cantidad de discos desde la entrada del usuario:
if len(sys.argv) > 1:
  try:
    discos = int(sys.argv[1])
    if not 0 < discos < LIMITE_SUPERIOR:
      print('La cantidad de discos debe estar entre 1 y 64')
      discos = 0
  except:
    print('La cantidad de discos ingresada no es válida')

while not discos:
  entrada = input('Ingrese la cantidad de discos [1-64]: ')
  try:
    discos = int(entrada)
    if not 0 < discos < LIMITE_SUPERIOR:
      print('La cantidad de discos debe estar entre 1 y 64')
      discos = 0
  except:
    print('La cantidad de discos ingresada no es válida, ingrese un número entero')

if discos > 8:
  print(f'La cantidad de discos es alta, se necesitan {2**discos - 1} movimientos para completar la tarea.')
  input('Si desea salir presione Ctrl + C en cualquier momento, para continuar presione ENTER')

inicial = [x + 1 for x in range(discos)]
inicial.reverse()
auxiliar = []
final = []
pasos = 0

def mover(origen, destino):
  global pasos
  elemento = origen.pop()
  destino.append(elemento)
  pasos += 1
  print(f'Paso {pasos}: movido {elemento}')
  print(f'Inicial: {inicial}')
  print(f'Auxiliar: {auxiliar}')
  print(f'Final: {final}')
  print()

def ordenar(cantidad, _inicial, _auxiliar, _final):
  if cantidad:
    ordenar(cantidad - 1, _inicial, _final, _auxiliar)
    mover(_inicial, _final)
    ordenar(cantidad - 1, _auxiliar, _inicial, _final)

ordenar(discos, inicial, auxiliar, final)
print(f'Logrado en {pasos} pasos')
