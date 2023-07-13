"Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con"
"una lista vacía y otra con una lista vacía"

list_1 = []
list_2 = ["año", "edad", "curso", "carrera", "cumpleaños"]


if len(list_1) == 0:
    print("la lista esta vacia")

if len(list_2) != 0:
    print("la lista esta llena y sus componentes son: {}".format(list_2))
