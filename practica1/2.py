"""Usando el concepto y funciones de listas, realizando un programa con
las siguientes caracteristicas (3 puntos):
Reglas:
- Crear una lista con 10 valores aleatorios o aleatorios (Pista: Usar el método
agregar y para)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""
import random

milista = []

for i in range(10):
    milista.append(random.randrange(1, 20))
    print("mi lista actual es: {}".format(milista))

"cuadrados"
mi_cuadrado = []
for j in milista:
    mi_cuadrado.append(j ** 2)
    print("mi lista de cuadrados es: {}".format(mi_cuadrado))
"cubo"
mi_cubo = []
for a in milista:
    mi_cubo.append(a ** 3)
    print("mi lista de cubos es: {}".format(mi_cubo))

suma_listas = mi_cuadrado + mi_cubo

suma_listas.reverse()

print("la lista inversa de la suma de ambas listas es: {}".format(suma_listas))